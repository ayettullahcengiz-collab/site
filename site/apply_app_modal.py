import os

# 1. Append CSS to styles.css
modal_css = """
/* ========================================================
   GRANDPASHABET FIRST VISIT APP DOWNLOAD PROMPT MODAL
   ======================================================== */
.gp-app-modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.78);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    z-index: 999999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
    box-sizing: border-box;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
}

.gp-app-modal-overlay.active {
    opacity: 1;
    visibility: visible;
}

.gp-app-modal-card {
    position: relative;
    width: 100%;
    max-width: 610px;
    background: #141704;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.14);
    box-shadow: 0 16px 50px rgba(0, 0, 0, 0.9);
    display: flex;
    align-items: center;
    justify-content: space-between;
    overflow: hidden;
    transform: scale(0.92);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.gp-app-modal-overlay.active .gp-app-modal-card {
    transform: scale(1);
}

.gp-app-modal-content {
    flex: 1 1 auto;
    padding: 26px 20px 24px 28px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    z-index: 2;
}

.gp-app-modal-close {
    background: transparent;
    border: none;
    outline: none;
    color: #ffffff;
    cursor: pointer;
    padding: 0;
    margin: 0 0 16px 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    transition: transform 0.15s ease, opacity 0.15s ease;
    opacity: 0.9;
}

.gp-app-modal-close:hover {
    opacity: 1;
    transform: scale(1.12);
}

.gp-app-modal-title {
    color: #ffffff;
    font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 18px;
    font-weight: 700;
    line-height: 1.35;
    margin: 0 0 20px 0;
    text-shadow: 0 2px 5px rgba(0,0,0,0.6);
    letter-spacing: -0.2px;
}

.gp-app-modal-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(180deg, #8ba014 0%, #687907 100%);
    color: #ffffff !important;
    font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    text-decoration: none;
    padding: 12px 34px;
    border-radius: 25px;
    border: 1px solid #9db715;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.3);
    cursor: pointer;
    transition: transform 0.15s ease, filter 0.15s ease, box-shadow 0.15s ease;
    margin-bottom: 22px;
    user-select: none;
}

.gp-app-modal-btn:hover {
    filter: brightness(1.12);
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(139, 160, 20, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.4);
}

.gp-app-modal-btn:active {
    transform: translateY(1px);
    filter: brightness(0.95);
}

.gp-app-modal-checkbox-row {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    user-select: none;
    margin: 0;
    font-family: 'Roboto', -apple-system, BlinkMacSystemFont, sans-serif;
}

.gp-app-modal-checkbox-row input[type="checkbox"] {
    display: none;
}

.gp-app-modal-checkbox-box {
    width: 19px;
    height: 19px;
    border: 2px solid #8e9089;
    border-radius: 4px;
    background: rgba(0, 0, 0, 0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.15s ease;
    flex-shrink: 0;
    box-sizing: border-box;
}

.gp-app-modal-checkbox-row:hover .gp-app-modal-checkbox-box {
    border-color: #b8bcb0;
}

.gp-app-modal-checkbox-row input[type="checkbox"]:checked + .gp-app-modal-checkbox-box {
    background: #7d910f;
    border-color: #8fa612;
}

.gp-app-modal-checkbox-box::after {
    content: "";
    width: 5px;
    height: 9px;
    border: solid #ffffff;
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
    display: none;
    margin-bottom: 2px;
}

.gp-app-modal-checkbox-row input[type="checkbox"]:checked + .gp-app-modal-checkbox-box::after {
    display: block;
}

.gp-app-modal-checkbox-text {
    color: #e0e2d8;
    font-size: 14px;
    font-weight: 500;
}

.gp-app-modal-phone {
    flex: 0 0 190px;
    width: 190px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    align-self: stretch;
    overflow: hidden;
    position: relative;
    user-select: none;
    pointer-events: none;
}

.gp-app-modal-phone img {
    height: 100%;
    max-height: 280px;
    object-fit: contain;
    object-position: right center;
    display: block;
}

@media (max-width: 520px) {
    .gp-app-modal-card {
        max-width: 420px;
    }
    .gp-app-modal-content {
        padding: 22px 14px 20px 18px;
    }
    .gp-app-modal-title {
        font-size: 15px;
        margin-bottom: 16px;
    }
    .gp-app-modal-btn {
        padding: 10px 24px;
        font-size: 14px;
        margin-bottom: 18px;
    }
    .gp-app-modal-phone {
        flex: 0 0 120px;
        width: 120px;
    }
}

@media (max-width: 370px) {
    .gp-app-modal-phone {
        display: none;
    }
    .gp-app-modal-content {
        padding: 20px 16px;
    }
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.gp-app-modal-overlay' not in css_content:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + modal_css)
    print("styles.css updated with modal styles.")
else:
    print("Modal styles already in styles.css.")

# 2. Add Modal HTML and JS to index.html
modal_html_and_js = """
<!-- GrandPashabet App Download Prompt Modal (First Visit) -->
<div id="gp_app_modal_overlay" class="gp-app-modal-overlay" role="dialog" aria-modal="true" aria-labelledby="gp_modal_title">
    <div class="gp-app-modal-card">
        <div class="gp-app-modal-content">
            <button type="button" class="gp-app-modal-close" id="gp_modal_close_btn" aria-label="Kapat">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
            <div class="gp-app-modal-title" id="gp_modal_title">
                Anlık bildirimler ve kesintisiz giriş için<br>grandpashabet uygulamasını
            </div>
            <a href="https://shortpear.online/grandmobilapp" target="_blank" class="gp-app-modal-btn" id="gp_modal_download_btn">
                HEMEN İNDİR
            </a>
            <label class="gp-app-modal-checkbox-row" for="gp_modal_dont_show">
                <input type="checkbox" id="gp_modal_dont_show">
                <span class="gp-app-modal-checkbox-box"></span>
                <span class="gp-app-modal-checkbox-text">Bir daha gösterme</span>
            </label>
        </div>
        <div class="gp-app-modal-phone">
            <img src="images/app_modal_phone_faded.png" alt="Grandpashabet Mobil Uygulaması">
        </div>
    </div>
</div>

<script>
(function() {
    var MODAL_DISMISSED_KEY = 'gp_app_modal_dismissed';
    var SESSION_SEEN_KEY = 'gp_app_modal_seen';

    function initGrandPashaAppModal() {
        var overlay = document.getElementById('gp_app_modal_overlay');
        var closeBtn = document.getElementById('gp_modal_close_btn');
        var downloadBtn = document.getElementById('gp_modal_download_btn');
        var dontShowCheckbox = document.getElementById('gp_modal_dont_show');

        if (!overlay) return;

        var isPermanentlyDismissed = localStorage.getItem(MODAL_DISMISSED_KEY) === 'true';
        var isSessionSeen = sessionStorage.getItem(SESSION_SEEN_KEY) === 'true';

        function showModal() {
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
            
            // If user checked "Bir daha gösterme", save permanently in localStorage
            if (dontShowCheckbox && dontShowCheckbox.checked) {
                localStorage.setItem(MODAL_DISMISSED_KEY, 'true');
            }
            // Mark as seen for this browser session
            sessionStorage.setItem(SESSION_SEEN_KEY, 'true');
        }

        // Global methods to easily test or re-trigger anytime
        window.openGrandPashaAppModal = showModal;
        window.resetGrandPashaAppModal = function() {
            localStorage.removeItem(MODAL_DISMISSED_KEY);
            sessionStorage.removeItem(SESSION_SEEN_KEY);
            if (dontShowCheckbox) dontShowCheckbox.checked = false;
            showModal();
        };

        // Show on first entry if not permanently dismissed and not seen in this session
        if (!isPermanentlyDismissed && !isSessionSeen) {
            setTimeout(showModal, 700);
        }

        if (closeBtn) {
            closeBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                closeModal();
            });
        }

        if (downloadBtn) {
            downloadBtn.addEventListener('click', function() {
                // If they click download, record preference and dismiss
                setTimeout(closeModal, 400);
            });
        }

        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                closeModal();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGrandPashaAppModal);
    } else {
        initGrandPashaAppModal();
    }
})();
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

if 'gp_app_modal_overlay' not in html_content:
    pos = html_content.rfind('</body>')
    if pos != -1:
        new_html = html_content[:pos] + "\n" + modal_html_and_js + "\n" + html_content[pos:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("index.html updated with modal markup and script.")
    else:
        print("Could not find </body> in index.html")
else:
    print("Modal markup already in index.html")
