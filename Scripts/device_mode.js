/**
 * device_mode.js
 * Automatically detects whether the visitor is on Mobile or Desktop/PC.
 * - Mobile: Activates responsive mobile mode, adjusts viewport to device-width,
 *   enables 2x2 jackpots, scrollable category pills, and mobile bottom bar.
 * - Desktop/PC: Activates full 1360px desktop layout with original desktop header and sidebars.
 * Seamlessly responds to orientation changes and browser window resizing.
 */
(function () {
    'use strict';

    function isMobile() {
        var ua = navigator.userAgent || navigator.vendor || window.opera || '';
        var isMobileUA = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile|mobile|CriOS/i.test(ua);
        var isSmallScreen = (window.innerWidth <= 768) || (screen.width <= 768 && window.innerWidth <= 1024);
        return isMobileUA || isSmallScreen;
    }

    function applyMode() {
        var mob = isMobile();
        var html = document.documentElement;
        var vp = document.querySelector('meta[name="viewport"]');

        if (!vp) {
            vp = document.createElement('meta');
            vp.name = 'viewport';
            document.head.appendChild(vp);
        }

        if (mob) {
            html.setAttribute('data-type', 'Mobile');
            html.classList.add('mobile-mode');
            html.classList.remove('desktop-mode');
            vp.setAttribute('content', 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no');

            // Restore all navigation items to main horizontal scroll container
            var moreContent = document.getElementById('js_dy_hdr_more_content');
            var nav = document.querySelector('.tl_header_navigation');
            var moreBtn = document.getElementById('js_dy_hdr_more');
            if (moreContent && nav) {
                Array.from(moreContent.children).forEach(function (c) {
                    c.classList.remove('bg-tert');
                    nav.appendChild(c);
                });
                if (moreBtn) moreBtn.style.display = 'none';
            }
        } else {
            html.setAttribute('data-type', 'Desktop');
            html.classList.add('desktop-mode');
            html.classList.remove('mobile-mode');
            vp.setAttribute('content', 'width=1360, initial-scale=0.5, maximum-scale=0.5, user-scalable=no, minimal-ui');

            var moreBtnPc = document.getElementById('js_dy_hdr_more');
            if (moreBtnPc) moreBtnPc.style.display = '';
            if (typeof window.__respHdrRecalc === 'function') {
                window.__respHdrRecalc();
            }
        }
    }

    // Run immediately when script executes
    applyMode();

    // Run again when DOM is ready to ensure navigation elements exist
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', applyMode);
    } else {
        applyMode();
    }

    // Dynamic resize & orientation change handler with debounce
    var resizeTimer = null;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(applyMode, 150);
    });
    window.addEventListener('orientationchange', function () {
        setTimeout(applyMode, 200);
    });

    window.toggleDeviceMode = function (forceMobile) {
        if (typeof forceMobile === 'boolean') {
            if (forceMobile) {
                document.documentElement.classList.add('mobile-mode');
                document.documentElement.setAttribute('data-type', 'Mobile');
                var vp = document.querySelector('meta[name="viewport"]');
                if (vp) vp.setAttribute('content', 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no');
            } else {
                document.documentElement.classList.remove('mobile-mode');
                document.documentElement.setAttribute('data-type', 'Desktop');
                var vp2 = document.querySelector('meta[name="viewport"]');
                if (vp2) vp2.setAttribute('content', 'width=1360, initial-scale=0.5, maximum-scale=0.5, user-scalable=no, minimal-ui');
            }
        }
    };
})();
