#!/usr/bin/env python3
"""Validate files referenced by the local pedal configurator."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
required = {
    "index.html", "Bike_Pedal.html", "v3d.js", "Bike Pedal.js",
    "Bike Pedal.css", "visual_logic.js", "Bike Pedal.gltf",
    "Bike Pedal.gltf.xz", "Bike Pedal.bin.xz",
    "Pedal_Logo.png", "sounds/on.mp3",
}
gltf = json.loads((ROOT / "Bike Pedal.gltf").read_text(encoding="utf-8"))
required.update(item["uri"] for item in gltf.get("buffers", []) if "uri" in item)
required.update(item["uri"] for item in gltf.get("images", []) if "uri" in item)

for page in ("index.html", "Bike_Pedal.html"):
    text = (ROOT / page).read_text(encoding="utf-8")
    required.update(re.findall(r'(?:src|href)="([^"?#]+)', text))

missing = sorted(item for item in required if not (ROOT / item).is_file())
if missing:
    print("Missing files:")
    print("\n".join(f"- {item}" for item in missing))
    raise SystemExit(1)

total = sum((ROOT / item).stat().st_size for item in required)
print(f"Validated {len(required)} referenced files ({total / 1_000_000:.2f} MB).")
