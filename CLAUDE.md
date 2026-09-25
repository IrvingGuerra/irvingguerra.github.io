# irvingguerra.github.io

Sitio público de Irving en GitHub Pages (se publica solo al hacer push a `main`).

- `index.html` — página principal: Irving como developer de apps y juegos,
  proyecto destacado (hoy solo **Duo Arena**, por decisión de Irving) y contacto
  (GitHub + guerravargasirving@gmail.com, elegido por él para ser público).
- `duoarena/index.html` — página oficial de Duo Arena: presentación, botón
  "Jugar en el navegador" (https://duo-arena-irving.web.app) y "Próximamente en
  Google Play" (sigue en prueba interna), capturas en `duoarena/img/`, y la
  presentación de Isla Higuera (mundo, tipos, personajes). Sale de
  `duo-arena/sitio/isla-higuera.html` y de la biblia `duo-arena/docs/PERSONAJES.md`:
  si cambian personajes o tipos, actualizar las dos.
- `duoarena/privacidad.html`, `getmycurrency/privacidad.html` — políticas de
  privacidad. **No mover estas URLs**: Play Console las tiene registradas. Get My
  Currency no sale como proyecto, pero su política se enlaza en el pie.

Reglas: español; Higuera Blanca está en Nayarit (no mencionar de dónde viene el
nombre del pueblo); nada de nombres de prueba visibles si se puede evitar.
Probar local con `python3 -m http.server` y revisar a 390 px de ancho (sin
scroll horizontal) antes de hacer push.
