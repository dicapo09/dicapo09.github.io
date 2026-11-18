#!/usr/bin/env python3
"""Publica una nueva versión de Dicapo Clima para la actualización automática.
Uso: python3 publicar_clima.py DicapoClima_1.1.apk 2 1.1 "Notas de la versión"
- Copia la APK a releases/ y escribe ota/dicapoclima.json con tamaño y SHA-256.
- El versionCode debe ser MAYOR que el instalado y la APK firmada con dicapoclima.jks.
Después: git add -A && git commit -m "Dicapo Clima 1.1" && git push
"""
import hashlib, json, os, shutil, sys
apk, code, name = sys.argv[1], int(sys.argv[2]), sys.argv[3]
notes = sys.argv[4] if len(sys.argv) > 4 else "Mejoras de Dicapo Clima."
here = os.path.dirname(os.path.abspath(__file__))
fname = f"DicapoClima_{name}.apk"
os.makedirs(os.path.join(here, "releases"), exist_ok=True)
dst = os.path.join(here, "releases", fname)
if os.path.abspath(apk) != dst:
    shutil.copyfile(apk, dst)
data = open(dst, "rb").read()
man = {
    "packageName": "cl.dicapo.clima",
    "versionCode": code,
    "versionName": name,
    "minSdk": 24,
    "url": f"https://dicapo09.github.io/releases/{fname}",
    "size": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "notes": notes,
}
open(os.path.join(here, "ota", "dicapoclima.json"), "w").write(json.dumps(man, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(man, ensure_ascii=False, indent=2))
