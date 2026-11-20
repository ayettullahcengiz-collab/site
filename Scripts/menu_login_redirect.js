// Global redirect to login for top menu items (only when NOT logged in)
(function () {
    function redirectToLogin(e) {
        // Giriş yapılmışsa normal navigasyona izin ver
        if (sessionStorage.getItem('gp_logged_in') === '1') {
            var origHref = this.getAttribute('data-original-href');
            if (origHref && origHref !== 'javascript:void(0)' && origHref !== '#' && origHref !== '') {
                window.location.href = origHref;
            }
            return true;
        }

        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        // Login popup aç
        var loginBtn = document.querySelector('.loginDialog');
        if (loginBtn) {
            loginBtn.click();
        } else {
            window.location.href = '/login/login';
        }
        return false;
    }

    function doAttachRedirects() {
        if (sessionStorage.getItem('gp_logged_in') === '1') return;

        var menuLinks = document.querySelectorAll(
            '.tl_header_navigation a.tl_main_nav_item, ' +
            '#js_dy_hdr a, ' +
            '#js_dy_hdr_more_content a, ' +
            '.header_nav__more_content a, ' +
            '.header_nav__dropdown a, ' +
            '.js_sport_links, ' +
            '.dynamic_featured_item'
        );

        menuLinks.forEach(function (el) {
            el.addEventListener('click', redirectToLogin, true);
            el.onclick = redirectToLogin;
            el.setAttribute('data-original-href', el.getAttribute('href') || '');
            el.setAttribute('href', 'javascript:void(0)');
        });
    }

    // Çıkış sonrası tekrar bağlanabilmesi için global yap
    window.attachRedirects = doAttachRedirects;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', doAttachRedirects);
    } else {
        doAttachRedirects();
    }

    window.addEventListener('load', doAttachRedirects);
    setTimeout(doAttachRedirects, 500);
    setTimeout(doAttachRedirects, 1500);
    setTimeout(doAttachRedirects, 3000);
})();
