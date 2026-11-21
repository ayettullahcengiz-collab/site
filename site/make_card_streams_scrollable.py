html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Card stream ve yatay kaydirilabilir swiper seritlerini hem mobilde dokunmatik hem masaustunde mouse drag ile akici kaydirilabilir yapan CSS
scrollable_streams_css = '''
<style>
/* GrandPashaBet Ozel & Sizden Gelen Dev Kazanclar & Tum Card Stream seritlerini akici kaydirilabilir yap */
.banners_card_stream, 
[id^="js_card_stream_"] {
    overflow-x: auto !important;
    overflow-y: hidden !important;
    scroll-snap-type: x mandatory !important;
    scrollbar-width: none !important;
    -webkit-overflow-scrolling: touch !important;
    cursor: grab !important;
    padding: 0 16px 14px 16px !important;
}

.banners_card_stream::-webkit-scrollbar,
[id^="js_card_stream_"]::-webkit-scrollbar {
    display: none !important;
}

.banners_card_stream .swiper-wrapper,
[id^="js_card_stream_"] .swiper-wrapper {
    display: flex !important;
    flex-wrap: nowrap !important;
    transform: none !important;
    width: max-content !important;
    gap: 10px !important;
    transition: none !important;
}

.banners_card_stream .swiper-slide,
[id^="js_card_stream_"] .swiper-slide {
    width: 105px !important;
    min-width: 105px !important;
    max-width: 105px !important;
    height: auto !important;
    flex-shrink: 0 !important;
    scroll-snap-align: start !important;
    margin-right: 0 !important;
}

.banners_card_stream .dynamicBanners_item,
[id^="js_card_stream_"] .dynamicBanners_item {
    width: 100% !important;
    height: 155px !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    display: block !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.5) !important;
}

.banners_card_stream .dynamicBanners_img,
[id^="js_card_stream_"] .dynamicBanners_img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    border-radius: 12px !important;
    display: block !important;
}
</style>
'''

# Mouse ile tutup surukleme (Drag to scroll) scripti
drag_scroll_script = '''
<script>
(function() {
    function enableDragScroll(el) {
        if (!el) return;
        let isDown = false;
        let startX, scrollLeft;

        el.addEventListener('mousedown', function(e) {
            isDown = true;
            el.style.cursor = 'grabbing';
            startX = e.pageX - el.offsetLeft;
            scrollLeft = el.scrollLeft;
        });

        el.addEventListener('mouseleave', function() {
            isDown = false;
            el.style.cursor = 'grab';
        });

        el.addEventListener('mouseup', function() {
            isDown = false;
            el.style.cursor = 'grab';
        });

        el.addEventListener('mousemove', function(e) {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - el.offsetLeft;
            const walk = (x - startX) * 1.5;
            el.scrollLeft = scrollLeft - walk;
        });
    }

    document.querySelectorAll('.banners_card_stream, [id^="js_card_stream_"]').forEach(function(slider) {
        enableDragScroll(slider);
    });
})();
</script>
'''

if '</head>' in html:
    html = html.replace('</head>', scrollable_streams_css + '\n</head>')
    print('Card stream CSS eklendi!')

if '</body>' in html:
    html = html.replace('</body>', drag_scroll_script + '\n</body>')
    print('Drag scroll JS eklendi!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Tamamlandi!')
