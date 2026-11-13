---
name: guion-video-corto
description: >
  Guiones de video corto (Reels, Shorts, TikTok) beat por beat: línea hablada, texto en pantalla y plano, con 3 hooks para A/B y caption por red. Elige el arquetipo (descubrimiento, autoridad, nutrición, cierre/ads, testimonio) según el nivel de conciencia del público. Para cualquier marca, con un perfil de marca que se rellena una vez. Incluye 26 fórmulas de gancho, un verificador de hooks y tiempos, trial reels y reels de voz + motion graphics sin cámara. Activar con "guion de video", "guion para un Reel", "script de TikTok", "necesito un hook", "video de testimonio", "video para ads", "mejorar retención", "trial reel", "reel de motion graphics".
---

# guion-video-corto
## Video corto por arquetipo y nivel de conciencia

Esta skill no escribe "un video genérico". Primero **identifica qué tipo de video necesita la pieza**, es decir, su intención y el nivel de conciencia del público. Después carga el **playbook** que corresponde y lo construye sobre un **motor de retención** común a todos. Las cifras externas se tratan como hipótesis. Lo que vale de verdad son los datos de la propia cuenta.

> **Entregable:** guion **beat por beat** (qué se dice + texto en pantalla + plano) + **caption por red** + el arquetipo y el nivel de conciencia usados. **No genera el video**: se graba o se edita aparte.

---

## 1. La columna vertebral: niveles de conciencia (Eugene Schwartz)

Esto decide **qué tan agresivo** puede ser un guion. No es una cuestión de estilo: depende de quién mira.

1. **Inconsciente:** no sabe que tiene el problema.
2. **Consciente del problema:** siente el dolor, pero no sabe que hay solución.
3. **Consciente de la solución:** sabe que existen soluciones, pero no conoce la tuya.
4. **Consciente del producto:** te conoce, pero no está convencido.
5. **El más consciente:** está listo y solo necesita la oferta.

**Regla de oro:** solo se es agresivo con quien ya está caliente (niveles 4–5). A un público frío (niveles 1–2) un cierre duro lo espanta. Por eso el video orgánico de descubrimiento no vende, y el anuncio de retargeting sí va directo a la oferta.

---

## 2. La métrica que manda

La distribución la decide la **retención temprana**, no las vistas. Mirar en este orden:
1. **Retención a los 3 s**, es decir, cuántos siguen mirando después del gancho. Es la nota del hook.
2. **Tiempo medio de visualización**, para saber si el medio del video sostiene.
3. **Envíos por alcance** (shares ÷ alcance), la señal más fuerte que se puede ganar.
4. **Alcance a no seguidores**, para saber si el video viajó.
5. **Seguidores por alcance**, para saber si el perfil convirtió la atención.

> **Sin números mágicos.** Metas como "70 % a los 3 s" circulan sin una fuente verificable: úsalas solo como hipótesis. **La referencia real es la mediana de la propia cuenta.** Un video que supera 3× esa mediana es una señal. Por debajo de 1,5× es un día normal.

**Diagnóstico que ahorra meses:**
- Un video con vistas y sin seguidores tiene un problema de **perfil**, no de hook.
- Un video sin vistas tiene un problema de **hook**.

Separa los dos casos antes de reescribir nada.

---

## 3. El enrutador

Identifica a qué arquetipo pertenece la pieza y carga su playbook. Si el usuario no lo dice, **pregúntalo** o dedúcelo del objetivo.

| Arquetipo | Nivel de conciencia | Trabajo del guion | Agresividad | CTA típico | Canal | Playbook |
|---|---|---|---|---|---|---|
| **Descubrimiento** | Inconsciente → Problema | Que te encuentren | Cero venta | Seguir / guardar | Orgánico | `playbooks/descubrimiento.md` |
| **Autoridad** | Problema → Solución | Que te crean | Suave | Seguir / comentar | Orgánico | `playbooks/autoridad.md` |
| **Nutrición** | Solución → Producto | Que te prefieran | Media | Palabra clave → DM | Orgánico + retargeting suave | `playbooks/nutricion.md` |
| **Cierre / Ads** | Producto → Más consciente | Que te elijan ya | Alta / directa | Agenda / compra / aplica | **Ads** (retargeting) | `playbooks/cierre-ads.md` |
| **Testimonio** | Consideración → Cierre | Que validen la oferta | Suave-media | Palabra clave → DM | Orgánico + ads | `playbooks/testimonio.md` |

> Cada pieza tiene **una** intención dominante. Si el usuario quiere "varios en uno", sepáralos en piezas distintas.

---

## 4. Flujo de trabajo

1. **Marca → perfil.** Si existe `perfiles/<marca>.md`, cárgalo. Si no, usa `perfiles/plantilla-marca.md` y pide en el chat el contexto mínimo. Nunca inventes datos de la marca.
2. **Arquetipo → playbook.** Usa el enrutador de la sección 3 y lee el playbook que corresponda. Ahí están la estructura, el ángulo del hook, la agresividad y el CTA.
3. **Motor común.** Lee `references/motor_hooks_retencion.md` y `references/formulas_hooks.md`. Elige **3 fórmulas distintas**, no tres versiones de la misma. Para cada una, escribe por separado la línea hablada y el texto en pantalla.
4. **Pasa el verificador.** Si hay terminal, corre `scripts/guion_check.py` (sección 8) y corrige cada alerta. Si no hay terminal, aplica las mismas reglas a mano.
5. **Construye el guion** con la estructura del playbook y el motor. Una idea por beat, con open loops encadenados.
6. **Plataforma.** Ajusta el corte según `references/plataformas.md`. No repostees el mismo corte en todas las redes.
7. **Caption + CTA** para la red pedida, con el CTA que marquen el playbook y el perfil.
8. **Léelo en voz alta.** Una línea "escrita" se nota apenas alguien la dice. Reescribe todo lo que no suene a una persona hablando.

Si el usuario solo quiere el hook, o solo la estructura, entrega esa parte.

---

## 5. Motor de retención (resumen)

Esqueleto base, que cada playbook adapta: **Hook (0–3 s) → Tensión → Beats de valor con mini-loops → Prueba → Payoff → CTA.** El detalle está en `references/motor_hooks_retencion.md`.

Reglas que valen para todas las intenciones:
- Empezar a mitad de la acción o por el payoff. Nada de "hola, en este video…".
- No poner el logo ni la marca al inicio.
- El frame 1 promete lo que el video entrega.
- Cortes o cambios cada pocos segundos, y un re-hook a la mitad si el video pasa de 30 s.
- Subtítulos siempre: el video tiene que entenderse sin sonido.
- **El texto en pantalla es un guion aparte.**
  - Máximo 6 palabras por tarjeta, y la tarjeta del hook aparece en el frame 1.
  - Respeta la zona segura en 1080×1920: nada por encima de y=230 ni por debajo de y=1440, y los 230 px de la derecha libres. Comprueba en la vista previa de cada red.
- **Cambia el plano en cada beat.** En un plano fijo de 8 s es donde la gente se va.
- **Una idea por video.** Si el guion tiene dos, son dos videos: dilo.
- **Números antes que adjetivos.** Si falta un número real, deja `{{tu número}}` y avisa. Nunca lo inventes.
- Testimonios y casos solo si son reales y hay permiso para usarlos.
- **Un idioma por pieza:** lo que se dice, el texto en pantalla y el caption van en el mismo idioma.

### Nichos regulados (salud, finanzas, legal…)
- Sin promesas de resultados ni claims que la marca no pueda probar.
- En piezas que se pautan, no aludir a atributos personales del espectador, como "¿Tienes sobrepeso?" o "¿Tienes deudas?". Habla del servicio y del resultado.
- Antes/después solo si es real, con consentimiento y permitido por la plataforma.

---

## 6. Perfiles de marca

La marca no cambia el motor: solo lo viste.
- `perfiles/plantilla-marca.md` es una plantilla en blanco. Se rellena una vez por marca y se guarda como `perfiles/<marca>.md`.
- Si no se indica para qué marca es la pieza, **pregunta antes de escribir**.
- Lo que falte (precios, plazos, garantías, cifras) se marca con `[COMPLETAR]` y se avisa al usuario.

---

## 7. Formato de entrega

```
| # | Tiempo | Qué se dice (voz) | Texto en pantalla | Visual / plano |
```

- **3 variantes de hook** arriba, para el A/B.
- **Caption por red** debajo. La primera línea corta con curiosidad, antes del «… más».
- **Etiqueta** al final: arquetipo + nivel de conciencia + plataforma.

---

## 8. Verificador (`scripts/guion_check.py`)

Está en Python 3, sin dependencias, y funciona en español y en inglés.

```bash
python scripts/guion_check.py hooks.txt                       # un hook por línea → ranking 0–100
python scripts/guion_check.py --hook "Perdí 40 clientes por un formulario sin respuesta."
python scripts/guion_check.py guion.txt --beats --objetivo 30 --ppm 160   # una línea por beat
```

Hace cinco comprobaciones del hook:
- **Duración:** se dice en 3 s o menos.
- **Concreción:** tiene números, nombres o plazos.
- **Lo que está en juego:** nombra un costo, una pérdida o un error.
- **Carga adelante:** lo importante va en las primeras palabras.
- **A quién le habla:** usa tú/you o nombra un público.

Por debajo de 50 todavía no hay hook.

Con `--beats` revisa el guion completo y marca:
- un hook de más de 3,5 s;
- beats de más de 4,5 s;
- tres beats seguidos sin nada concreto;
- falta de loop, cuando la última línea no retoma ninguna palabra del hook.

No predice vistas: detecta saludos, preámbulos, hooks vacíos y guiones largos.

**El gancho tiene 5 capas**, y el script solo mide la voz y el texto. Antes de entregar, revisa a mano que estas capas digan lo mismo y lleguen en los primeros 3 s:
1. el **texto en pantalla**;
2. lo **visual**, es decir, lo que se ve en el frame 1;
3. lo **vocal**, la primera línea hablada;
4. el **sonido**: música, efecto o un silencio intencional;
5. el **caption**, su primera línea.

Si dos capas compiten, se quita una.

**Palabras por minuto:** calíbralas con la voz real de la persona midiendo un video ya grabado (palabras ÷ minutos). Mientras no esté medido, usa 160 en español y 170 en inglés como punto de partida, y avísalo.

---

## 9. Trial reels y formato "voz + motion"

**Los trial reels** son reels que Instagram muestra primero solo a no seguidores. Son un laboratorio gratis para probar hooks.
- Cada reel puede tener su versión trial con **otro hook**, para hacer un A/B real.
- Mira la retención a 3 s, el alcance a no seguidores, los envíos y los seguidores por alcance. El que gana se publica normal o se pauta.
- Conviene un volumen que se pueda sostener, no ráfagas.

**El formato voz + motion graphics** no necesita cámara y sirve para hacer volumen:
- La voz real se graba aparte, y la animación va en After Effects u otra herramienta.
- La estructura es la del motor: hook visual con texto en el frame 1 → 4–7 beats de 2–4 s, cada uno con un cambio visual → payoff → CTA.
- Entrega además una **hoja de animación** que diga, para cada beat, el texto en pantalla, el elemento visual, el movimiento y la duración.

---

## 10. Archivos

- `playbooks/`: la estructura de cada intención. Se lee en el paso 2.
- `perfiles/`: la voz y la identidad de cada marca. Se lee en el paso 1.
- `references/motor_hooks_retencion.md`: patrones de hook, retención, subtítulos, A/B y un guion resuelto. Se lee en el paso 3.
- `references/formulas_hooks.md`: 26 fórmulas de gancho en español y en inglés. Se lee en el paso 3.
- `references/plataformas.md`: cómo adaptar el corte a Reels, Shorts y TikTok. Se lee en el paso 6.
- `scripts/guion_check.py`: el verificador local.
