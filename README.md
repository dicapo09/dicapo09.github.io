# Dicapo TV — actualizaciones

Este sitio (https://dicapo09.github.io) alimenta la actualización automática de Dicapo TV (desde la v21.7).

- `ota/dicapotv.json`: versión publicada (la app la consulta una vez al día y desde la campana).
- `releases/`: las APK. Deben estar firmadas con `dicapo.keystore` y tener un `versionCode` mayor que el instalado.

Publicar una versión nueva:

```
python3 publicar.py DicapoTV_21.8.apk 43701 21.8 "Qué trae esta versión"
git add -A && git commit -m "Dicapo TV 21.8" && git push
```

Conviene borrar de `releases/` las APK viejas para no llenar el sitio (límite 1 GB).

## Dicapo TV Pro

- `ota/dicapotvpro.json` y `releases/DicapoTVPro_X.apk` (desde la 1.0.10).
- La APK publicada nunca lleva listas con usuario y contraseña.
- Va firmada con la llave del proyecto Dicapo TV Pro, no con `dicapo.keystore`.
