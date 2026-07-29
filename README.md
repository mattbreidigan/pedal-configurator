# Pedal configurator — local copy

This folder mirrors the public pedal configurator embedded on Tom Dent's
3D-product-configurator demonstration page.

## Run

From PowerShell:

```powershell
cd "D:\New folder\pedal-configurator"
python validate.py
.\serve.ps1
```

Open <http://localhost:8080/>. Do not open `index.html` directly with a
`file://` URL: browsers commonly block glTF buffers and textures in that mode.

To use another port:

```powershell
.\serve.ps1 -Port 9000
```

## Entry points

- `index.html` — original presentation wrapper and preloader.
- `Bike_Pedal.html` — configurator directly, without the outer wrapper.
- `visual_logic.js` — Verge3D interaction/configuration behavior.
- `Bike Pedal.gltf` + `Bike Pedal.bin` — scene and geometry.
- `Bike Pedal.gltf.xz` + `Bike Pedal.bin.xz` — compressed scene files used by
  the configurator's default runtime mode.

## Rights

These are third-party demonstration assets fetched from
<https://tomdent.co.uk/3d-product-configurators/>. Local possession does not
transfer copyright or grant redistribution/commercial-use rights. Verge3D's
runtime is also subject to its applicable license. Confirm permissions with the
rights holders before publishing, modifying for commercial use, or redistributing.
