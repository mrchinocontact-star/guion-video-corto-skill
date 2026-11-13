#!/usr/bin/env python3
"""
guion_check.py - verificador local de hooks y guiones de video corto (ES/EN).

Qué es: cinco comprobaciones de texto que comparten los hooks que retienen
(se dice en 3 s, tiene algo concreto, hay algo en juego, lo importante va
adelante, le habla a alguien) y un control de tiempos por beat.

Qué NO es: un predictor de vistas. Detecta saludos, preámbulos, hooks vacíos
y guiones largos. Qué video viaja lo deciden la cara, la edición, el audio y
a quién se lo muestra la plataforma. La curva de retención real manda.

Inspirado en hookscore.py / beats.py de instagram-agent-skill (MIT), reescrito
para español e inglés. Sin dependencias.

Uso
  python guion_check.py hooks.txt                       # un hook por línea, ranking
  python guion_check.py --hook "Perdí 40 clientes por un formulario sin respuesta."
  python guion_check.py guion.txt --beats --objetivo 30 --ppm 150
  python guion_check.py hooks.txt --json
"""

import argparse
import json
import re
import sys
import unicodedata

WORD_RE = re.compile(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ$%'’]+(?:[.,][0-9]+)?")

SPOKEN_NUMBERS = {
    # es
    "cero", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
    "diez", "once", "doce", "quince", "veinte", "treinta", "cuarenta",
    "cincuenta", "sesenta", "setenta", "ochenta", "noventa", "cien", "ciento",
    "mil", "millón", "millones", "doble", "triple", "mitad", "docena",
    # en
    "zero", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "fifteen", "twenty", "thirty", "forty", "fifty",
    "hundred", "thousand", "million", "half", "twice", "dozen",
}
TIME_UNITS = {
    "segundo", "segundos", "minuto", "minutos", "hora", "horas", "día", "días",
    "semana", "semanas", "mes", "meses", "año", "años",
    "second", "seconds", "minute", "minutes", "hour", "hours", "day", "days",
    "week", "weeks", "month", "months", "year", "years",
}
STAKE_WORDS = {
    # es
    "perder", "pierdes", "pierde", "perdí", "perdimos", "pierden", "perdiendo",
    "costó", "cuesta", "cuestan", "costo", "error", "errores", "dinero",
    "pacientes", "paciente", "citas", "cita", "clientes", "riesgo", "nunca",
    "deja", "dejes", "mal", "peor", "fuga", "fugas", "vacía", "vacían",
    "multa", "caro", "gratis", "ganas", "gana", "ahorra", "ahorras",
    # en
    "lose", "lost", "losing", "cost", "costs", "mistake", "mistakes", "money",
    "patients", "patient", "clients", "wrong", "stop", "never", "worse",
    "risk", "leak", "leaks", "free", "save", "saves", "wasted", "waste",
}
FILLER_OPENERS = [
    "hola", "buenas", "hey", "hi", "hello", "bueno", "entonces", "hoy",
    "en este video", "en este reel", "quiero contarte", "vamos a", "les voy",
    "te voy a", "así que", "so", "today", "in this video", "let me",
    "i want to", "welcome", "what's up", "qué tal",
]
GREETINGS = ["hola", "buenas", "hey", "hi ", "hello", "qué tal", "what's up", "welcome", "bienvenid"]
AUDIENCE_WORDS = {
    "tú", "tu", "tus", "te", "ti", "usted", "ustedes", "vos", "tenés",
    "you", "your", "you're", "yours",
}
AUDIENCE_PATTERNS = [
    r"\bsi (eres|tienes|tenés|sos|manejas|diriges)\b", r"\bdueñ[oa]s? de\b",
    r"\bif you\b", r"\bowners?\b", r"\bpara (clínicas|med ?spas?|dueños)\b",
]
FIRST_PERSON = {"perdí", "perdimos", "me", "mi", "mis", "nos", "nuestro", "nuestra", "yo", "hice", "hicimos",
                "i", "i'm", "i've", "we", "my", "our", "us"}
ES_HINTS = {"de", "la", "que", "el", "en", "los", "tu", "por", "con", "para", "una", "es", "no", "lo"}
EN_HINTS = {"the", "you", "your", "to", "and", "of", "in", "is", "it", "for", "that", "this", "with"}


def norm(s):
    return unicodedata.normalize("NFC", s.strip())


def words(s):
    return WORD_RE.findall(s)


def lang_of(text):
    w = [x.lower() for x in words(text)]
    es = sum(1 for x in w if x in ES_HINTS)
    en = sum(1 for x in w if x in EN_HINTS)
    return "en" if en > es else "es"


def default_ppm(lang):
    return 170 if lang == "en" else 160


def seconds(text, ppm):
    return len(words(text)) / ppm * 60.0


def concrete_hits(text):
    w = words(text)
    low = [x.lower() for x in w]
    hits = 0
    hits += len(re.findall(r"\d", text)) and len(re.findall(r"\d+(?:[.,]\d+)?", text))
    hits += sum(1 for x in low if x in SPOKEN_NUMBERS)
    hits += sum(1 for x in low if x in TIME_UNITS)
    hits += text.count("$") + text.count("%")
    # nombres propios / marcas (mayúscula que no abre la frase)
    for i, x in enumerate(w):
        if i > 0 and x[:1].isupper() and len(x) > 2 and not w[i - 1].endswith((".", "!", "?")):
            hits += 1
    return hits


def score_hook(hook, ppm):
    h = norm(hook)
    low = h.lower()
    w = [x.lower() for x in words(h)]
    n = max(len(w), 1)
    flags = []

    # 1 duración
    secs = seconds(h, ppm)
    dur = 100 if secs <= 3.0 else max(0.0, 100 - (secs - 3.0) * 30)
    if secs > 3.5:
        flags.append(f"tarda {secs:.1f}s en decirse (ideal ≤3s)")

    # 2 concreción
    c = concrete_hits(h)
    conc = min(100, c * 50)
    if c == 0:
        flags.append("nada concreto (número, plazo, nombre)")

    # 3 algo en juego
    s = sum(1 for x in w if x in STAKE_WORDS)
    stake = min(100, s * 55)
    if s == 0 and c >= 2:
        stake = 55  # contraste de cifras (antes/ahora) ya pone algo en juego
    if stake == 0:
        flags.append("no hay nada en juego (costo, pérdida, error, resultado)")

    # 4 carga adelante
    front = 100
    for f in FILLER_OPENERS:
        if low.startswith(f):
            front = 15
            flags.append(f"preámbulo al inicio: «{f}»")
            break
    if front == 100:
        first = w[:4]
        if not any(x in STAKE_WORDS or x in SPOKEN_NUMBERS or re.search(r"\d", x) or x in AUDIENCE_WORDS for x in first):
            front = 60

    # 5 a quién le habla
    aud = 0
    if any(x in AUDIENCE_WORDS for x in w):
        aud = 80
    if any(re.search(p, low) for p in AUDIENCE_PATTERNS):
        aud = 100
    if aud == 0 and any(x in FIRST_PERSON for x in w):
        aud = 60  # confesión en primera persona: válida, pero mejor si nombra al público
    if aud == 0:
        flags.append("no le habla a nadie (tú / un público nombrado / primera persona)")

    checks = {"duracion": dur, "concrecion": conc, "en_juego": stake, "adelante": front, "a_quien": aud}
    vals = list(checks.values())
    mean = sum(vals) / len(vals)
    total = 0.7 * mean + 0.3 * min(vals)
    if any(low.startswith(g.strip()) for g in GREETINGS):
        total = min(total, 30)
        flags.insert(0, "abre con saludo")
    verdict = "FUERTE" if total >= 70 else "OK" if total >= 50 else "FLOJO"
    return {"hook": h, "puntaje": round(total, 1), "veredicto": verdict, "segundos": round(secs, 1),
            "checks": {k: round(v) for k, v in checks.items()}, "alertas": flags}


def check_beats(lines, ppm, objetivo):
    beats = [norm(x) for x in lines if norm(x)]
    out = {"beats": [], "alertas": []}
    t = 0.0
    run_empty = 0
    for i, b in enumerate(beats):
        s = seconds(b, ppm)
        out["beats"].append({"n": i + 1, "desde": round(t, 1), "seg": round(s, 1), "texto": b})
        if i == 0 and s > 3.5:
            out["alertas"].append(f"beat 1 (hook) dura {s:.1f}s: ideal ≤3s")
        if i > 0 and s > 4.5:
            out["alertas"].append(f"beat {i+1} dura {s:.1f}s: máx 4s (partirlo o cambiar plano)")
        if concrete_hits(b) == 0:
            run_empty += 1
            if run_empty == 3:
                out["alertas"].append(f"beats {i-1}-{i+1}: tres seguidos sin nada concreto")
        else:
            run_empty = 0
        t += s
    out["total_seg"] = round(t, 1)
    if objetivo:
        if t > objetivo * 1.2:
            out["alertas"].append(f"dura {t:.1f}s, objetivo {objetivo}s: recortar")
        elif t < objetivo * 0.6:
            out["alertas"].append(f"dura {t:.1f}s, objetivo {objetivo}s: se queda corto")
    if len(beats) >= 2:
        stop = ES_HINTS | EN_HINTS | {"y", "a", "un", "se", "me", "mi", "i", "a", "an"}
        first = {x.lower() for x in words(beats[0]) if x.lower() not in stop and len(x) > 2}
        last = {x.lower() for x in words(beats[-1]) if x.lower() not in stop and len(x) > 2}
        if not first & last:
            out["alertas"].append("sin loop: la última línea no retoma ninguna palabra del hook")
    if beats:
        out["hook"] = score_hook(beats[0], ppm)
    return out


def main():
    ap = argparse.ArgumentParser(description="Verificador de hooks y guiones (ES/EN)")
    ap.add_argument("archivo", nargs="?", help="txt: un hook por línea, o un beat por línea con --beats ('-' = stdin)")
    ap.add_argument("--hook", help="un solo hook")
    ap.add_argument("--beats", action="store_true", help="tratar el archivo como guion, un beat por línea")
    ap.add_argument("--objetivo", type=float, default=0, help="duración objetivo en segundos")
    ap.add_argument("--ppm", type=float, default=0, help="palabras por minuto de quien habla")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if a.hook:
        lines = [a.hook]
    elif a.archivo:
        src = sys.stdin if a.archivo == "-" else open(a.archivo, encoding="utf-8")
        lines = [x for x in src.read().splitlines() if x.strip()]
    else:
        ap.error("pasa un archivo o --hook")

    ppm = a.ppm or default_ppm(lang_of(" ".join(lines)))

    if a.beats:
        res = check_beats(lines, ppm, a.objetivo)
        if a.json:
            print(json.dumps(res, ensure_ascii=False, indent=2)); return
        print(f"GUION · {len(res['beats'])} beats · {res['total_seg']}s a {ppm:.0f} ppm")
        for b in res["beats"]:
            print(f"  {b['n']:>2}  {b['desde']:>5}s  ({b['seg']}s)  {b['texto'][:80]}")
        h = res.get("hook")
        if h:
            print(f"\nHOOK {h['puntaje']} {h['veredicto']}  {h['checks']}")
        print("\nALERTAS" if res["alertas"] or (h and h["alertas"]) else "\nSIN ALERTAS")
        for x in res["alertas"] + (h["alertas"] if h else []):
            print("  - " + x)
        return

    res = sorted((score_hook(x, ppm) for x in lines), key=lambda r: -r["puntaje"])
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2)); return
    print(f"HOOKS · {len(res)} · {ppm:.0f} ppm")
    for r in res:
        print(f"  {r['puntaje']:>5}  {r['veredicto']:<6} {r['segundos']}s  {r['hook'][:90]}")
        for f in r["alertas"]:
            print(f"           · {f}")
    if res and res[0]["puntaje"] < 50:
        print("\nEl mejor está bajo 50: todavía no hay hook. Reescribir antes de grabar.")


if __name__ == "__main__":
    main()
