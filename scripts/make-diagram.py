#!/usr/bin/env python3
"""Draw docs/screenshots/how-it-works.png — the pour flow, self-contained."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1280, 640
BG = (13, 18, 40)
CARD = (24, 32, 64)
GOLD = (201, 162, 39)
GOLD_SOFT = (232, 205, 128)
TEXT = (240, 244, 255)
MUTED = (159, 176, 224)
GREEN = (74, 222, 128)
RED = (255, 107, 107)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_CJK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    title_f = ImageFont.truetype(FONT_BOLD, 34)
    card_f = ImageFont.truetype(FONT_BOLD, 21)
    sub_f = ImageFont.truetype(FONT_REG, 16)
    cjk_f = ImageFont.truetype(FONT_CJK, 15)

    d.text((48, 34), "How the pour works", font=title_f, fill=TEXT)
    d.text((48, 78), "Skill-bartender 技能配杯流程", font=cjk_f, fill=MUTED)

    def card(x, y, w, h, title, subs, accent=GOLD, fill=CARD):
        d.rounded_rectangle((x, y, x + w, y + h), radius=14, fill=fill, outline=accent, width=2)
        d.rectangle((x + 2, y + 24, x + 2, y + 24), fill=accent)
        d.text((x + 18, y + 16), title, font=card_f, fill=TEXT)
        yy = y + 52
        for s in subs:
            d.text((x + 18, yy), s, font=sub_f, fill=MUTED)
            yy += 26

    def arrow(x1, y1, x2, y2):
        d.line((x1, y1, x2, y2), fill=GOLD_SOFT, width=3)
        # arrowhead
        import math
        ang = math.atan2(y2 - y1, x2 - x1)
        for da in (0.42, -0.42):
            d.line((x2, y2, x2 - 16 * math.cos(ang + da), y2 - 16 * math.sin(ang + da)),
                   fill=GOLD_SOFT, width=3)

    # Row 1: the ladder
    card(48, 130, 260, 150, "0 · Plain tools", ["read / grep / bash / web", "load nothing"], accent=GREEN)
    card(340, 130, 260, 150, "1 · One match", ["exactly one skill fits", "load it"], accent=GOLD)
    card(632, 130, 260, 150, "2 · Workflow", ["a workflow skill composes it", "load it, never hand-assemble"], accent=GOLD)
    card(924, 130, 308, 150, "3 · Unsure", ["a wrong body lives in history", "miss beats false pour →", "don't load"], accent=RED)
    arrow(308, 205, 340, 205)
    arrow(600, 205, 632, 205)
    arrow(892, 205, 924, 205)

    # Row 2: the cellar
    card(48, 330, 380, 250, "Missing skill?", ["quarantine dir — never straight into", "the skills root"], accent=GOLD)
    arrow(428, 405, 470, 405)
    card(470, 330, 380, 250, "Taste · SkillSpector scan", ["static scan = filter, not guarantee", "scripts/ are code — show the human,", "default deny"], accent=GOLD)
    arrow(850, 405, 892, 405)
    card(892, 330, 340, 250, "Human approval → install", ["source URL + commit hash + verdict", "explicit yes required", "never auto-installs"], accent=GREEN)

    out = ROOT / "docs" / "screenshots" / "how-it-works.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print("wrote:", out)


if __name__ == "__main__":
    main()
