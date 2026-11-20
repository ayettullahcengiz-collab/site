/**
 * jackpot_local.js
 * GrandPashabet offline jackpot display with 1-2s roll animation
 * and exact final values/logos matching the live site.
 * Pure high-res transparent master icons without any screenshot artifacts.
 */
(function () {
  'use strict';

  // Prevent skeletOn from wiping jackpot containers with skeletons
  function hookSkeletOn() {
    if (typeof window.skeletOn === 'function' && !window.skeletOn._hooked) {
      var orig = window.skeletOn;
      window.skeletOn = function (type) {
        if (type === 'jackpot') return;
        return orig.apply(this, arguments);
      };
      window.skeletOn._hooked = true;
    }
  }
  hookSkeletOn();
  setInterval(hookSkeletOn, 50);

  // Prevent index.html's SetJackpot from wiping containers with skeletons
  function neutralise() {
    window.SetJackpot = function () {};
    window.GetJackpotView = function () {};
  }
  neutralise();
  setInterval(neutralise, 50);

  /* ── Hedef Veriler ─────────────────────────────────────────────────── */
  var AMUSNET_DATA = [
    {
      name: 'club',
      iconImg: '/img/jackpot/icon_club.png',
      finalStr: '4000.25',
      targetVal: 4000.25
    },
    {
      name: 'diamond',
      iconImg: '/img/jackpot/icon_diamond.png',
      finalStr: '07211.23',
      targetVal: 7211.23
    },
    {
      name: 'heart',
      iconImg: '/img/jackpot/icon_heart.png',
      finalStr: '912020.34',
      targetVal: 912020.34
    },
    {
      name: 'spade',
      iconImg: '/img/jackpot/icon_spade.png',
      finalStr: '22462083.86',
      targetVal: 22462083.86
    }
  ];

  var SPORT_DATA = [
    {
      tier: 'MEGA',
      minBet: '1 000',
      finalStr: 'TRY 1 442 158.15',
      targetVal: 1442158.15,
      gemImg: '/img/jackpot/gem_mega.png',
      glowClass: 'sport_card_mega'
    },
    {
      tier: 'MAJOR',
      minBet: '500',
      finalStr: 'TRY 25 697.11',
      targetVal: 25697.11,
      gemImg: '/img/jackpot/gem_major.png',
      glowClass: 'sport_card_major'
    },
    {
      tier: 'MINOR',
      minBet: '50',
      finalStr: 'TRY 2 312.48',
      targetVal: 2312.48,
      gemImg: '/img/jackpot/gem_minor.png',
      glowClass: 'sport_card_minor'
    },
    {
      tier: 'MINI',
      minBet: '1',
      finalStr: 'TRY 750.26',
      targetVal: 750.26,
      gemImg: '/img/jackpot/gem_mini.png',
      glowClass: 'sport_card_mini'
    }
  ];

  /* ── Sayı Formatlayıcı ──────────────────────────────────────────────── */
  function formatSport(num) {
    var parts = num.toFixed(2).split('.');
    var intPart = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    return 'TRY ' + intPart + '.' + parts[1];
  }

  function formatAmusnet(num, keepZero) {
    var parts = num.toFixed(2).split('.');
    var intPart = parts[0];
    if (keepZero && intPart.length === 4) {
      intPart = '0' + intPart;
    }
    return intPart + '.' + parts[1];
  }

  /* ── 1.8 Saniyelik Rolling Animasyonu ───────────────────────────────── */
  function runRollingAnimation() {
    var duration = 1800; // 1.8 saniye oynayacak
    var startTime = null;

    var amusnetEls = document.querySelectorAll('.js_amusnet_val');
    var sportEls   = document.querySelectorAll('.js_sport_val');

    function animate(now) {
      if (!startTime) startTime = now;
      var elapsed = now - startTime;
      var progress = Math.min(elapsed / duration, 1);

      // Deceleration (ease-out cubic)
      var ease = 1 - Math.pow(1 - progress, 3);

      if (progress < 1) {
        amusnetEls.forEach(function (el, idx) {
          var item = AMUSNET_DATA[idx];
          var jitter = (Math.random() - 0.5) * (1 - progress) * (item.targetVal * 0.08);
          var current = (item.targetVal * 0.75) + (item.targetVal * 0.25 * ease) + jitter;
          if (current < 0) current = 0;
          el.textContent = formatAmusnet(current, idx === 1);
        });

        sportEls.forEach(function (el, idx) {
          var item = SPORT_DATA[idx];
          var jitter = (Math.random() - 0.5) * (1 - progress) * (item.targetVal * 0.08);
          var current = (item.targetVal * 0.75) + (item.targetVal * 0.25 * ease) + jitter;
          if (current < 0) current = 0;
          el.textContent = formatSport(current);
        });

        requestAnimationFrame(animate);
      } else {
        // Tam 1.8 saniye doldu -> SON DURUŞ
        amusnetEls.forEach(function (el, idx) {
          el.textContent = AMUSNET_DATA[idx].finalStr;
        });
        sportEls.forEach(function (el, idx) {
          el.textContent = SPORT_DATA[idx].finalStr;
        });
      }
    }

    requestAnimationFrame(animate);
  }

  /* ── Amusnet HTML Kurulumu ─────────────────────────────────────────── */
  function renderAmusnet() {
    var cont = document.getElementById('jackpot_container_8');
    if (!cont) return;

    var html = [
      '<div class="amusnet_jackpots_grid w-100" id="js_jacpot_cont_AmusnetJackpot_8">',
      AMUSNET_DATA.map(function (item) {
        return [
          '<div class="amusnet_jackpot_card">',
          '  <div class="amusnet_icon_wrap">',
          '    <img class="amusnet_card_icon" src="' + item.iconImg + '" alt="' + item.name + '" />',
          '  </div>',
          '  <div class="amusnet_content_wrap">',
          '    <div class="amusnet_val_row">',
          '      <span class="amusnet_card_value js_amusnet_val">0.00</span>',
          '      <span class="amusnet_crns">TRY</span>',
          '    </div>',
          '  </div>',
          '</div>'
        ].join('\n');
      }).join('\n'),
      '</div>'
    ].join('\n');

    cont.innerHTML = html;
  }

  /* ── Spor Jackpot HTML Kurulumu ────────────────────────────────────── */
  function renderSport() {
    var cont = document.getElementById('jackpot_container_93');
    if (!cont) return;

    var html = [
      '<div class="sport_jackpots_grid w-100" id="js_jacpot_cont_SportJackpot_93">',
      SPORT_DATA.map(function (item) {
        return [
          '<div class="sport_jackpot_card ' + item.glowClass + '">',
          '  <div class="sport_card_left">',
          '    <div class="sport_card_header">',
          '      <strong class="sport_tier_title">' + item.tier + '</strong>',
          '      <span class="sport_dot">&#8226;</span>',
          '      <span class="sport_min_bet_txt">Minimum Bahis TRY ' + item.minBet + '</span>',
          '    </div>',
          '    <div class="sport_card_value js_sport_val">TRY 0.00</div>',
          '  </div>',
          '  <div class="sport_card_right">',
          '    <img class="sport_gem_img" src="' + item.gemImg + '" alt="' + item.tier + '" />',
          '  </div>',
          '</div>'
        ].join('\n');
      }).join('\n'),
      '</div>'
    ].join('\n');

    cont.innerHTML = html;
  }

  /* ── Özel CSS Stilleri ─────────────────────────────────────────────── */
  function injectStyles() {
    var existing = document.getElementById('jackpot_custom_styles');
    if (existing) existing.remove();

    var style = document.createElement('style');
    style.id = 'jackpot_custom_styles';
    style.textContent = [
      /* Amusnet 4-Kolon Grid */
      '.amusnet_jackpots_grid {',
      '  display: grid;',
      '  grid-template-columns: repeat(4, 1fr);',
      '  gap: 12px;',
      '  width: 100%;',
      '  box-sizing: border-box;',
      '}',
      '@media (max-width: 900px) {',
      '  .amusnet_jackpots_grid { grid-template-columns: repeat(2, 1fr); }',
      '}',
      '@media (max-width: 500px) {',
      '  .amusnet_jackpots_grid { grid-template-columns: 1fr; }',
      '}',

      /* Amusnet Kartları */
      '.amusnet_jackpot_card {',
      '  display: flex;',
      '  align-items: center;',
      '  padding: 10px 16px;',
      '  border-radius: 16px;',
      '  min-height: 82px;',
      '  background: linear-gradient(180deg, #182206 0%, #101804 100%);',
      '  border: 1px solid #233108;',
      '  box-sizing: border-box;',
      '  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);',
      '  cursor: pointer;',
      '  transition: transform 0.2s ease, box-shadow 0.2s ease;',
      '}',
      '.amusnet_jackpot_card:hover {',
      '  transform: translateY(-2px);',
      '  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.5);',
      '}',
      '.amusnet_icon_wrap {',
      '  display: flex;',
      '  align-items: center;',
      '  justify-content: center;',
      '  margin-right: 12px;',
      '  flex-shrink: 0;',
      '}',
      '.amusnet_card_icon {',
      '  width: 58px;',
      '  height: 58px;',
      '  object-fit: contain;',
      '  filter: drop-shadow(0 3px 6px rgba(0,0,0,0.45));',
      '}',
      '.amusnet_content_wrap {',
      '  display: flex;',
      '  flex-direction: column;',
      '  justify-content: center;',
      '}',
      '.amusnet_val_row {',
      '  display: flex;',
      '  align-items: center;',
      '}',
      '.amusnet_card_value {',
      '  font-size: 20px;',
      '  font-weight: 700;',
      '  color: #ddc170;',
      '  letter-spacing: -0.2px;',
      '  margin-right: 6px;',
      '}',
      '.amusnet_crns {',
      '  font-size: 20px;',
      '  font-weight: 700;',
      '  color: #ddc170;',
      '}',

      /* Spor Jackpot 4-Kolon Grid */
      '.sport_jackpots_grid {',
      '  display: grid;',
      '  grid-template-columns: repeat(4, 1fr);',
      '  gap: 12px;',
      '  width: 100%;',
      '  box-sizing: border-box;',
      '}',
      '@media (max-width: 900px) {',
      '  .sport_jackpots_grid { grid-template-columns: repeat(2, 1fr); }',
      '}',
      '@media (max-width: 500px) {',
      '  .sport_jackpots_grid { grid-template-columns: 1fr; }',
      '}',

      /* Spor Jackpot Kartı */
      '.sport_jackpot_card {',
      '  position: relative;',
      '  display: flex;',
      '  justify-content: space-between;',
      '  align-items: center;',
      '  padding: 12px 16px;',
      '  border-radius: 14px;',
      '  min-height: 82px;',
      '  background-color: #121811;',
      '  border: 1px solid #232c1b;',
      '  box-sizing: border-box;',
      '  overflow: hidden;',
      '  cursor: pointer;',
      '  transition: transform 0.2s ease, border-color 0.2s ease;',
      '}',
      '.sport_jackpot_card:hover {',
      '  transform: translateY(-2px);',
      '}',

      /* Renk Haresi / Gradient & Glow */
      '.sport_card_mega {',
      '  background: linear-gradient(90deg, #131b14 0%, #131b14 55%, rgba(0, 185, 245, 0.26) 100%) !important;',
      '  border-color: rgba(0, 185, 245, 0.35) !important;',
      '}',
      '.sport_card_major {',
      '  background: linear-gradient(90deg, #131b14 0%, #131b14 55%, rgba(240, 45, 45, 0.26) 100%) !important;',
      '  border-color: rgba(240, 45, 45, 0.35) !important;',
      '}',
      '.sport_card_minor {',
      '  background: linear-gradient(90deg, #131b14 0%, #131b14 55%, rgba(185, 215, 235, 0.26) 100%) !important;',
      '  border-color: rgba(185, 215, 235, 0.35) !important;',
      '}',
      '.sport_card_mini {',
      '  background: linear-gradient(90deg, #131b14 0%, #131b14 55%, rgba(245, 175, 20, 0.26) 100%) !important;',
      '  border-color: rgba(245, 175, 20, 0.35) !important;',
      '}',

      /* Kristaller için Özel Işıltı (Glow) */
      '.sport_card_mega .sport_gem_img { filter: drop-shadow(0 0 12px rgba(0, 195, 255, 0.65)); }',
      '.sport_card_major .sport_gem_img { filter: drop-shadow(0 0 12px rgba(255, 45, 45, 0.65)); }',
      '.sport_card_minor .sport_gem_img { filter: drop-shadow(0 0 12px rgba(220, 240, 255, 0.65)); }',
      '.sport_card_mini .sport_gem_img { filter: drop-shadow(0 0 12px rgba(255, 200, 30, 0.65)); }',

      /* Spor Kart Sol Kısım (Yazılar) */
      '.sport_card_left {',
      '  display: flex;',
      '  flex-direction: column;',
      '  justify-content: center;',
      '  z-index: 2;',
      '}',
      '.sport_card_header {',
      '  display: flex;',
      '  align-items: center;',
      '  font-size: 11px;',
      '  line-height: 1.4;',
      '  color: #a4a99e;',
      '  margin-bottom: 5px;',
      '}',
      '.sport_tier_title {',
      '  font-weight: 700;',
      '  color: #ffffff;',
      '  letter-spacing: 0.3px;',
      '}',
      '.sport_dot {',
      '  margin: 0 4px;',
      '  color: #7d8477;',
      '}',
      '.sport_min_bet_txt {',
      '  font-weight: 500;',
      '  color: #a4a99e;',
      '}',
      '.sport_card_value {',
      '  font-size: 19px;',
      '  font-weight: 700;',
      '  color: #ffffff;',
      '  letter-spacing: -0.2px;',
      '}',

      /* Spor Kart Sağ Kısım (Kristal Logo) */
      '.sport_card_right {',
      '  display: flex;',
      '  align-items: center;',
      '  justify-content: center;',
      '  z-index: 2;',
      '}',
      '.sport_gem_img {',
      '  height: 56px;',
      '  width: auto;',
      '  max-width: 48px;',
      '  object-fit: contain;',
      '}',
      '#turnstile-frame, iframe[src*="Tloader"], iframe[src*="grndspr2"] {',
      '  display: none !important;',
      '  visibility: hidden !important;',
      '  pointer-events: none !important;',
      '}'
    ].join('\n');
    document.head.appendChild(style);
  }

  /* ── Başlatıcı ──────────────────────────────────────────────────────── */
  var initialised = false;
  function init() {
    injectStyles();
    renderAmusnet();
    renderSport();
    if (!initialised) {
      initialised = true;
      runRollingAnimation();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      setTimeout(init, 20);
    });
  } else {
    setTimeout(init, 20);
  }

  // Güvenlik: Herhangi bir skeleton kalırsa veya sonradan eklenirse temizle
  var checkCount = 0;
  var checkInterval = setInterval(function () {
    checkCount++;
    var hasSkeleton = document.querySelector('.skeleton-jackpot__container, .skeleton-jackpot__body');
    if (hasSkeleton) {
      renderAmusnet();
      renderSport();
    }
    if (checkCount > 50) {
      clearInterval(checkInterval);
    }
  }, 100);

})();
