# irvingguerra.github.io

Sitio público de Irving en GitHub Pages (se publica solo al hacer push a `main`).

- `index.html` — desde el 2026-11-12: **portafolio profesional** de Irving (Software Engineer), en
  **inglés por defecto con botón a español** (textos ES en el objeto `ES` del script; `?lang=es` también sirve).
  Diseño "Store Shelf" hecho con la skill **impeccable**: estante con los íconos reales, fichas de FTN (HealthyVita,
  empleado), Nuntius (MDreieck), Kabandu y Krispis (freelance) con enlaces a tiendas y "lo que hay detrás", sección de
  IA, productos propios (LiteDash, Duo Arena, Derrapazo, Get My Currency), experiencia, formación y contacto.
  Íconos en `img/apps/*.webp` (los de FTN, Kabandu y Nuntius bajados de App Store), fuente Geist local en `fonts/`,
  `img/og.png` para compartir. Irving autorizó nombrar a las 4 empresas; **sin cifras del negocio, sin capturas
  internas, sin el chatbot de FTN y sin Benevo**. Teléfono NO público.
- `cv/build.py` — genera `cv.pdf` (inglés) y `cv-es.pdf` con Chrome headless desde `cv/cv-en.html` y `cv/cv-es.html`.
  El contenido del CV vive en `build.py`: si cambia la experiencia, cambiar ahí y en `index.html` (los dos idiomas).
- `PRODUCT.md`, `DESIGN.md` y `.impeccable/` son de impeccable y están en `.git/info/exclude` (no se suben).
- `duoarena/index.html` — desde el 2026-09-26 solo **redirige a
  https://duoarena.com.mx/** (la página oficial, el perfil web y el juego en
  `/jugar/` viven en el repo `duo-arena`, carpeta `sitio/web/`). Se deja para
  los enlaces viejos; `duoarena/img/` se queda por enlaces viejos.
- `duoarena/privacidad.html`, `getmycurrency/privacidad.html`,
  `derrapazo/privacidad.html` — políticas de privacidad. **No mover estas URLs**: Play Console las tiene registradas. Las tres
  políticas (más la de LiteDash en litedash.dev) se enlazan en el pie.
  La de Duo Arena sale de `duo-arena/sitio/privacidad.html`: cambiarlas juntas.

Reglas: la plática y este archivo en español (el portafolio va bilingüe); Higuera Blanca está en Nayarit (no mencionar de dónde viene el
nombre del pueblo); nada de nombres de prueba visibles si se puede evitar.
Probar local con `python3 -m http.server` y revisar a 390 px de ancho (sin
scroll horizontal) antes de hacer push.
