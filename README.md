# guion-video-corto · skill para Claude

Una skill de Claude para escribir guiones de video corto (Reels, Shorts, TikTok) **beat por beat**. Cada guion trae la línea hablada, el texto en pantalla y el plano, 3 hooks para A/B y el caption de cada red.

- **Enrutador por intención:** descubrimiento, autoridad, nutrición, cierre/ads y testimonio, según el nivel de conciencia del público (Schwartz).
- **26 fórmulas de gancho** en español y en inglés, cada una con su plantilla, un ejemplo, el texto en pantalla y cuándo se arruina.
- **Verificador sin dependencias** (`guion_check.py`): puntúa hooks de 0 a 100 y revisa los tiempos de cada beat.
- **Perfil de marca en blanco:** sirve para cualquier negocio, sin datos de nadie.
- Trial reels, formato voz + motion graphics y reglas para nichos regulados.

## Instalación

**Claude Code**
```bash
git clone https://github.com/mrchinocontact-star/guion-video-corto-skill.git
cp -r guion-video-corto-skill/skills/guion-video-corto ~/.claude/skills/
```

**Claude.ai / app de escritorio:** comprime la carpeta `skills/guion-video-corto` en un .zip y súbelo en *Settings → Capabilities → Skills*.

## Uso
Pídele a Claude algo como «guion para un Reel de descubrimiento sobre por qué los clientes desaparecen después de pedir precio». La primera vez te va a pedir los datos de tu marca para rellenar `perfiles/plantilla-marca.md`.

```bash
python skills/guion-video-corto/scripts/guion_check.py --hook "Perdí 40 clientes por un formulario sin respuesta."
```

## Créditos y licencia
MIT. Las fórmulas de gancho 1–26 y la lógica del verificador se basan en [instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) (MIT, © 2026 Jake Schincariol), traducidas y reescritas. Ver `LICENSE`.

---

## English
A Claude skill (in Spanish) that writes short-form video scripts beat by beat. It routes each piece by intent and awareness level, and includes 26 hook formulas (ES/EN), a dependency-free hook and beat checker, and a blank brand profile. MIT licensed. Hook formulas adapted from instagram-agent-skill (MIT).
