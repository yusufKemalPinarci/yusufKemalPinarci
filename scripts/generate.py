#!/usr/bin/env python3
"""Profil README'sindeki tüm özel SVG görselleri üretir.

Kullanım:  python3 scripts/generate.py
Çıktılar:  assets/*.svg
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "'Inter','Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','SF Mono','Fira Code',Menlo,Consolas,monospace"

BG = "#0B0A16"
BRAND = ("#A78BFA", "#F472B6", "#34D399")


def e(s: str) -> str:
    return escape(s, {'"': "&quot;"})


def write(name: str, body: str) -> None:
    (OUT / name).write_text(body.strip() + "\n", encoding="utf-8")
    print("✓", name)


def brand_gradient(gid: str, animated: bool = True) -> str:
    anim = (
        '<animateTransform attributeName="gradientTransform" type="translate" '
        'values="-1 0;1 0;-1 0" dur="10s" repeatCount="indefinite"/>'
        if animated else ""
    )
    return f"""
<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0" spreadMethod="reflect">
  <stop offset="0" stop-color="{BRAND[0]}"/>
  <stop offset=".5" stop-color="{BRAND[1]}"/>
  <stop offset="1" stop-color="{BRAND[2]}"/>
  {anim}
</linearGradient>"""


def chip(x, y, label, delay, dy=-8):
    w = round(len(label) * 7.6 + 30)
    return f"""
<g>
  <animateTransform attributeName="transform" type="translate" values="0 0;0 {dy};0 0"
    dur="5s" begin="{delay}s" repeatCount="indefinite" calcMode="spline"
    keySplines=".45 0 .55 1;.45 0 .55 1"/>
  <rect x="{x}" y="{y}" width="{w}" height="32" rx="16" fill="#17142C" stroke="#FFFFFF" stroke-opacity=".16"/>
  <text x="{x + w / 2}" y="{y + 21}" text-anchor="middle" font-family="{SANS}" font-size="13.5"
    font-weight="600" fill="#F4F4F5">{e(label)}</text>
</g>"""


# ───────────────────────────── HERO ─────────────────────────────
def hero():
    W, H = 1200, 440
    lines = [
        "Flutter ile offline-first uygulamalar yazıyorum",
        "React + Node.js + .NET ile uçtan uca ürünler",
        "Python ile bilgisayarlı görü & nesne tespiti",
    ]
    CW, X0, Y = 10.2, 92, 378
    slot, T = 5.0, 15.0
    clips, texts, cur_vals, cur_times = [], [], [], []
    for i, line in enumerate(lines):
        w = round(len(line) * CW, 1)
        s = i * slot + 0.2
        pts = [(0, 0), (s, 0), (s + 1.9, w), (s + 4.0, w), (s + 4.6, 0), (T, 0)]
        kt = ";".join(f"{t / T:.4f}" for t, _ in pts)
        vals = ";".join(str(v) for _, v in pts)
        clips.append(
            f'<clipPath id="ty{i}"><rect x="{X0}" y="{Y - 22}" width="0" height="32">'
            f'<animate attributeName="width" values="{vals}" keyTimes="{kt}" dur="{T}s" '
            f'repeatCount="indefinite"/></rect></clipPath>'
        )
        texts.append(
            f'<text clip-path="url(#ty{i})" x="{X0}" y="{Y}" textLength="{w}" lengthAdjust="spacing" '
            f'font-family="{MONO}" font-size="17" fill="#E4E4E7">{e(line)}</text>'
        )
        for t, v in pts[1:5]:
            cur_times.append(t)
            cur_vals.append(X0 + v + 2)
    cur_times = [0.0] + cur_times + [T]
    cur_vals = [X0 + 2] + cur_vals + [X0 + 2]
    ckt = ";".join(f"{t / T:.4f}" for t in cur_times)
    cvals = ";".join(f"{v:.1f}" for v in cur_vals)

    # Telefon ekranı (SeviyeBen tarzı RPG arayüzü)
    PX, PY, PW, PH = 0, 0, 236, 372
    quests = [
        ("Sabah koşusu", "+50 XP", True),
        ("45 dk kod", "+80 XP", True),
        ("20 sayfa kitap", "+40 XP", False),
    ]
    qrows = ""
    for i, (q, xp, done) in enumerate(quests):
        y = 248 + i * 36
        mark = (
            f'<circle cx="44" cy="{y + 15}" r="8" fill="#34D399"/>'
            f'<path d="M40 {y + 15} l3 3 l5 -6" stroke="#0B0A16" stroke-width="2" fill="none" stroke-linecap="round"/>'
            if done else
            f'<circle cx="44" cy="{y + 15}" r="7.5" fill="none" stroke="#A1A1AA" stroke-width="1.5">'
            f'<animate attributeName="stroke" values="#A1A1AA;#F472B6;#A1A1AA" dur="2s" repeatCount="indefinite"/></circle>'
        )
        qrows += f"""
  <rect x="26" y="{y}" width="184" height="30" rx="10" fill="#FFFFFF" fill-opacity=".06"/>
  {mark}
  <text x="60" y="{y + 19.5}" font-family="{SANS}" font-size="12" fill="#{'A1A1AA' if done else 'F4F4F5'}"
    {'text-decoration="line-through"' if done else ''}>{e(q)}</text>
  <text x="202" y="{y + 19.5}" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="#34D399">{xp}</text>"""

    phone = f"""
<g transform="translate(905 34) rotate(-5 118 186)">
  <animateTransform attributeName="transform" type="translate" additive="sum"
    values="0 0;0 -10;0 0" dur="6s" repeatCount="indefinite" calcMode="spline"
    keySplines=".45 0 .55 1;.45 0 .55 1"/>
  <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="38" fill="#08070F" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="2"/>
  <rect x="10" y="10" width="{PW - 20}" height="{PH - 20}" rx="30" fill="url(#screen)"/>
  <rect x="{PW / 2 - 36}" y="18" width="72" height="20" rx="10" fill="#08070F"/>
  <text x="26" y="66" font-family="{SANS}" font-size="15" font-weight="800" fill="#FFFFFF">SeviyeBen</text>
  <rect x="148" y="51" width="62" height="22" rx="11" fill="#F59E0B" fill-opacity=".18"/>
  <text x="179" y="66" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" fill="#FCD34D">◆ 1.240</text>
  <circle cx="118" cy="118" r="36" fill="url(#brandS)"/>
  <circle cx="118" cy="118" r="36" fill="none" stroke="#FFFFFF" stroke-opacity=".5" stroke-width="2" stroke-dasharray="8 6">
    <animateTransform attributeName="transform" type="rotate" values="0 118 118;360 118 118" dur="14s" repeatCount="indefinite"/>
  </circle>
  <text x="118" y="130" text-anchor="middle" font-size="32">⚔️</text>
  <text x="118" y="180" text-anchor="middle" font-family="{SANS}" font-size="18" font-weight="800" fill="#FFFFFF">Seviye 12</text>
  <text x="118" y="198" text-anchor="middle" font-family="{SANS}" font-size="11.5" fill="#A1A1AA">Kod Şövalyesi</text>
  <rect x="26" y="210" width="184" height="10" rx="5" fill="#FFFFFF" fill-opacity=".1"/>
  <rect x="26" y="210" width="60" height="10" rx="5" fill="url(#xp)">
    <animate attributeName="width" values="60;150;150;60" keyTimes="0;.55;.9;1" dur="6s" repeatCount="indefinite"/>
  </rect>
  <text x="26" y="236" font-family="{MONO}" font-size="10" fill="#A1A1AA">XP</text>
  <text x="210" y="236" text-anchor="end" font-family="{MONO}" font-size="10" fill="#A1A1AA">740 / 1000</text>
  {qrows}
</g>"""

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  {brand_gradient("brand")}
  {brand_gradient("brandS", animated=False)}
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0B0A16"/><stop offset="1" stop-color="#140F28"/>
  </linearGradient>
  <linearGradient id="screen" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1D1736"/><stop offset="1" stop-color="#0D0B1A"/>
  </linearGradient>
  <linearGradient id="xp" x1="0" x2="1"><stop offset="0" stop-color="#34D399"/><stop offset="1" stop-color="#22D3EE"/></linearGradient>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
  <pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse">
    <path d="M44 0H0V44" fill="none" stroke="#FFFFFF" stroke-opacity=".045"/>
  </pattern>
  <radialGradient id="fade" cx=".35" cy=".5" r=".75">
    <stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#0B0A16" stop-opacity=".9"/>
  </radialGradient>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="28"/></clipPath>
  {''.join(clips)}
</defs>

<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <circle cx="180" cy="40" r="190" fill="#7C3AED" opacity=".55" filter="url(#blur)">
    <animate attributeName="cx" values="180;360;180" dur="16s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1050" cy="420" r="210" fill="#DB2777" opacity=".38" filter="url(#blur)">
    <animate attributeName="cy" values="420;300;420" dur="13s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="-20" r="170" fill="#059669" opacity=".32" filter="url(#blur)">
    <animate attributeName="cx" values="700;560;700" dur="18s" repeatCount="indefinite"/>
  </circle>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <rect width="{W}" height="{H}" fill="url(#fade)"/>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="27" fill="none" stroke="url(#brand)" stroke-opacity=".55" stroke-width="2"/>

<!-- durum hapı -->
<rect x="64" y="52" width="372" height="32" rx="16" fill="#FFFFFF" fill-opacity=".06" stroke="#FFFFFF" stroke-opacity=".14"/>
<circle cx="84" cy="68" r="9" fill="#34D399" opacity=".3">
  <animate attributeName="r" values="4;10;4" dur="2s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values=".5;0;.5" dur="2s" repeatCount="indefinite"/>
</circle>
<circle cx="84" cy="68" r="4" fill="#34D399"/>
<text x="100" y="73" font-family="{SANS}" font-size="13.5" fill="#D4D4D8">Şu an: <tspan fill="#FFFFFF" font-weight="600">oyunlaştırılmış Flutter uygulamaları</tspan></text>

<text x="64" y="136" font-family="{SANS}" font-size="22" fill="#A1A1AA">Merhaba 👋 ben</text>
<text x="62" y="208" font-family="{SANS}" font-size="70" font-weight="800" letter-spacing="-2" fill="#FFFFFF">Yusuf Kemal</text>
<text x="62" y="282" font-family="{SANS}" font-size="70" font-weight="800" letter-spacing="-2" fill="url(#brand)">Pınarcı.</text>
<text x="64" y="324" font-family="{SANS}" font-size="19" fill="#D4D4D8"><tspan font-weight="700" fill="#FFFFFF">Full Stack &amp; Mobile Developer</tspan>  ·  fikirden ürüne, uçtan uca</text>

<!-- yazılan terminal satırı -->
<text x="64" y="{Y}" font-family="{MONO}" font-size="17" font-weight="700" fill="#34D399">❯</text>
{''.join(texts)}
<rect x="{X0}" y="{Y - 16}" width="9" height="20" rx="1" fill="#F472B6">
  <animate attributeName="x" values="{cvals}" keyTimes="{ckt}" dur="{T}s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1s" repeatCount="indefinite"/>
</rect>

{chip(752, 92, "📱 Flutter", 0)}
{chip(738, 214, "⚡ Offline-first", 1.4, 8)}
{chip(770, 330, "🎮 Oyunlaştırma", 2.6)}
{phone}
</svg>"""
    write("hero.svg", svg)


# ─────────────────────────── BÖLÜM BAŞLIĞI ───────────────────────────
def section(slug, num, title, sub):
    W, H = 1200, 96
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  {brand_gradient("g", animated=False)}
  <linearGradient id="line" x1="0" x2="1">
    <stop offset="0" stop-color="#A78BFA" stop-opacity=".9"/><stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
  </linearGradient>
</defs>
<text x="4" y="58" font-family="{MONO}" font-size="16" font-weight="700" fill="url(#g)">{num}</text>
<text x="44" y="60" font-family="{SANS}" font-size="32" font-weight="800" letter-spacing="-.5" fill="#8B5CF6">{e(title)}</text>
<text x="44" y="86" font-family="{SANS}" font-size="15" fill="#8B8B99">{e(sub)}</text>
<rect x="{round(64 + len(title) * 16.8)}" y="48" width="{round(1196 - 64 - len(title) * 16.8)}" height="2" rx="1" fill="url(#line)"/>
</svg>"""
    write(f"section-{slug}.svg", svg)


# ───────────────────────────── HAKKIMDA ─────────────────────────────
def about():
    W, H = 1200, 400
    K, C, S, P, I, F, M = "#C792EA", "#FFCB6B", "#C3E88D", "#89DDFF", "#E4E4E7", "#82AAFF", "#6B7280"

    def t(s, c):
        return f'<tspan fill="{c}">{e(s)}</tspan>'

    def lst(items):
        out = t("[", P)
        for i, it in enumerate(items):
            out += t(f'"{it}"', S) + (t(", ", P) if i < len(items) - 1 else "")
        return out + t("];", P)

    code = [
        t("// kim bu adam?", M),
        t("class ", K) + t("YusufKemal ", C) + t("extends ", K) + t("Developer ", C) + t("{", P),
        t("  final ", K) + t("rol     ", I) + t("= ", P) + t('"Full Stack & Mobile Developer"', S) + t(";", P),
        t("  final ", K) + t("mobil   ", I) + t("= ", P) + lst(["Flutter", "Dart", "Kotlin"]),
        t("  final ", K) + t("web     ", I) + t("= ", P) + lst(["React", "TypeScript", "Node.js"]),
        t("  final ", K) + t("backend ", I) + t("= ", P) + lst([".NET", "Django", "Firebase"]),
        t("  final ", K) + t("ai      ", I) + t("= ", P) + lst(["Python", "OpenCV", "YOLO"]),
        "",
        t("  String ", C) + t("felsefe", F) + t("() => ", P) + t('"Offline-first, hızlı, oyun gibi."', S) + t(";", P)
        + '<tspan fill="#F472B6">▍<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/></tspan>',
        t("}", P),
    ]
    LH, Y0, X0 = 27, 112, 92
    rows = ""
    for i, line in enumerate(code):
        y = Y0 + i * LH
        rows += f'<text x="58" y="{y}" text-anchor="end" font-family="{MONO}" font-size="14" fill="#4B4B5C">{i + 1}</text>'
        rows += f'<text x="{X0}" y="{y}" xml:space="preserve" font-family="{MONO}" font-size="15.5">{line}</text>'
    cy = Y0 + 8 * LH

    stats = [
        ("50+", "Açık kaynak repo", "GitHub'da 2020'den beri"),
        ("20+", "Mobil uygulama", "Flutter & Kotlin"),
        ("4", "Katman", "mobil · web · API · yapay zekâ"),
    ]
    tiles = ""
    for i, (n, label, sub) in enumerate(stats):
        y = 24 + i * 120
        tiles += f"""
<rect x="822" y="{y}" width="354" height="106" rx="20" fill="#0F0D1D" stroke="#FFFFFF" stroke-opacity=".1"/>
<text x="850" y="{y + 64}" font-family="{SANS}" font-size="48" font-weight="800" letter-spacing="-1" fill="url(#g)">{n}</text>
<text x="{850 + len(n) * 30 + 16}" y="{y + 50}" font-family="{SANS}" font-size="15" font-weight="600" fill="#F4F4F5">{e(label)}</text>
<text x="{850 + len(n) * 30 + 16}" y="{y + 72}" font-family="{SANS}" font-size="14" fill="#8B8B99">{e(sub)}</text>"""

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  {brand_gradient("g")}
  <filter id="sh" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000" flood-opacity=".35"/></filter>
</defs>
<g filter="url(#sh)">
  <rect x="24" y="24" width="774" height="352" rx="20" fill="#0F0D1D" stroke="#FFFFFF" stroke-opacity=".1"/>
</g>
<path d="M24 64 V44 a20 20 0 0 1 20 -20 H778 a20 20 0 0 1 20 20 V64 Z" fill="#17142B"/>
<circle cx="50" cy="44" r="6.5" fill="#FF5F57"/><circle cx="72" cy="44" r="6.5" fill="#FEBC2E"/><circle cx="94" cy="44" r="6.5" fill="#28C840"/>
<rect x="124" y="30" width="138" height="34" rx="8" fill="#0F0D1D"/>
<text x="140" y="52" font-family="{MONO}" font-size="13" fill="#E4E4E7"><tspan fill="#40C4FF">◆</tspan> yusuf.dart</text>
<text x="776" y="50" text-anchor="end" font-family="{MONO}" font-size="12" fill="#6B6B7B">Dart · UTF-8</text>
{rows}
{tiles}
</svg>"""
    write("about.svg", svg)


# ───────────────────────────── PROJE KARTLARI ─────────────────────────────
PROJECTS = [
    ("kelime-bahis", "🎲", "Kelime Bahis", "Flutter · Roguelike · Offline",
     ["Türkçe kelimelerle oynanan, her turda", "riskin büyüdüğü roguelike kelime oyunu."],
     ["Flutter", "Oyun", "Offline"], "#F59E0B", "#EF4444"),
    ("borc-ejderi", "🐉", "Borç Ejderi", "Flutter · Finans RPG",
     ["Borcu ejderhaya, birikimi kılıca çeviren", "oyunlaştırılmış bütçe uygulaması."],
     ["Flutter", "RPG", "Finans"], "#22C55E", "#0D9488"),
    ("seviye-ben", "⚔️", "SeviyeBen", "Flutter · Alışkanlık RPG",
     ["Her alışkanlık bir görev, her gün bir", "seviye: hayatını karaktere dönüştür."],
     ["Flutter", "RPG", "Offline"], "#8B5CF6", "#6366F1"),
    ("ruya", "🌙", "Rüya", "Flutter · AI · Offline",
     ["Alarm, gece defteri ve yapay zekâ", "yorumuyla tamamen offline rüya günlüğü."],
     ["Flutter", "AI", "Offline"], "#3B82F6", "#6366F1"),
    ("brewlog", "☕", "BrewLog", "Flutter · Specialty Kahve",
     ["Öğütme, oran ve süreyi kaydedip", "mükemmel fincanı bulduran dial-in günlüğü."],
     ["Flutter", "Günlük", "Offline"], "#D97706", "#B45309"),
    ("kuafor_randevu", "💈", "Kuaför Randevu", "Flutter · .NET API",
     ["Flutter mobil uygulama ve C# / .NET", "backend'iyle uçtan uca randevu sistemi."],
     ["Flutter", ".NET", "REST API"], "#EC4899", "#DB2777"),
    ("directional-object-detection", "🛰️", "Uzayda Nesne Tespiti", "Python · Computer Vision",
     ["Uydu görüntülerinde yönlü (rotated)", "kutularla nesne tespiti modeli."],
     ["Python", "Deep Learning", "CV"], "#06B6D4", "#0EA5E9"),
    ("travel_with_student_web", "✈️", "Travel with Student", "TypeScript · Web",
     ["Öğrenci seyahatlerini planlamak ve", "keşfetmek için modern web platformu."],
     ["TypeScript", "React", "Web"], "#14B8A6", "#22C55E"),
]


def card(slug, emoji, title, sub, desc, tags, a1, a2):
    W, H = 600, 230
    tag_svg, x = "", 28
    for tg in tags:
        w = round(len(tg) * 7.4 + 24)
        tag_svg += (
            f'<rect x="{x}" y="180" width="{w}" height="26" rx="13" fill="{a1}" fill-opacity=".14" '
            f'stroke="{a1}" stroke-opacity=".35"/>'
            f'<text x="{x + w / 2}" y="197.5" text-anchor="middle" font-family="{SANS}" font-size="12.5" '
            f'font-weight="600" fill="{a1}">{e(tg)}</text>'
        )
        x += w + 8
    d = "".join(
        f'<text x="28" y="{132 + i * 23}" font-family="{SANS}" font-size="15.5" fill="#D4D4D8">{e(l)}</text>'
        for i, l in enumerate(desc)
    )
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a1}"/><stop offset="1" stop-color="{a2}"/></linearGradient>
  <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{a1}" stop-opacity=".7"/><stop offset=".45" stop-color="#FFFFFF" stop-opacity=".08"/>
    <stop offset="1" stop-color="#FFFFFF" stop-opacity=".08"/>
  </linearGradient>
  <filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="45"/></filter>
  <clipPath id="c"><rect width="{W}" height="{H}" rx="22"/></clipPath>
</defs>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="#0E0C1B"/>
  <circle cx="40" cy="20" r="120" fill="{a1}" opacity=".32" filter="url(#b)">
    <animate attributeName="opacity" values=".22;.4;.22" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="600" cy="230" r="110" fill="{a2}" opacity=".16" filter="url(#b)"/>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="21" fill="none" stroke="url(#bd)" stroke-width="1.5"/>
<rect x="28" y="28" width="60" height="60" rx="16" fill="url(#a)"/>
<rect x="28" y="28" width="60" height="30" rx="16" fill="#FFFFFF" fill-opacity=".12"/>
<text x="58" y="70" text-anchor="middle" font-size="30">{emoji}</text>
<text x="106" y="56" font-family="{SANS}" font-size="23" font-weight="800" letter-spacing="-.3" fill="#FFFFFF">{e(title)}</text>
<text x="106" y="80" font-family="{SANS}" font-size="13.5" fill="#9CA3AF">{e(sub)}</text>
<circle cx="556" cy="50" r="18" fill="#FFFFFF" fill-opacity=".06" stroke="#FFFFFF" stroke-opacity=".12"/>
<path d="M550 56 L562 44 M553 44 H562 V53" stroke="#E4E4E7" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
{d}
{tag_svg}
</svg>"""
    write(f"card-{slug}.svg", svg)


# ───────────────────────────── KAPANIŞ ─────────────────────────────
def footer():
    W, H = 1200, 230
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  {brand_gradient("g")}
  <filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
  <clipPath id="c"><rect width="{W}" height="{H}" rx="28"/></clipPath>
</defs>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="#0B0A16"/>
  <circle cx="300" cy="230" r="180" fill="#7C3AED" opacity=".45" filter="url(#b)">
    <animate attributeName="cx" values="300;460;300" dur="14s" repeatCount="indefinite"/>
  </circle>
  <circle cx="900" cy="0" r="170" fill="#DB2777" opacity=".35" filter="url(#b)">
    <animate attributeName="cx" values="900;760;900" dur="12s" repeatCount="indefinite"/>
  </circle>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="27" fill="none" stroke="url(#g)" stroke-opacity=".5" stroke-width="2"/>
<text x="600" y="98" text-anchor="middle" font-family="{SANS}" font-size="44" font-weight="800" letter-spacing="-1" fill="#FFFFFF">Birlikte bir şey <tspan fill="url(#g)">inşa edelim.</tspan></text>
<text x="600" y="136" text-anchor="middle" font-family="{SANS}" font-size="17" fill="#A1A1AA">Mobil uygulama, web ürünü ya da çılgın bir fikir — hepsine açığım.</text>
<rect x="490" y="160" width="220" height="44" rx="22" fill="#FFFFFF"/>
<text x="600" y="188" text-anchor="middle" font-family="{SANS}" font-size="16" font-weight="700" fill="#0B0A16">LinkedIn'den yaz  →</text>
</svg>"""
    write("footer.svg", svg)


if __name__ == "__main__":
    hero()
    about()
    section("about", "01", "Hakkımda", "Kod yazmayı değil, ürün çıkarmayı seviyorum.")
    section("projects", "02", "Öne Çıkan Projeler", "Kartlara tıkla, repoya git.")
    section("stack", "03", "Teknolojiler", "Günlük çalıştığım araç kutusu.")
    section("activity", "04", "GitHub'daki İzim", "Her gün biraz daha.")
    for p in PROJECTS:
        card(*p)
    footer()
