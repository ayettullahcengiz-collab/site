var StorySlider = StorySlider || (function () {
    const sliderInitialDelay = 4500;
    let storyCont = '';
    let bannerGroupId = '';
    let mainSlider = '';
    let sliderDelay = sliderInitialDelay;
    let timeOutId = '';
    let activeBulletForPause = '';
    let activeSliderVideoForPause = '';
    let isMobileDevice = false;
    let storyRoot = null;

    function setActiveStoryContext(groupId, container, mobileDevice) {
        bannerGroupId = groupId;
        storyCont = container;
        storyRoot = container?.parentElement || null;
        isMobileDevice = mobileDevice;
    }

    function getStoryScope() {
        return storyRoot || storyCont || document;
    }

    function pushStoryEvent(eventName, parameters) {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            event: eventName,
            ...parameters
        });
    }

    function getStoryId(element) {
        if (!element) {
            return '';
        }

        if (element.dataset?.bannerId) {
            return element.dataset.bannerId;
        }

        const childWithBannerId = element.querySelector?.('[data-banner-id]');
        if (childWithBannerId?.dataset?.bannerId) {
            return childWithBannerId.dataset.bannerId;
        }

        const parentWithBannerId = element.closest?.('[data-banner-id]');
        return parentWithBannerId?.dataset?.bannerId || '';
    }

    function getActiveMainSlide() {
        if (!mainSlider || !mainSlider.slides || mainSlider.activeIndex == null) {
            return null;
        }

        return mainSlider.slides[mainSlider.activeIndex] || null;
    }

    function getNestedSlider(mainSlide) {
        return mainSlide?.getElementsByClassName('js_story_slider_nested')?.[0]?.swiper || null;
    }

    function getActiveStorySlide() {
        const activeMainSlide = getActiveMainSlide();
        const nestedSlider = getNestedSlider(activeMainSlide);

        if (!nestedSlider || nestedSlider.activeIndex == null) {
            return activeMainSlide;
        }

        return nestedSlider.slides[nestedSlider.activeIndex] || activeMainSlide;
    }

    function getFirstStoryId(mainSlide) {
        if (!mainSlide) {
            return '';
        }

        const nestedSlider = getNestedSlider(mainSlide);
        if (nestedSlider?.slides?.length) {
            return getStoryId(nestedSlider.slides[0]);
        }

        const firstStory = mainSlide.querySelector?.('[data-banner-id]');
        return getStoryId(firstStory || mainSlide);
    }

    function pushStoryBlockChange(previousMainSlide, nextMainSlide) {
        if (!previousMainSlide || !nextMainSlide || previousMainSlide === nextMainSlide) {
            return;
        }

        pushStoryEvent('stories_block_change', {
            stories_block_id: nextMainSlide.dataset?.blockId || '',
            previous_stories_block_id: previousMainSlide.dataset?.blockId || '',
            stories_id: getFirstStoryId(nextMainSlide)
        });
    }

    function handleNestedNextAnalytics(e) {
        if (!mainSlider || mainSlider.destroyed === true) {
            return;
        }

        const button = e.currentTarget;
        const nestedSlider = button.closest('.js_story_slider_nested')?.swiper || button.parentNode?.swiper;

        if (!nestedSlider) {
            return;
        }

        const currentIndex = nestedSlider.activeIndex;
        const lastIndex = nestedSlider.slides.length - 1;

        if (currentIndex < lastIndex) {
            const previousStory = nestedSlider.slides[currentIndex];
            const nextStory = nestedSlider.slides[currentIndex + 1];

            pushStoryEvent('stories_next_click', {
                stories_id: getStoryId(nextStory),
                previous_stories_id: getStoryId(previousStory)
            });

            return;
        }

        if (!mainSlider.isEnd) {
            const previousMainSlide = mainSlider.slides[mainSlider.activeIndex];
            const nextMainSlide = mainSlider.slides[mainSlider.activeIndex + 1];

            pushStoryBlockChange(previousMainSlide, nextMainSlide);
        }
    }

    function handleNestedPrevAnalytics(e) {
        if (!mainSlider || mainSlider.destroyed === true) {
            return;
        }

        const button = e.currentTarget;
        const nestedSlider = button.closest('.js_story_slider_nested')?.swiper || button.swiper || button.parentNode?.swiper;

        if (!nestedSlider) {
            return;
        }

        const currentIndex = nestedSlider.activeIndex;

        if (currentIndex > 0) {
            const previousStory = nestedSlider.slides[currentIndex];
            const nextStory = nestedSlider.slides[currentIndex - 1];

            pushStoryEvent('stories_back_click', {
                stories_id: getStoryId(nextStory),
                previous_stories_id: getStoryId(previousStory)
            });

            return;
        }

        if (!mainSlider.isBeginning) {
            const previousMainSlide = mainSlider.slides[mainSlider.activeIndex];
            const nextMainSlide = mainSlider.slides[mainSlider.activeIndex - 1];

            pushStoryBlockChange(previousMainSlide, nextMainSlide);
        }
    }

    function handleStoryActionClick(e) {
        const actionElement = e.currentTarget;

        const storySlide = actionElement.closest('[data-banner-id]');
        const clickLink =
            actionElement.getAttribute('href') ||
            actionElement.dataset.url ||
            actionElement.dataset.href ||
            '';

        pushStoryEvent('stories_button_click', {
            stories_id: getStoryId(storySlide),
            click_link: clickLink
        });
    }

    function bindAnalyticsEvents() {
        const scope = getStoryScope();

        scope.querySelectorAll('.js_nested_slider_next').forEach((item) => {
            item.removeEventListener('click', handleNestedNextAnalytics, true);
            item.addEventListener('click', handleNestedNextAnalytics, true);
        });

        scope.querySelectorAll('.js_nested_slider_prev').forEach((item) => {
            item.removeEventListener('click', handleNestedPrevAnalytics, true);
            item.addEventListener('click', handleNestedPrevAnalytics, true);
        });

        scope.querySelectorAll('.story-link').forEach((item) => {
            item.removeEventListener('click', handleStoryActionClick, false);
            item.addEventListener('click', handleStoryActionClick, false);
        });
    }

    function slidersInit(initialSlide) {
        if (!storyCont) {
            return;
        }

        storyCont.querySelectorAll('.js_story_slider_nested').forEach((sliderElement) => {
            new Swiper(sliderElement, {
                slidesPerView: 1,
                nested: true,
                allowTouchMove: false,
                navigation: {
                    nextEl: sliderElement.querySelector('.js_nested_slider_next'),
                    prevEl: sliderElement.querySelector('.js_nested_slider_prev'),
                },
                pagination: {
                    el: sliderElement.querySelector('.js_story_pgination'),
                    clickable: false,
                    bulletActiveClass: 'nested__pagination-bullet-active',
                    renderBullet: function (index, className) {
                        return `<div class="story-nested__pagination-bullet ${className} js_nested_pb" data-index="${index}"><span></span></div>`;
                    },
                },
                on: {
                    reachEnd: function (swiper) {
                        if (swiper.slides.length > 1) {
                            setStoryAsSeen(swiper.wrapperEl.closest('.js_main_slide').dataset.blockId);
                        }
                        swiper.navigation.nextEl.addEventListener('click', slideMainNext, false);
                    },
                    reachBeginning: function (swiper) {
                        swiper.navigation.prevEl.swiper = swiper;
                        swiper.navigation.prevEl.addEventListener('click', slideMainPrev, false);
                    },
                    slideNextTransitionStart: function (swiper) {
                        swiper.navigation.prevEl.removeEventListener('click', slideMainPrev, false);
                    },
                    slidePrevTransitionStart: function (swiper) {
                        swiper.navigation.nextEl.removeEventListener('click', slideMainNext, false);
                    },
                    slideChange: function (swiper) {
                        let pItems = swiper.pagination.bullets;
                        let pItemsLength = pItems.length;
                        for (let i = 0; i < pItemsLength; i++) {
                            if (pItems[i].dataset.index < swiper.realIndex) {
                                pItems[i].classList.add('seen');
                            } else {
                                pItems[i].classList.remove('seen');
                            }
                        }
                        if (mainSlider.isBeginning) {
                            if (swiper.isBeginning) {
                                swiper.navigation.prevEl.classList.add('hidden');
                            } else {
                                swiper.navigation.prevEl.classList.remove('hidden');
                            }
                        }
                        if (mainSlider.isEnd) {
                            if (swiper.isEnd) {
                                swiper.navigation.nextEl.classList.add('hidden');
                            } else {
                                swiper.navigation.nextEl.classList.remove('hidden');
                            }
                        }
                        manageStoryVideoSlide(swiper);
                        if (timeOutId != '') {
                            timeOutId.cancel();
                        }
                        if (swiper.isEnd) {
                            timeOutId = new customPauseResumeTimer(function () { mainSlider.slideNext(200); }, sliderDelay);
                        } else {
                            timeOutId = new customPauseResumeTimer(function () { swiper.slideNext(200); }, sliderDelay);
                        }
                    }
                }
            });
        });

        const mainSliderElement = storyCont.querySelector(`#js_story_slider_${bannerGroupId}`);
        if (!mainSliderElement) {
            return;
        }

        mainSlider = new Swiper(mainSliderElement, {
            slidesPerView: 3.5,
            initialSlide: initialSlide,
            spaceBetween: 30,
            allowTouchMove: false,
            centeredSlides: true,
            on: {
                slideChange: manageNestedSliderAutoplay,
                afterInit: function (swiper) {
                    setTimeout(() => {
                        manageNestedSliderAutoplay(swiper);
                        if (swiper.activeIndex == 0) {
                            let activeSw = swiper.slides[0].getElementsByClassName('js_story_slider_nested')[0].swiper;
                            if (activeSw.slides.length == 1) {
                                setStoryAsSeen(activeSw.wrapperEl.closest('.js_main_slide').dataset.blockId);
                            }
                        }
                    }, 500);
                },
                activeIndexChange: function (swiper) {
                    setTimeout(() => {
                        let activeSw = swiper.slides[swiper.activeIndex].getElementsByClassName('js_story_slider_nested')[0].swiper;
                        if (activeSw.slides.length == 1) {
                            setStoryAsSeen(activeSw.wrapperEl.closest('.js_main_slide').dataset.blockId);
                        }
                    }, 500);
                },
            },
            breakpoints: {
                1370: {
                    slidesPerView: 4,
                },
                1453: {
                    slidesPerView: 4.5,
                },
                1536: {
                    slidesPerView: 4.75,
                },
                1783: {
                    slidesPerView: 5.5,
                }
            }
        });

        bindAnalyticsEvents();
    }

    function bindStoryWidgetEvents(localRoot, localStoryCont, localBannerGroupId, localIsMobileDevice) {
        if (!localRoot || !localStoryCont) {
            return;
        }

        const activateContext = () => {
            setActiveStoryContext(localBannerGroupId, localStoryCont, localIsMobileDevice);
        };

        if (localIsMobileDevice) {
            localStoryCont.querySelectorAll('.js_main_slide').forEach((item) => {
                item.addEventListener('touchstart', function () {
                    activateContext();

                    let index = Number(this.dataset.index);
                    const previousMainSlide = getActiveMainSlide();
                    const nextMainSlide = mainSlider?.slides?.[index];

                    if (previousMainSlide && nextMainSlide && mainSlider.activeIndex != index) {
                        pushStoryBlockChange(previousMainSlide, nextMainSlide);
                    }

                    mainSlider?.slideTo(index, 500);
                });
            });
        } else {
            localStoryCont.querySelectorAll('.js_main_slide').forEach((item) => {
                item.addEventListener('click', function () {
                    activateContext();

                    let index = Number(this.dataset.index);
                    const previousMainSlide = getActiveMainSlide();
                    const nextMainSlide = mainSlider?.slides?.[index];

                    if (previousMainSlide && nextMainSlide && mainSlider.activeIndex != index) {
                        pushStoryBlockChange(previousMainSlide, nextMainSlide);
                    }

                    mainSlider?.slideTo(index, 500);
                });
            });
        }

        localStoryCont.querySelectorAll('.js_nested_items').forEach((item) => {
            initPresslHoldEvent(item, pauseSliderOnHoldStart, resumeSliderOnHoldEnd);
        });

        localRoot.querySelectorAll('.js_story_preview').forEach((item) => {
            item.addEventListener('click', function () {
                activateContext();

                const index = Number(this.dataset.index);
                const mainSlide = localStoryCont.querySelector(
                    `.js_main_slide[data-index="${index}"]`
                );

                const firstStory = mainSlide?.querySelector('[data-banner-id]');

                pushStoryEvent('stories_start_play', {
                    stories_id: firstStory?.dataset?.bannerId || ''
                });

                slidersInit(index);

                localStoryCont.classList.remove('hidden');
                document.body.classList.add('ofh');
            });
        });

        localStoryCont.querySelectorAll('.js_story_video_mute_btn').forEach((item) => {
            item.addEventListener('click', function () {
                activateContext();

                let btn = this;
                let prevElem = btn.previousElementSibling;
                if (prevElem && prevElem.nodeName == 'VIDEO') {
                    if (prevElem.muted) {
                        prevElem.muted = false;
                        btn.classList.remove('muted');
                    } else {
                        btn.classList.add('muted');
                        prevElem.muted = true;
                    }
                }
            });
        });
    }

    document.removeEventListener('keyup', slidersDestroyOnEsc, false);
    document.addEventListener('keyup', slidersDestroyOnEsc, false);

    function manageStoryVideoSlide(swiper) {
        let slidesLength = swiper.slides.length;
        sliderDelay = sliderInitialDelay;
        for (let j = 0; j < slidesLength; j++) {
            let video = swiper.slides[j].querySelector('video');
            if (video != null) {
                showSoundIconIfVideoHasAudio(video);
                let activeBullet = swiper.slides[j].closest('.js_story_slider_nested')?.querySelector('.nested__pagination-bullet-active')?.firstChild;
                if (j == swiper.activeIndex) {
                    video.currentTime = 0;
                    video.play();
                    sliderDelay = (video.duration * 1000) - 500;
                    if (activeBullet) {
                        activeBullet.style.animationDuration = video.duration + 's';
                    }
                } else {
                    video.muted = true;
                    video.pause();
                    let btn = video.nextElementSibling;
                    if (btn?.nodeName == 'BUTTON') {
                        btn.classList.add('muted');
                    }
                }
            }
        }
    }

    function pauseSliderOnHoldStart(e) {
        if (timeOutId != '') {
            timeOutId.pause();
        }
        let trg = e.target;
        activeBulletForPause = trg.closest('.js_story_slider_nested')?.querySelector('.nested__pagination-bullet-active')?.firstChild || '';
        if (activeBulletForPause) {
            activeBulletForPause.style.animationPlayState = 'paused';
        }
        if (trg.nodeName == 'VIDEO') {
            activeSliderVideoForPause = trg;
            activeSliderVideoForPause.pause();
        } else {
            activeSliderVideoForPause = '';
        }
    }

    function resumeSliderOnHoldEnd() {
        if (timeOutId != '') {
            timeOutId.resume();
        }
        if (activeBulletForPause) {
            activeBulletForPause.style.animationPlayState = 'running';
        }
        if (activeSliderVideoForPause != '') {
            activeSliderVideoForPause.play();
        }
    }

    function setStoryAsSeen(storyId) {
        let cVal = getCookie('_stsSeen');
        if (!cVal.includes(storyId + ',')) {
            setCookie('_stsSeen', cVal += storyId + ',', 10);
            getStoryScope().querySelector('.js_story_preview[data-block-id="' + storyId + '"]')?.classList.add('seen')
        }
    }

    function slideMainNext(e) {
        e.stopPropagation();
        if (mainSlider.isEnd) {
            slidersDestroy();
        } else {
            mainSlider.slideNext(200);
        }
    }

    function slideMainPrev(e) {
        e.stopPropagation();
        if (!mainSlider.isBeginning) {
            mainSlider.slidePrev(200);
        } else {
            if (timeOutId != '') {
                timeOutId.cancel();
            }
            let activeNestedSlider = e.currentTarget.swiper;
            let activeBullet = activeNestedSlider.slides[0].closest('.js_story_slider_nested').querySelector('.nested__pagination-bullet-active')
            activeBullet.classList.remove('nested__pagination-bullet-active');
            void activeBullet.offsetWidth;
            activeBullet.classList.add('nested__pagination-bullet-active');
            timeOutId = new customPauseResumeTimer(function () { activeNestedSlider.slideNext(200); }, sliderDelay);
        }
    }

    function manageNestedSliderAutoplay(mnSlider) {
        if (mnSlider.slides.length > 0) {
            if (timeOutId != '') {
                timeOutId.cancel();
            }
            let activeIndex = mnSlider.activeIndex;
            let prevIndex = mnSlider.previousIndex;
            let activeSw = getNestedSlider(mnSlider.slides[activeIndex]);
            let prevSw = getNestedSlider(mnSlider.slides[prevIndex]);

            if (!activeSw) {
                return;
            }

            if (prevSw) {
                prevSwSlidesLength = prevSw.slides.length;
                for (let j = 0; j < prevSwSlidesLength; j++) {
                    let video = prevSw.slides[j].querySelector('video');
                    if (video != null) {
                        showSoundIconIfVideoHasAudio(video);
                        let btn = video.nextElementSibling;
                        if (btn?.nodeName == 'BUTTON') {
                            btn.classList.add('muted');
                        }
                        video.muted = true;
                        video.pause();
                    }
                }
            }
            manageStoryVideoSlide(activeSw);
            if (mainSlider.isEnd) {
                if (!activeSw.isEnd) {
                    timeOutId = new customPauseResumeTimer(function () { activeSw.slideNext(200); }, sliderDelay);
                } else {
                    timeOutId = new customPauseResumeTimer(slidersDestroy, sliderDelay);
                }
            } else {
                if (activeSw.slides.length > 1) {
                    if (activeSw.isEnd) {
                        timeOutId = new customPauseResumeTimer(function () { mainSlider.slideNext(200); }, sliderDelay);
                    } else {
                        timeOutId = new customPauseResumeTimer(function () { activeSw.slideNext(200); }, sliderDelay);
                    }
                } else {
                    timeOutId = new customPauseResumeTimer(function () { mainSlider.slideNext(200); }, sliderDelay);
                }
            }
        }
    }

    function slidersDestroyOnEsc(e) {
        if (e.keyCode == 27 && mainSlider != '' && mainSlider.destroyed != true) {
            slidersDestroy();
        }
    }

    function slidersDestroy() {
        storyCont?.classList.add('hidden');
        document.body.classList.remove('ofh');
        if (timeOutId != '') {
            timeOutId.cancel();
        }
        const scope = getStoryScope();

        scope.querySelectorAll('.js_nested_slider_next').forEach((item) => {
            item.removeEventListener('click', slideMainNext, false);
            item.removeEventListener('click', handleNestedNextAnalytics, true);
        });
        scope.querySelectorAll('.js_nested_slider_prev').forEach((item) => {
            item.removeEventListener('click', slideMainPrev, false);
            item.removeEventListener('click', handleNestedPrevAnalytics, true);
        });
        scope.querySelectorAll('.story-link').forEach((item) => {
            item.removeEventListener('click', handleStoryActionClick, false);
        });
        scope.querySelectorAll('.js_story_video').forEach((video) => {
            video.muted = true;
            video.pause();
            video.currentTime = 0;
            video.nextElementSibling.classList.add('muted');
        });

        scope.querySelector('.js_nested_nav_prev_first')?.classList.add('hidden');
        let lastNext = scope.querySelector('.js_nested_nav_next_last');
        if (lastNext) {
            if (lastNext.parentNode?.swiper?.slides?.length > 1) {
                lastNext.classList.remove('hidden');
            } else {
                lastNext.classList.add('hidden');
            }
        }

        if (mainSlider && mainSlider != '' && Array.isArray(mainSlider.slides)) {
            for (let i = 0; i < mainSlider.slides.length; i++) {
                const nestedSlider = mainSlider.slides[i]?.getElementsByClassName('js_story_slider_nested')?.[0]?.swiper;
                if (nestedSlider) {
                    nestedSlider.destroy();
                }
            }

            if (typeof mainSlider.destroy === 'function') {
                mainSlider.destroy();
            }
        }
    }

    return {
        init: function (args) {
            const localBannerGroupId = args.bannerGroupId;
            const localIsMobileDevice = args.isMobileDevice;
            const localStoryCont = document.getElementById(`js_story_cont_${localBannerGroupId}`);

            if (!localStoryCont) {
                return;
            }

            const localRoot = localStoryCont.parentElement || document;

            const previewSliderElement = localRoot.querySelector(`#js_story_preview_slider_${localBannerGroupId}`);
            if (previewSliderElement && !previewSliderElement.swiper) {
                new Swiper(previewSliderElement, {
                    slidesPerView: 'auto',
                    allowTouchMove: true,
                    centeredSlides: false,
                    spaceBetween: 12,
                    navigation: {
                        nextEl: localRoot.querySelector(`#js_prw_slider_next_${localBannerGroupId}`),
                        prevEl: localRoot.querySelector(`#js_prw_slider_prev_${localBannerGroupId}`),
                    },
                });
            }

            bindStoryWidgetEvents(
                localRoot,
                localStoryCont,
                localBannerGroupId,
                localIsMobileDevice
            );

            const closeButton = localStoryCont.querySelector(`#js_story_close_${localBannerGroupId}`);
            if (closeButton) {
                closeButton.addEventListener('click', function () {
                    setActiveStoryContext(localBannerGroupId, localStoryCont, localIsMobileDevice);

                    const activeStory = getActiveStorySlide();

                    pushStoryEvent('stories_close', {
                        stories_id: getStoryId(activeStory)
                    });

                    slidersDestroy();
                });
            }
        },
        destorySlider: slidersDestroy
    }
}());
