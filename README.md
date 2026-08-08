# Pedal configurator

## Run

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

