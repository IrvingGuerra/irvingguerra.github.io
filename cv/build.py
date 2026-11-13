#!/usr/bin/env python3
"""Genera cv/cv-en.html y cv/cv-es.html; luego Chrome los imprime a cv.pdf y cv-es.pdf.

Uso:  python3 cv/build.py
El contenido vive aquí (un solo lugar) y sale de los mismos datos que index.html.
"""
import pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

T = {
  "en": {
    "title": "Software Engineer",
    "summary": "Software Engineer with 8+ years architecting and shipping production systems end to end: mobile, web, backend, desktop and IoT. Lead engineer of the FTN app at HealthyVita and builder of live platforms for companies across Mexico. I engineer with AI agents as a disciplined part of the process (layered context, rules, MCP, subagents and production verification), with ~2,850 commits co-authored with Claude, and I build AI features into products: chatbots, operations-analysis agents and neural text-to-speech.",
    "h_exp": "Experience", "h_own": "Own products", "h_edu": "Education", "h_skills": "Skills",
    "jobs": [
      ("HealthyVita · FTN", "Software Engineer", "2024 – present",
       ["Lead engineer of the FTN subscription fitness app (Flutter, iOS & Android): 1,599 of its 1,753 commits.",
        "Full-stack across the Django REST API (Postgres) and the Angular backoffice and public web, in a team of ~15.",
        "In-app purchases plus 4 payment channels, Apple Health / Health Connect, Shorebird code push, AWS (ECS, Lambda, Terraform).",
        "Integrated AI features and modeled LLM cost per conversation to choose the right model per task."]),
      ("MDreieck · Nuntius", "Lead engineer (via Antware, independent since 2024)", "2020 – present",
       ["Early-warning platform for Mexico: seismic alert reception, CAP alerts by territory, SAME/EAS radio rebroadcast, IoT siren fleet, weather and river stations with automatic thresholds.",
        "Real-time control panel (Meteor, Vue, MongoDB, WebSockets), Flutter app with full-screen critical alerts on App Store and Google Play.",
        "Three Electron/Next.js desktop apps, Raspberry Pi (Node.js) and ESP32 (C++) firmware, neural TTS voices (Piper, Google TTS), Docker server per client.",
        "~1,290 commits."]),
      ("Kabandu", "Freelance · Founding engineer", "2025 – present",
       ["Operating system for a brow & beauty salon chain: POS and admin desktop (Electron, fingerprint check-in), bookings, gift cards, loyalty and memberships.",
        "Client and staff apps in Flutter (App Store, Google Play), TypeScript server on Fly.io, WhatsApp Business automation. ~1,200 commits."]),
      ("Krispis Breakfast n' Dinner", "Freelance · Full-stack engineer", "2023 – present",
       ["Multi-branch restaurant platform: online ordering (Next.js, Stripe), kiosk, table QR, kitchen display, POS, CRM and inventory.",
        "TypeScript server on Fly.io with Uber Direct delivery, Google Wallet, web push and WhatsApp OTP. ~1,160 commits."]),
      ("Diccu", "Freelance · Full-stack engineer", "2022 – present",
       ["Home and construction marketplace (App Store, Google Play): buy from local hardware stores and hire professionals, with maps, customer–business chat, promotions and reviews.",
        "Flutter app (Firebase, Google Maps, Shorebird), React/MUI admin panel, Fastify/TypeScript server on Fly.io."]),
      ("Antware", "Software Engineer · Embedded Systems Developer", "2020 – 2024",
       ["React Native, Meteor (MongoDB), Vue and React, real-time WebSockets, Jest, Scrum, GitHub CI.",
        "Seismic-alert systems with Raspberry Pi and Node.js, EAS-SAME desktop transmitters, compliance with Mexican seismic-alert standards."]),
      ("Carklin", "Full-stack Developer", "2021 – 2022",
       ["React Native app, REST APIs with Cloud Functions, push notifications, in-app purchases with RevenueCat."]),
      ("IPN", "Full-stack Developer", "2019 – 2020",
       ["React and Firebase, PHP and MySQL, Java (Spring Boot, Struts 2, JSF, Hibernate), React Native."]),
      ("Freelance", "10+ projects", "2018 – 2024",
       ["Bongless (restaurant group), Relpers, Neurona Wireless (real-time voice requests with Dialogflow and Google Assistant), MyBike (App Store and Google Play)."]),
    ],
    "own": "LiteDash: open-source Android car launcher + companion app (Kotlin, Compose; Google Play, litedash.dev) · LGlow: open-source ad-free home screen for rooted LG TVs (webOS) · Duo Arena: online platform fighter, 2–6 players (Flutter, Flame; duoarena.com.mx) · Derrapazo: 3D kart racer (Godot; Google Play) · Get My Currency (Google Play).",
    "edu": [("B.S. Computer Systems Engineering", "ESCOM, Instituto Politécnico Nacional", "2015 – 2020"),
            ("Digital Systems Technician", "CECyT 1, Instituto Politécnico Nacional", "2013 – 2015")],
    "skills": [("AI engineering", "Claude Code, agentic workflows, MCP, subagents, LLM cost modeling, TTS"),
               ("Mobile", "Flutter, Dart, Kotlin, Jetpack Compose, React Native, Shorebird"),
               ("Web", "TypeScript, React, Next.js, Angular, Vue, MUI"),
               ("Backend", "Node.js, Express, Python, Django, Meteor, Java Spring"),
               ("Data & cloud", "PostgreSQL, MongoDB, Firebase, AWS, Fly.io, Terraform, Docker"),
               ("Other", "Electron, Godot, Raspberry Pi, ESP32")],
    "portfolio": "Portfolio",
  },
  "es": {
    "title": "Ingeniero de software",
    "summary": "Ingeniero de software con 8+ años diseñando y lanzando sistemas en producción de punta a punta: móvil, web, backend, escritorio e IoT. Líder de la app de FTN en HealthyVita y constructor de plataformas en vivo para empresas en México. Trabajo con agentes de IA como parte disciplinada del proceso (contexto por capas, reglas, MCP, subagentes y verificación en producción), con ~2,850 commits coescritos con Claude, y construyo funciones de IA en los productos: chatbots, agentes de análisis de operaciones y voz neuronal.",
    "h_exp": "Experiencia", "h_own": "Productos propios", "h_edu": "Formación", "h_skills": "Habilidades",
    "jobs": [
      ("HealthyVita · FTN", "Ingeniero de software", "2024 – hoy",
       ["Líder de la app fitness por suscripción FTN (Flutter, iOS y Android): 1,599 de sus 1,753 commits.",
        "Full-stack en la API REST de Django (Postgres) y en el backoffice y la web pública en Angular, en un equipo de ~15.",
        "Compras in-app y 4 canales de pago, Apple Salud / Health Connect, code push con Shorebird, AWS (ECS, Lambda, Terraform).",
        "Integré funciones de IA y calculé el costo de LLM por conversación para elegir el modelo adecuado."]),
      ("MDreieck · Nuntius", "Ingeniero líder (con Antware, independiente desde 2024)", "2020 – hoy",
       ["Plataforma de alerta temprana para México: recepción de alerta sísmica, alertas CAP por territorio, retransmisión por radio SAME/EAS, flota de sirenas IoT, estaciones meteorológicas y fluviómetros con umbrales automáticos.",
        "Panel en tiempo real (Meteor, Vue, MongoDB, WebSockets) y app en Flutter con alertas críticas a pantalla completa en App Store y Google Play.",
        "Tres apps de escritorio (Electron, Next.js), firmware para Raspberry Pi (Node.js) y ESP32 (C++), voces TTS neuronales (Piper, Google TTS), servidor Docker por cliente.",
        "~1,290 commits."]),
      ("Kabandu", "Freelance · Ingeniero fundador", "2025 – hoy",
       ["Sistema de una cadena de cejas y belleza: punto de venta y admin de escritorio (Electron, check-in con huella), agenda, gift cards, puntos y membresías.",
        "Apps de clientas y del personal en Flutter (App Store, Google Play), servidor TypeScript en Fly.io, automatización con WhatsApp Business. ~1,200 commits."]),
      ("Krispis Breakfast n' Dinner", "Freelance · Ingeniero full-stack", "2023 – hoy",
       ["Plataforma para una cadena de restaurantes: pedidos en línea (Next.js, Stripe), kiosco, QR en mesa, pantalla de cocina, punto de venta, CRM e inventario.",
        "Servidor TypeScript en Fly.io con delivery de Uber Direct, Google Wallet, web push y acceso por WhatsApp. ~1,160 commits."]),
      ("Diccu", "Freelance · Ingeniero full-stack", "2022 – hoy",
       ["Marketplace de hogar y construcción (App Store, Google Play): compras en ferreterías locales y contratación de profesionales, con mapas, chat entre clientes y negocios, promociones y reseñas.",
        "App en Flutter (Firebase, Google Maps, Shorebird), panel de admin en React/MUI, servidor Fastify/TypeScript en Fly.io."]),
      ("Antware", "Ingeniero de software · Sistemas embebidos", "2020 – 2024",
       ["React Native, Meteor (MongoDB), Vue y React, tiempo real con WebSockets, Jest, Scrum, CI en GitHub.",
        "Sistemas de alerta sísmica con Raspberry Pi y Node.js, transmisores EAS-SAME de escritorio, cumplimiento de la norma mexicana de alerta sísmica."]),
      ("Carklin", "Desarrollador full-stack", "2021 – 2022",
       ["App en React Native, APIs REST con Cloud Functions, notificaciones push, compras in-app con RevenueCat."]),
      ("IPN", "Desarrollador full-stack", "2019 – 2020",
       ["React y Firebase, PHP y MySQL, Java (Spring Boot, Struts 2, JSF, Hibernate), React Native."]),
      ("Freelance", "10+ proyectos", "2018 – 2024",
       ["Bongless (grupo restaurantero), Relpers, Neurona Wireless (peticiones por voz en tiempo real con Dialogflow y Google Assistant), MyBike (App Store y Google Play)."]),
    ],
    "own": "LiteDash: launcher de código abierto para pantallas Android de auto + app compañera (Kotlin, Compose; Google Play, litedash.dev) · LGlow: open-source ad-free home screen for rooted LG TVs (webOS) · Duo Arena: juego de peleas en línea de 2 a 6 (Flutter, Flame; duoarena.com.mx) · Derrapazo: carreras de karts en 3D (Godot; Google Play) · Get My Currency (Google Play).",
    "edu": [("Ingeniería en Sistemas Computacionales", "ESCOM, Instituto Politécnico Nacional", "2015 – 2020"),
            ("Técnico en Sistemas Digitales", "CECyT 1, Instituto Politécnico Nacional", "2013 – 2015")],
    "skills": [("Ingeniería con IA", "Claude Code, flujos con agentes, MCP, subagentes, costo de LLM, TTS"),
               ("Móvil", "Flutter, Dart, Kotlin, Jetpack Compose, React Native, Shorebird"),
               ("Web", "TypeScript, React, Next.js, Angular, Vue, MUI"),
               ("Backend", "Node.js, Express, Python, Django, Meteor, Java Spring"),
               ("Datos y nube", "PostgreSQL, MongoDB, Firebase, AWS, Fly.io, Terraform, Docker"),
               ("Otros", "Electron, Godot, Raspberry Pi, ESP32")],
    "portfolio": "Portafolio",
  },
}

CSS = """
@font-face { font-family: Geist; src: url(../fonts/Geist-Variable.woff2) format("woff2"); font-weight: 100 900; }
@page { size: Letter; margin: 14mm 15mm; }
* { box-sizing: border-box; }
body { margin: 0; font: 400 9.6pt/1.42 Geist, -apple-system, Helvetica, sans-serif; color: #111; -webkit-print-color-adjust: exact; }
h1 { font-size: 22pt; letter-spacing: -.02em; margin: 0; font-weight: 650; }
.t { font-size: 11.5pt; color: #0062E0; font-weight: 600; margin-top: 1pt; }
.contact { margin-top: 5pt; color: #444; font-size: 9pt; }
.contact a { color: inherit; text-decoration: none; }
p.sum { margin: 9pt 0 0; color: #222; }
h2 { font-size: 8.6pt; text-transform: uppercase; letter-spacing: .09em; color: #555; margin: 13pt 0 5pt; padding-bottom: 3pt; border-bottom: .75pt solid #ccc; font-weight: 650; }
.job { margin-bottom: 7pt; break-inside: avoid; }
.job .row { display: flex; justify-content: space-between; gap: 12pt; }
.job b { font-weight: 650; }
.job .role { color: #444; }
.job .yr { color: #555; white-space: nowrap; font-variant-numeric: tabular-nums; }
ul { margin: 2pt 0 0; padding-left: 12pt; }
li { margin: 1pt 0; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0 18pt; }
.edu div, .sk div { margin-bottom: 3pt; }
.sk b, .edu b { font-weight: 600; }
.muted { color: #555; }
"""

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")

def build(lang):
    d = T[lang]
    jobs = "".join(
        f'<div class="job"><div class="row"><span><b>{esc(c)}</b> · <span class="role">{esc(r)}</span></span><span class="yr">{y}</span></div>'
        f'<ul>{"".join(f"<li>{esc(x)}</li>" for x in pts)}</ul></div>' for c, r, y, pts in d["jobs"])
    edu = "".join(f'<div><b>{esc(a)}</b><br><span class="muted">{esc(b)} · {c}</span></div>' for a, b, c in d["edu"])
    sk = "".join(f'<div><b>{esc(a)}:</b> {esc(b)}</div>' for a, b in d["skills"])
    html = f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>Irving Guerra CV</title><style>{CSS}</style></head><body>
<h1>Irving Cristóbal Guerra Vargas</h1>
<div class="t">{d['title']}</div>
<div class="contact">guerravargasirving@gmail.com · <a href="https://www.linkedin.com/in/irvingguerra">linkedin.com/in/irvingguerra</a> · <a href="https://github.com/IrvingGuerra">github.com/IrvingGuerra</a> · <a href="https://irvingguerra.github.io">irvingguerra.github.io</a> · {'México' if lang == 'es' else 'Mexico'}</div>
<p class="sum">{esc(d['summary'])}</p>
<h2>{d['h_exp']}</h2>{jobs}
<h2>{d['h_own']}</h2><p style="margin:0">{esc(d['own'])}</p>
<div class="grid"><div><h2>{d['h_skills']}</h2><div class="sk">{sk}</div></div><div><h2>{d['h_edu']}</h2><div class="edu">{edu}</div></div></div>
</body></html>"""
    src = ROOT / "cv" / f"cv-{lang}.html"
    src.write_text(html, encoding="utf-8")
    out = ROOT / ("cv.pdf" if lang == "en" else "cv-es.pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={out}", src.as_uri()], check=True, capture_output=True)
    print(out.name, out.stat().st_size)

for lang in T:
    build(lang)
