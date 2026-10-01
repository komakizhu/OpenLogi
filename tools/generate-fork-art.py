"""Generate original LogiLocal fork artwork with Pillow (python -m pip install Pillow)."""
import json
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "design/icon"


def mouse(accent, filled):
    image = Image.new("RGBA", (1024, 1024))
    draw = ImageDraw.Draw(image)
    if filled:
        draw.rounded_rectangle((32, 32, 992, 992), radius=220, fill="#102b2b")
    draw.rounded_rectangle((300, 170, 724, 790), radius=212, outline=accent, width=52)
    draw.line((512, 196, 512, 405), fill=accent, width=32)
    draw.rounded_rectangle((478, 275, 546, 375), radius=32, fill="white")
    for x in (378, 512, 646):
        draw.ellipse((x - 28, 870, x + 28, 926), fill=accent)
    return image


for stem, accent, layer in (
    ("openlogi", "#64e4b7", "OpenLogi.png"),
    ("openlogi-prism", "#c1a0ff", "OpenLogi-1.png"),
):
    image = mouse(accent, True)
    image.save(ICONS / f"{stem}.png")
    image.save(ICONS / f"{stem}.ico", sizes=[(n, n) for n in (16, 32, 48, 64, 128, 256)])
    document = ICONS / f"{stem}.icon"
    (document / "Assets").mkdir(parents=True, exist_ok=True)
    mouse(accent, False).save(document / "Assets" / layer)
    data = {
        "fill": {"solid": "srgb:0.06275,0.16863,0.16863,1.00000"},
        "groups": [{"layers": [{"image-name": layer, "name": "LogiLocal mouse", "glass": False}],
                    "shadow": {"kind": "neutral", "opacity": 0.25}, "specular": False}],
        "supported-platforms": {"circles": ["watchOS"], "squares": "shared"},
    }
    (document / "icon.json").write_text(json.dumps(data, indent=2) + "\n")
    if stem == "openlogi":
        for n in (16, 32, 48, 64, 128, 256, 512):
            image.resize((n, n), Image.Resampling.LANCZOS).save(ICONS / f"openlogi-{n}.png")
        image.save(ROOT / "crates/openlogi-desktop/icon/AppIcon.icns")

for variant, background, foreground in (
    ("light", "#edf7f3", "#102b2b"), ("dark", "#102b2b", "#edf7f3")
):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="480" viewBox="0 0 760 480">
  <rect width="760" height="480" fill="{background}"/>
  <text x="380" y="72" text-anchor="middle" font-family="sans-serif" font-size="32" fill="{foreground}">LogiLocal</text>
  <text x="380" y="106" text-anchor="middle" font-family="sans-serif" font-size="16" fill="{foreground}">Independent fork of OpenLogi</text>
  <path d="M320 245h120m-30-25 30 25-30 25" stroke="#42b88c" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <text x="380" y="412" text-anchor="middle" font-family="sans-serif" font-size="18" fill="{foreground}">Drag the app to Applications</text>
</svg>
'''
    (ROOT / f"design/bg/openlogi-dmg-{variant}.svg").write_text(svg)

# Independent template glyphs for macOS and the Windows tray.
for filename, color, variant in (
    ("tray-icon@2x.png", "black", False),
    ("tray-icon-white@2x.png", "white", False),
    ("tray-icon-prism@2x.png", "black", True),
):
    glyph = Image.new("RGBA", (144, 144))
    draw = ImageDraw.Draw(glyph)
    draw.rounded_rectangle((38, 10, 106, 134), radius=34, outline=color, width=10)
    draw.line((72, 15, 72, 46), fill=color, width=8)
    draw.rounded_rectangle((65, 48, 79, 68), radius=6, fill=color)
    if variant:
        draw.line((53, 94, 91, 94), fill=color, width=8)
    glyph.resize((36, 36), Image.Resampling.LANCZOS).save(
        ROOT / "crates/openlogi-agent/assets" / filename
    )
