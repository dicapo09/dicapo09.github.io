#!/usr/bin/env python3
"""Publica una nueva versión de Dicapo TV para la actualización automática.
Uso: python3 publicar.py DicapoTV_21.8.apk 43701 21.8 "Notas de la versión"
- Copia la APK a releases/ y escribe ota/dicapotv.json con tamaño y SHA-256.
- El versionCode debe ser MAYOR que el instalado y la APK firmada con dicapo.keystore.
Después: git add -A && git commit -m "Dicapo TV 21.8" && git push
"""
import hashlib, json, os, shutil, sys
apk, code, name = sys.argv[1], int(sys.argv[2]), sys.argv[3]
notes = sys.argv[4] if len(sys.argv) > 4 else "Mejoras de Dicapo TV."
here = os.path.dirname(os.path.abspath(__file__))
fname = f"DicapoTV_{name}.apk"
dst = os.path.join(here, "releases", fname)
if os.path.abspath(apk) != dst:
    shutil.copyfile(apk, dst)
data = open(dst, "rb").read()
man = {
    "packageName": "com.xuper.wiwyxuper",
    "versionCode": code,
    "versionName": name,
    "minSdk": 22,
    "url": f"https://dicapo09.github.io/releases/{fname}",
    "size": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "notes": notes,
}
open(os.path.join(here, "ota", "dicapotv.json"), "w").write(json.dumps(man, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(man, ensure_ascii=False, indent=2))
