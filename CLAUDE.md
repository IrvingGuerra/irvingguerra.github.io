# irvingguerra.github.io

Sitio público de Irving en GitHub Pages (se publica solo al hacer push a `main`).

- `index.html` — página principal: Irving como developer de apps y juegos,
  proyecto destacado (hoy solo **Duo Arena**, por decisión de Irving; sus
  botones llevan a duoarena.com.mx, /jugar/ y /perfil/) y contacto
  (GitHub + guerravargasirving@gmail.com, elegido por él para ser público).
- `duoarena/index.html` — desde el 2026-09-26 solo **redirige a
  https://duoarena.com.mx/** (la página oficial, el perfil web y el juego en
  `/jugar/` viven en el repo `duo-arena`, carpeta `sitio/web/`). Se deja para
  los enlaces viejos; `duoarena/img/` se queda (la usa el inicio).
- `duoarena/privacidad.html`, `getmycurrency/privacidad.html` — políticas de
  privacidad. **No mover estas URLs**: Play Console las tiene registradas. Get My
  Currency no sale como proyecto, pero su política se enlaza en el pie.
  La de Duo Arena sale de `duo-arena/sitio/privacidad.html`: cambiarlas juntas.

Reglas: español; Higuera Blanca está en Nayarit (no mencionar de dónde viene el
nombre del pueblo); nada de nombres de prueba visibles si se puede evitar.
Probar local con `python3 -m http.server` y revisar a 390 px de ancho (sin
scroll horizontal) antes de hacer push.
