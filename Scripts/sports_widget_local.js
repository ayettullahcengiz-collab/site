/**
 * Offline / Local Sports Landing Widgets (Popüler Canlı Maçlar & Popüler Maç Öncesi)
 * Grandpashabet Clone
 */

(function () {
    // SVGs for Sports Icons
    const ICONS = {
        soccer: `<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="12,7 15,10 14,14 10,14 9,10" fill="currentColor"/><line x1="12" y1="2" x2="12" y2="7" stroke="currentColor" stroke-width="1.5"/><line x1="2" y1="12" x2="9" y2="10" stroke="currentColor" stroke-width="1.5"/><line x1="22" y1="12" x2="15" y2="10" stroke="currentColor" stroke-width="1.5"/><line x1="6" y1="20" x2="10" y2="14" stroke="currentColor" stroke-width="1.5"/><line x1="18" y1="20" x2="14" y2="14" stroke="currentColor" stroke-width="1.5"/></svg>`,
        basketball: `<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><line x1="2" y1="12" x2="22" y2="12" stroke="currentColor" stroke-width="1.8"/><line x1="12" y1="2" x2="12" y2="22" stroke="currentColor" stroke-width="1.8"/><path d="M4.93 4.93a10 10 0 0 1 0 14.14" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M19.07 4.93a10 10 0 0 0 0 14.14" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>`,
        tennis: `<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2.5 8.5C6.5 8.5 9 5.5 9 2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M21.5 15.5C17.5 15.5 15 18.5 15 21.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>`,
        volleyball: `<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 12a10 10 0 0 0-7.07-2.93" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 12a10 10 0 0 0 2.93 7.07" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 12a10 10 0 0 0 4.14-7.07" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>`,
        rugby: `<svg viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="10" ry="6" transform="rotate(-45 12 12)" fill="none" stroke="currentColor" stroke-width="2"/><line x1="6.3" y1="6.3" x2="17.7" y2="17.7" stroke="currentColor" stroke-width="1.8"/><line x1="9" y1="12" x2="12" y2="9" stroke="currentColor" stroke-width="1.5"/><line x1="12" y1="15" x2="15" y2="12" stroke="currentColor" stroke-width="1.5"/></svg>`,
        star: `<svg viewBox="0 0 24 24"><polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26" fill="none" stroke="currentColor" stroke-width="2"/></svg>`,
        starFilled: `<svg viewBox="0 0 24 24"><polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26" fill="currentColor"/></svg>`,
        stream: `<svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10,8 15,10.5 10,13" fill="currentColor"/><line x1="7" y1="20" x2="17" y2="20" stroke="currentColor" stroke-width="2"/><line x1="12" y1="17" x2="12" y2="20" stroke="currentColor" stroke-width="2"/></svg>`,
        arrowLeft: `<svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`,
        arrowRight: `<svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`
    };

    // Flag SVG Helpers
    const FLAGS = {
        brazil: `<svg class="cw_flag_icon" viewBox="0 0 20 14"><rect width="20" height="14" fill="#009b3a"/><polygon points="10,1 18,7 10,13 2,7" fill="#fedf00"/><circle cx="10" cy="7" r="3.2" fill="#002776"/></svg>`,
        germany: `<svg class="cw_flag_icon" viewBox="0 0 20 14"><rect width="20" height="4.6" y="0" fill="#000"/><rect width="20" height="4.6" y="4.6" fill="#dd0000"/><rect width="20" height="4.8" y="9.2" fill="#ffce00"/></svg>`,
        europe: `<svg class="cw_flag_icon" viewBox="0 0 20 14"><rect width="20" height="14" fill="#003399"/><circle cx="10" cy="7" r="4" fill="none" stroke="#ffcc00" stroke-width="1.5" stroke-dasharray="1 1"/></svg>`,
        spain: `<svg class="cw_flag_icon" viewBox="0 0 20 14"><rect width="20" height="3.5" y="0" fill="#aa151b"/><rect width="20" height="7" y="3.5" fill="#f1bf00"/><rect width="20" height="3.5" y="10.5" fill="#aa151b"/></svg>`,
        turkey: `<svg class="cw_flag_icon" viewBox="0 0 20 14"><rect width="20" height="14" fill="#e30a17"/><circle cx="8" cy="7" r="3.5" fill="#fff"/><circle cx="9" cy="7" r="2.8" fill="#e30a17"/><polygon points="11.5,7 13.5,6.3 12.3,7.9 12.3,6.1 13.5,7.7" fill="#fff"/></svg>`,
        usa: `<svg class="cw_flag_icon" viewBox="0 0 20 14"><rect width="20" height="14" fill="#bd3d44"/><rect width="20" height="1.8" y="2" fill="#fff"/><rect width="20" height="1.8" y="6" fill="#fff"/><rect width="20" height="1.8" y="10" fill="#fff"/><rect width="9" height="7" fill="#192f5d"/></svg>`,
        uk: `<svg class="cw_flag_icon" viewBox="0 0 20 14"><rect width="20" height="14" fill="#012169"/><path d="M0,0 L20,14 M20,0 L0,14" stroke="#fff" stroke-width="2.5"/><path d="M0,0 L20,14 M20,0 L0,14" stroke="#c8102e" stroke-width="1.2"/><path d="M10,0 V14 M0,7 H20" stroke="#fff" stroke-width="4"/><path d="M10,0 V14 M0,7 H20" stroke="#c8102e" stroke-width="2.5"/></svg>`
    };

    // Generic Circular Team Crest generator
    function teamCrest(abbr, color1, color2) {
        return `<svg class="cw_team_logo" viewBox="0 0 32 32">
            <circle cx="16" cy="16" r="15" fill="${color1}" stroke="${color2}" stroke-width="2"/>
            <text x="16" y="20" font-size="11" font-weight="bold" fill="${color2}" text-anchor="middle" font-family="sans-serif">${abbr}</text>
        </svg>`;
    }

    // Matches Database
    const SPORTS_DATA = {
        soccer: {
            title: 'Futbol',
            icon: ICONS.soccer,
            live: [
                {
                    id: 'live_soc_1',
                    league: 'Brezilya. Serie A',
                    flag: FLAGS.brazil,
                    status: "2. Yarı 61'",
                    hasStream: true,
                    team1: 'Coritiba',
                    score1: '0',
                    team2: 'Santos',
                    score2: '0',
                    moreCount: '+267',
                    odds: [
                        { lbl: '1', val: '4.4' },
                        { lbl: 'X', val: '2.14' },
                        { lbl: '2', val: '2.76' }
                    ]
                },
                {
                    id: 'live_soc_2',
                    league: 'Brezilya. Serie A',
                    flag: FLAGS.brazil,
                    status: 'İlk Yarı',
                    hasStream: true,
                    team1: 'Remo',
                    score1: '2',
                    team2: 'Chapecoense',
                    score2: '0',
                    moreCount: '+297',
                    odds: [
                        { lbl: '1', val: '1.04' },
                        { lbl: 'X', val: '15' },
                        { lbl: '2', val: '41' }
                    ]
                },
                {
                    id: 'live_soc_3',
                    league: 'Brezilya. Serie A',
                    flag: FLAGS.brazil,
                    status: "1. Yarı 28'",
                    hasStream: true,
                    team1: 'Cruzeiro',
                    score1: '0',
                    team2: 'Palmeiras',
                    score2: '0',
                    moreCount: '+433',
                    odds: [
                        { lbl: '1', val: '2.38' },
                        { lbl: 'X', val: '3.05' },
                        { lbl: '2', val: '3.25' }
                    ]
                },
                {
                    id: 'live_soc_4',
                    league: 'İngiltere. Premier Lig',
                    flag: FLAGS.uk,
                    status: "2. Yarı 75'",
                    hasStream: true,
                    team1: 'Arsenal',
                    score1: '2',
                    team2: 'Chelsea',
                    score2: '1',
                    moreCount: '+312',
                    odds: [
                        { lbl: '1', val: '1.25' },
                        { lbl: 'X', val: '5.20' },
                        { lbl: '2', val: '11.0' }
                    ]
                }
            ],
            prematch: [
                {
                    id: 'pre_soc_1',
                    league: 'Kadınlar. UEFA Şampiyonlar Ligi',
                    flag: FLAGS.europe,
                    time: '19.11 20:45',
                    team1: 'FK Austria Vienna(K)',
                    logo1: teamCrest('FAV', '#4b2e83', '#ffffff'),
                    team2: 'Bayern Münih(K)',
                    logo2: teamCrest('FCB', '#dc052d', '#0066b2'),
                    odds1: [
                        { lbl: '1', val: '20' },
                        { lbl: 'X', val: '9.5' },
                        { lbl: '2', val: '1.06' }
                    ],
                    odds2: [
                        { lbl: 'Üst (4)', val: '1.98' },
                        { lbl: 'Alt (4)', val: '1.72' }
                    ]
                },
                {
                    id: 'pre_soc_2',
                    league: 'Almanya Bundesliga 2',
                    flag: FLAGS.germany,
                    time: '20.11 20:30',
                    team1: 'Arminia Bielefeld',
                    logo1: teamCrest('DSC', '#004f9f', '#ffffff'),
                    team2: 'Magdeburg',
                    logo2: teamCrest('FCM', '#005ca9', '#ffffff'),
                    odds1: [
                        { lbl: '1', val: '2.21' },
                        { lbl: 'X', val: '3.75' },
                        { lbl: '2', val: '2.99' }
                    ],
                    odds2: [
                        { lbl: 'Üst (3)', val: '2.08' },
                        { lbl: 'Alt (3)', val: '1.72' }
                    ]
                },
                {
                    id: 'pre_soc_3',
                    league: 'Almanya Bundesliga 2',
                    flag: FLAGS.germany,
                    time: '20.11 20:30',
                    team1: 'Darmstadt 98',
                    logo1: teamCrest('D98', '#004e9e', '#ffffff'),
                    team2: 'Heidenheim',
                    logo2: teamCrest('FCH', '#e30613', '#003366'),
                    odds1: [
                        { lbl: '1', val: '3.45' },
                        { lbl: 'X', val: '4.05' },
                        { lbl: '2', val: '1.95' }
                    ],
                    odds2: [
                        { lbl: 'Üst (3)', val: '1.80' },
                        { lbl: 'Alt (3)', val: '1.95' }
                    ]
                },
                {
                    id: 'pre_soc_4',
                    league: 'Türkiye. Süper Lig',
                    flag: FLAGS.turkey,
                    time: '21.11 20:00',
                    team1: 'Galatasaray',
                    logo1: teamCrest('GS', '#a90432', '#fdb912'),
                    team2: 'Fenerbahçe',
                    logo2: teamCrest('FB', '#002d72', '#fff000'),
                    odds1: [
                        { lbl: '1', val: '2.10' },
                        { lbl: 'X', val: '3.40' },
                        { lbl: '2', val: '2.95' }
                    ],
                    odds2: [
                        { lbl: 'Üst (2.5)', val: '1.75' },
                        { lbl: 'Alt (2.5)', val: '1.95' }
                    ]
                }
            ]
        },
        basketball: {
            title: 'Basketbol',
            icon: ICONS.basketball,
            live: [
                {
                    id: 'live_bsk_1',
                    league: 'Euroleague',
                    flag: FLAGS.europe,
                    status: '3. Çeyrek 04:12',
                    hasStream: true,
                    team1: 'Anadolu Efes',
                    score1: '64',
                    team2: 'Real Madrid',
                    score2: '61',
                    moreCount: '+188',
                    odds: [
                        { lbl: '1', val: '1.78' },
                        { lbl: 'X', val: '14.0' },
                        { lbl: '2', val: '2.15' }
                    ]
                },
                {
                    id: 'live_bsk_2',
                    league: 'Euroleague',
                    flag: FLAGS.europe,
                    status: '4. Çeyrek 01:50',
                    hasStream: true,
                    team1: 'Fenerbahçe Beko',
                    score1: '79',
                    team2: 'AS Monaco',
                    score2: '76',
                    moreCount: '+142',
                    odds: [
                        { lbl: '1', val: '1.34' },
                        { lbl: 'X', val: '16.0' },
                        { lbl: '2', val: '3.40' }
                    ]
                },
                {
                    id: 'live_bsk_3',
                    league: 'ABD. NBA',
                    flag: FLAGS.usa,
                    status: '2. Çeyrek 08:30',
                    hasStream: true,
                    team1: 'LA Lakers',
                    score1: '42',
                    team2: 'Boston Celtics',
                    score2: '48',
                    moreCount: '+255',
                    odds: [
                        { lbl: '1', val: '2.45' },
                        { lbl: 'X', val: '15.0' },
                        { lbl: '2', val: '1.60' }
                    ]
                }
            ],
            prematch: [
                {
                    id: 'pre_bsk_1',
                    league: 'Euroleague',
                    flag: FLAGS.europe,
                    time: '20.11 21:00',
                    team1: 'Panathinaikos',
                    logo1: teamCrest('PAO', '#007934', '#ffffff'),
                    team2: 'Olympiacos',
                    logo2: teamCrest('OLY', '#d81e05', '#ffffff'),
                    odds1: [
                        { lbl: '1', val: '1.65' },
                        { lbl: 'X', val: '15.0' },
                        { lbl: '2', val: '2.30' }
                    ],
                    odds2: [
                        { lbl: 'Üst (162.5)', val: '1.85' },
                        { lbl: 'Alt (162.5)', val: '1.85' }
                    ]
                },
                {
                    id: 'pre_bsk_2',
                    league: 'ABD. NBA',
                    flag: FLAGS.usa,
                    time: '21.11 03:30',
                    team1: 'Golden State',
                    logo1: teamCrest('GSW', '#1d428a', '#ffc72c'),
                    team2: 'Denver Nuggets',
                    logo2: teamCrest('DEN', '#0e2240', '#fec524'),
                    odds1: [
                        { lbl: '1', val: '1.92' },
                        { lbl: 'X', val: '14.0' },
                        { lbl: '2', val: '1.92' }
                    ],
                    odds2: [
                        { lbl: 'Üst (228.5)', val: '1.90' },
                        { lbl: 'Alt (228.5)', val: '1.90' }
                    ]
                },
                {
                    id: 'pre_bsk_3',
                    league: 'Türkiye. BSL',
                    flag: FLAGS.turkey,
                    time: '21.11 18:00',
                    team1: 'Beşiktaş Emlakjet',
                    logo1: teamCrest('BJK', '#000000', '#ffffff'),
                    team2: 'Pınar Karşıyaka',
                    logo2: teamCrest('KSK', '#006633', '#cc0000'),
                    odds1: [
                        { lbl: '1', val: '1.45' },
                        { lbl: 'X', val: '16.0' },
                        { lbl: '2', val: '2.85' }
                    ],
                    odds2: [
                        { lbl: 'Üst (165.5)', val: '1.82' },
                        { lbl: 'Alt (165.5)', val: '1.88' }
                    ]
                }
            ]
        },
        tennis: {
            title: 'Tenis',
            icon: ICONS.tennis,
            live: [
                {
                    id: 'live_tns_1',
                    league: 'ATP Finals Torino',
                    flag: FLAGS.europe,
                    status: '2. Set 4 - 3',
                    hasStream: true,
                    team1: 'Novak Djokovic',
                    score1: '1',
                    team2: 'Carlos Alcaraz',
                    score2: '0',
                    moreCount: '+86',
                    odds: [
                        { lbl: '1', val: '1.42' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.80' }
                    ]
                },
                {
                    id: 'live_tns_2',
                    league: 'ATP Finals Torino',
                    flag: FLAGS.europe,
                    status: '1. Set 5 - 5',
                    hasStream: true,
                    team1: 'Jannik Sinner',
                    score1: '0',
                    team2: 'Daniil Medvedev',
                    score2: '0',
                    moreCount: '+92',
                    odds: [
                        { lbl: '1', val: '1.58' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.35' }
                    ]
                },
                {
                    id: 'live_tns_3',
                    league: 'WTA Finals',
                    flag: FLAGS.usa,
                    status: '3. Set 2 - 1',
                    hasStream: true,
                    team1: 'Aryna Sabalenka',
                    score1: '1',
                    team2: 'Iga Swiatek',
                    score2: '1',
                    moreCount: '+74',
                    odds: [
                        { lbl: '1', val: '1.85' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '1.95' }
                    ]
                }
            ],
            prematch: [
                {
                    id: 'pre_tns_1',
                    league: 'ATP Davis Cup',
                    flag: FLAGS.spain,
                    time: '20.11 16:00',
                    team1: 'Rafael Nadal',
                    logo1: teamCrest('RN', '#ea5b0c', '#ffffff'),
                    team2: 'Botic van de Zandschulp',
                    logo2: teamCrest('BVZ', '#ff6600', '#ffffff'),
                    odds1: [
                        { lbl: '1', val: '1.38' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '3.10' }
                    ],
                    odds2: [
                        { lbl: 'Üst (21.5)', val: '1.80' },
                        { lbl: 'Alt (21.5)', val: '1.92' }
                    ]
                },
                {
                    id: 'pre_tns_2',
                    league: 'ATP Davis Cup',
                    flag: FLAGS.germany,
                    time: '20.11 18:30',
                    team1: 'Alexander Zverev',
                    logo1: teamCrest('AZ', '#000000', '#ffd700'),
                    team2: 'Holger Rune',
                    logo2: teamCrest('HR', '#c60c30', '#ffffff'),
                    odds1: [
                        { lbl: '1', val: '1.55' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.45' }
                    ],
                    odds2: [
                        { lbl: 'Üst (22.5)', val: '1.85' },
                        { lbl: 'Alt (22.5)', val: '1.85' }
                    ]
                },
                {
                    id: 'pre_tns_3',
                    league: 'WTA Challenger',
                    flag: FLAGS.turkey,
                    time: '21.11 13:00',
                    team1: 'Zeynep Sönmez',
                    logo1: teamCrest('ZS', '#e30a17', '#ffffff'),
                    team2: 'Daria Snigur',
                    logo2: teamCrest('DS', '#0057b7', '#ffd700'),
                    odds1: [
                        { lbl: '1', val: '1.70' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.10' }
                    ],
                    odds2: [
                        { lbl: 'Üst (20.5)', val: '1.82' },
                        { lbl: 'Alt (20.5)', val: '1.88' }
                    ]
                }
            ]
        },
        volleyball: {
            title: 'Voleybol',
            icon: ICONS.volleyball,
            live: [
                {
                    id: 'live_vly_1',
                    league: 'Türkiye. Sultanlar Ligi',
                    flag: FLAGS.turkey,
                    status: '2. Set 22 - 20',
                    hasStream: true,
                    team1: 'VakıfBank',
                    score1: '1',
                    team2: 'Eczacıbaşı Dynavit',
                    score2: '0',
                    moreCount: '+64',
                    odds: [
                        { lbl: '1', val: '1.52' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.40' }
                    ]
                },
                {
                    id: 'live_vly_2',
                    league: 'Türkiye. Efeler Ligi',
                    flag: FLAGS.turkey,
                    status: '3. Set 18 - 15',
                    hasStream: true,
                    team1: 'Fenerbahçe Medicana',
                    score1: '1',
                    team2: 'Ziraat Bankkart',
                    score2: '1',
                    moreCount: '+58',
                    odds: [
                        { lbl: '1', val: '1.75' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.05' }
                    ]
                },
                {
                    id: 'live_vly_3',
                    league: 'İtalya. Serie A1',
                    flag: FLAGS.europe,
                    status: '1. Set 23 - 21',
                    hasStream: true,
                    team1: 'Conegliano',
                    score1: '0',
                    team2: 'Milano',
                    score2: '0',
                    moreCount: '+45',
                    odds: [
                        { lbl: '1', val: '1.35' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '3.00' }
                    ]
                }
            ],
            prematch: [
                {
                    id: 'pre_vly_1',
                    league: 'Türkiye. Sultanlar Ligi',
                    flag: FLAGS.turkey,
                    time: '21.11 17:00',
                    team1: 'Galatasaray Daikin',
                    logo1: teamCrest('GS', '#a90432', '#fdb912'),
                    team2: 'Türk Hava Yolları',
                    logo2: teamCrest('THY', '#c8102e', '#ffffff'),
                    odds1: [
                        { lbl: '1', val: '1.68' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.15' }
                    ],
                    odds2: [
                        { lbl: 'Üst (181.5)', val: '1.85' },
                        { lbl: 'Alt (181.5)', val: '1.85' }
                    ]
                },
                {
                    id: 'pre_vly_2',
                    league: 'CEV Şampiyonlar Ligi',
                    flag: FLAGS.europe,
                    time: '21.11 19:30',
                    team1: 'Trentino',
                    logo1: teamCrest('TRE', '#003366', '#ffffff'),
                    team2: 'Perugia',
                    logo2: teamCrest('PER', '#000000', '#d4af37'),
                    odds1: [
                        { lbl: '1', val: '2.00' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '1.75' }
                    ],
                    odds2: [
                        { lbl: 'Üst (184.5)', val: '1.85' },
                        { lbl: 'Alt (184.5)', val: '1.85' }
                    ]
                },
                {
                    id: 'pre_vly_3',
                    league: 'Türkiye. Efeler Ligi',
                    flag: FLAGS.turkey,
                    time: '22.11 15:00',
                    team1: 'Halkbank',
                    logo1: teamCrest('HLK', '#005baa', '#ffffff'),
                    team2: 'Arkas Spor',
                    logo2: teamCrest('ARK', '#002b49', '#00a3e0'),
                    odds1: [
                        { lbl: '1', val: '1.40' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.85' }
                    ],
                    odds2: [
                        { lbl: 'Üst (179.5)', val: '1.82' },
                        { lbl: 'Alt (179.5)', val: '1.88' }
                    ]
                }
            ]
        },
        rugby: {
            title: 'Amerikan Futbolu',
            icon: ICONS.rugby,
            live: [
                {
                    id: 'live_rug_1',
                    league: 'ABD. NFL',
                    flag: FLAGS.usa,
                    status: '2. Çeyrek 06:45',
                    hasStream: true,
                    team1: 'Kansas City Chiefs',
                    score1: '14',
                    team2: 'Buffalo Bills',
                    score2: '13',
                    moreCount: '+165',
                    odds: [
                        { lbl: '1', val: '1.80' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.05' }
                    ]
                },
                {
                    id: 'live_rug_2',
                    league: 'ABD. NFL',
                    flag: FLAGS.usa,
                    status: '3. Çeyrek 02:10',
                    hasStream: true,
                    team1: 'Philadelphia Eagles',
                    score1: '21',
                    team2: 'Dallas Cowboys',
                    score2: '10',
                    moreCount: '+140',
                    odds: [
                        { lbl: '1', val: '1.18' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '4.80' }
                    ]
                },
                {
                    id: 'live_rug_3',
                    league: 'ABD. NFL',
                    flag: FLAGS.usa,
                    status: '4. Çeyrek 05:30',
                    hasStream: true,
                    team1: 'San Francisco 49ers',
                    score1: '24',
                    team2: 'Seattle Seahawks',
                    score2: '20',
                    moreCount: '+135',
                    odds: [
                        { lbl: '1', val: '1.25' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '3.90' }
                    ]
                }
            ],
            prematch: [
                {
                    id: 'pre_rug_1',
                    league: 'ABD. NFL',
                    flag: FLAGS.usa,
                    time: '22.11 04:15',
                    team1: 'Baltimore Ravens',
                    logo1: teamCrest('BAL', '#241773', '#9e7c0c'),
                    team2: 'Pittsburgh Steelers',
                    logo2: teamCrest('PIT', '#000000', '#ffb612'),
                    odds1: [
                        { lbl: '1', val: '1.58' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.40' }
                    ],
                    odds2: [
                        { lbl: 'Üst (47.5)', val: '1.90' },
                        { lbl: 'Alt (47.5)', val: '1.90' }
                    ]
                },
                {
                    id: 'pre_rug_2',
                    league: 'ABD. NFL',
                    flag: FLAGS.usa,
                    time: '22.11 21:00',
                    team1: 'Detroit Lions',
                    logo1: teamCrest('DET', '#0076b6', '#b0b7bc'),
                    team2: 'Green Bay Packers',
                    logo2: teamCrest('GB', '#203731', '#ffb612'),
                    odds1: [
                        { lbl: '1', val: '1.65' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.28' }
                    ],
                    odds2: [
                        { lbl: 'Üst (49.5)', val: '1.85' },
                        { lbl: 'Alt (49.5)', val: '1.85' }
                    ]
                },
                {
                    id: 'pre_rug_3',
                    league: 'ABD. NFL',
                    flag: FLAGS.usa,
                    time: '23.11 00:25',
                    team1: 'Minnesota Vikings',
                    logo1: teamCrest('MIN', '#4f2683', '#ffc62f'),
                    team2: 'Chicago Bears',
                    logo2: teamCrest('CHI', '#0b162a', '#c83803'),
                    odds1: [
                        { lbl: '1', val: '1.45' },
                        { lbl: 'X', val: '-' },
                        { lbl: '2', val: '2.80' }
                    ],
                    odds2: [
                        { lbl: 'Üst (43.5)', val: '1.88' },
                        { lbl: 'Alt (43.5)', val: '1.88' }
                    ]
                }
            ]
        }
    };

    // Active state tracker
    const state = {
        liveSport: 'soccer',
        prematchSport: 'soccer',
        liveOffset: 0,
        prematchOffset: 0
    };

    // Render Filter Bar
    function renderFilterBar(type, activeSport) {
        const sports = ['soccer', 'basketball', 'tennis', 'volleyball', 'rugby'];
        let tabsHtml = '';

        sports.forEach(s => {
            const sp = SPORTS_DATA[s];
            const isActive = s === activeSport;
            if (isActive) {
                tabsHtml += `
                    <button class="cw_sport_tab active" data-type="${type}" data-sport="${s}">
                        ${sp.icon}
                        <span>${sp.title}</span>
                    </button>
                `;
            } else {
                tabsHtml += `
                    <button class="cw_sport_tab icon_only" data-type="${type}" data-sport="${s}" title="${sp.title}">
                        ${sp.icon}
                    </button>
                `;
            }
        });

        return `
            <div class="cw_sports_filter_bar">
                <div class="cw_sports_tabs">
                    ${tabsHtml}
                </div>
                <div class="cw_sports_nav_arrows">
                    <button class="cw_sports_nav_btn js_cw_prev" data-type="${type}">
                        ${ICONS.arrowLeft}
                    </button>
                    <button class="cw_sports_nav_btn js_cw_next" data-type="${type}">
                        ${ICONS.arrowRight}
                    </button>
                </div>
            </div>
        `;
    }

    // Render Live Match Cards
    function renderLiveCards(sportKey, offset) {
        const matches = SPORTS_DATA[sportKey]?.live || [];
        if (matches.length === 0) return '<div style="color:#788568;padding:20px;">Maç bulunamadı</div>';

        // Select 3 matches cyclically
        let visible = [];
        for (let i = 0; i < Math.min(3, matches.length); i++) {
            const idx = (offset + i) % matches.length;
            visible.push(matches[idx]);
        }

        let cardsHtml = '';
        visible.forEach(m => {
            let oddsHtml = '';
            m.odds.forEach(o => {
                oddsHtml += `
                    <div class="cw_odd_box js_cw_odd" data-match="${m.id}" data-odd="${o.lbl}">
                        <span class="cw_odd_lbl">${o.lbl}</span>
                        <span class="cw_odd_val">${o.val}</span>
                    </div>
                `;
            });

            cardsHtml += `
                <div class="cw_match_card" data-match-id="${m.id}">
                    <div>
                        <div class="cw_card_header">
                            <div class="cw_card_league" title="${m.league}">
                                ${m.flag}
                                <span>${m.league}</span>
                            </div>
                            <button class="cw_card_fav_btn js_cw_fav">
                                ${ICONS.star}
                            </button>
                        </div>
                        <div class="cw_card_time_row">
                            <span class="cw_live_badge">
                                <span class="cw_live_pulse"></span>
                                ${m.status}
                            </span>
                            ${m.hasStream ? `<span class="cw_stream_icon">${ICONS.stream}</span>` : ''}
                        </div>
                        <div class="cw_card_teams">
                            <div class="cw_team_row">
                                <span class="cw_team_name">${m.team1}</span>
                                <span class="cw_team_score">${m.score1}</span>
                            </div>
                            <div class="cw_team_row">
                                <span class="cw_team_name">${m.team2}</span>
                                <span class="cw_team_score">${m.score2}</span>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="cw_card_market_row">
                            <span class="cw_market_title">Maç Sonucu</span>
                            <span class="cw_more_markets">${m.moreCount}</span>
                        </div>
                        <div class="cw_card_odds_grid">
                            ${oddsHtml}
                        </div>
                        <div class="cw_card_slider_bar"></div>
                    </div>
                </div>
            `;
        });

        return `<div class="cw_sports_cards_grid">${cardsHtml}</div>`;
    }

    // Render Pre-match Match Cards
    function renderPrematchCards(sportKey, offset) {
        const matches = SPORTS_DATA[sportKey]?.prematch || [];
        if (matches.length === 0) return '<div style="color:#788568;padding:20px;">Maç bulunamadı</div>';

        let visible = [];
        for (let i = 0; i < Math.min(3, matches.length); i++) {
            const idx = (offset + i) % matches.length;
            visible.push(matches[idx]);
        }

        let cardsHtml = '';
        visible.forEach(m => {
            let odds1Html = '';
            m.odds1.forEach(o => {
                odds1Html += `
                    <div class="cw_odd_box js_cw_odd" data-match="${m.id}" data-odd="${o.lbl}">
                        <span class="cw_odd_lbl">${o.lbl}</span>
                        <span class="cw_odd_val">${o.val}</span>
                    </div>
                `;
            });

            let odds2Html = '';
            if (m.odds2 && m.odds2.length) {
                let inner = '';
                m.odds2.forEach(o => {
                    inner += `
                        <div class="cw_odd_box js_cw_odd" data-match="${m.id}" data-odd="${o.lbl}">
                            <span class="cw_odd_lbl">${o.lbl}</span>
                            <span class="cw_odd_val">${o.val}</span>
                        </div>
                    `;
                });
                odds2Html = `<div class="cw_card_odds_grid two_cols">${inner}</div>`;
            }

            cardsHtml += `
                <div class="cw_match_card" data-match-id="${m.id}">
                    <div>
                        <div class="cw_card_header">
                            <div class="cw_card_league" title="${m.league}">
                                ${m.flag}
                                <span>${m.league}</span>
                            </div>
                            <button class="cw_card_fav_btn js_cw_fav">
                                ${ICONS.star}
                            </button>
                        </div>
                        <div class="cw_card_time_row">
                            <span class="cw_prematch_time">${m.time}</span>
                        </div>
                        <div class="cw_card_teams">
                            <div class="cw_team_row">
                                <div class="cw_team_info">
                                    ${m.logo1 || ''}
                                    <span class="cw_team_name">${m.team1}</span>
                                </div>
                            </div>
                            <div class="cw_team_row">
                                <div class="cw_team_info">
                                    ${m.logo2 || ''}
                                    <span class="cw_team_name">${m.team2}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="cw_card_odds_grid">
                            ${odds1Html}
                        </div>
                        ${odds2Html}
                    </div>
                </div>
            `;
        });

        return `<div class="cw_sports_cards_grid">${cardsHtml}</div>`;
    }

    // Update Live Container
    function updateLiveWidget() {
        const cont = document.getElementById('js-sport-Live-cont');
        if (!cont) return;

        cont.innerHTML = `
            <div class="cw_sports_section">
                ${renderFilterBar('live', state.liveSport)}
                ${renderLiveCards(state.liveSport, state.liveOffset)}
            </div>
        `;
        bindEvents(cont, 'live');
    }

    // Update Prematch Container
    function updatePrematchWidget() {
        const cont = document.getElementById('js-sport-Prematch-cont');
        if (!cont) return;

        cont.innerHTML = `
            <div class="cw_sports_section">
                ${renderFilterBar('prematch', state.prematchSport)}
                ${renderPrematchCards(state.prematchSport, state.prematchOffset)}
            </div>
        `;
        bindEvents(cont, 'prematch');
    }

    // Event Binder
    function bindEvents(rootElem, type) {
        // Tab buttons
        const tabs = rootElem.querySelectorAll('.cw_sport_tab');
        tabs.forEach(btn => {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                const sport = this.getAttribute('data-sport');
                if (type === 'live') {
                    state.liveSport = sport;
                    state.liveOffset = 0;
                    updateLiveWidget();
                } else {
                    state.prematchSport = sport;
                    state.prematchOffset = 0;
                    updatePrematchWidget();
                }
            });
        });

        // Prev Arrow
        const prevBtn = rootElem.querySelector('.js_cw_prev');
        if (prevBtn) {
            prevBtn.addEventListener('click', function (e) {
                e.preventDefault();
                if (type === 'live') {
                    const listLen = SPORTS_DATA[state.liveSport]?.live?.length || 1;
                    state.liveOffset = (state.liveOffset - 1 + listLen) % listLen;
                    updateLiveWidget();
                } else {
                    const listLen = SPORTS_DATA[state.prematchSport]?.prematch?.length || 1;
                    state.prematchOffset = (state.prematchOffset - 1 + listLen) % listLen;
                    updatePrematchWidget();
                }
            });
        }

        // Next Arrow
        const nextBtn = rootElem.querySelector('.js_cw_next');
        if (nextBtn) {
            nextBtn.addEventListener('click', function (e) {
                e.preventDefault();
                if (type === 'live') {
                    const listLen = SPORTS_DATA[state.liveSport]?.live?.length || 1;
                    state.liveOffset = (state.liveOffset + 1) % listLen;
                    updateLiveWidget();
                } else {
                    const listLen = SPORTS_DATA[state.prematchSport]?.prematch?.length || 1;
                    state.prematchOffset = (state.prematchOffset + 1) % listLen;
                    updatePrematchWidget();
                }
            });
        }

        // Odds click selection
        const oddBoxes = rootElem.querySelectorAll('.js_cw_odd');
        oddBoxes.forEach(box => {
            box.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                // Toggle active state on clicked odd box
                const wasActive = this.classList.contains('active');
                // Remove active from sibling odd boxes in same grid
                const parentGrid = this.parentElement;
                if (parentGrid) {
                    parentGrid.querySelectorAll('.js_cw_odd').forEach(b => b.classList.remove('active'));
                }
                if (!wasActive) {
                    this.classList.add('active');
                }
            });
        });

        // Favorite star toggle
        const favBtns = rootElem.querySelectorAll('.js_cw_fav');
        favBtns.forEach(f => {
            f.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                this.classList.toggle('active');
                if (this.classList.contains('active')) {
                    this.innerHTML = ICONS.starFilled;
                } else {
                    this.innerHTML = ICONS.star;
                }
            });
        });
    }

    // Initialize widgets
    function initWidgets() {
        updateLiveWidget();
        updatePrematchWidget();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initWidgets);
    } else {
        initWidgets();
    }

    // Backup interval in case container was rendered later
    let attempts = 0;
    const interval = setInterval(() => {
        attempts++;
        const live = document.getElementById('js-sport-Live-cont');
        const prematch = document.getElementById('js-sport-Prematch-cont');
        if (live && !live.querySelector('.cw_sports_section')) {
            updateLiveWidget();
        }
        if (prematch && !prematch.querySelector('.cw_sports_section')) {
            updatePrematchWidget();
        }
        if (attempts > 15) {
            clearInterval(interval);
        }
    }, 400);

    // Expose helper on window if needed
    window.__sportsWidgetLocal = {
        updateLive: updateLiveWidget,
        updatePrematch: updatePrematchWidget,
        state: state
    };
})();
