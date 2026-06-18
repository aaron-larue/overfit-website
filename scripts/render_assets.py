from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
INK = (242, 240, 232, 255)
TRANSPARENT = (0, 0, 0, 0)

LOGO = """ ██████╗ ██╗   ██╗███████╗██████╗ ███████╗██╗████████╗
██╔═══██╗██║   ██║██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝
██║   ██║██║   ██║█████╗  ██████╔╝█████╗  ██║   ██║
██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══╝  ██║   ██║
╚██████╔╝ ╚████╔╝ ███████╗██║  ██║██║     ██║   ██║
 ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝"""

MARK = """ ██████╗
██╔═══██╗
██║   ██║
██║   ██║
╚██████╔╝
 ╚═════╝"""


def text_bounds(text, font):
    scratch = Image.new("RGBA", (1, 1), TRANSPARENT)
    draw = ImageDraw.Draw(scratch)
    return draw.multiline_textbbox((0, 0), text, font=font, spacing=0)


def render_text_png(text, path, font_size, padding):
    font = ImageFont.truetype(FONT_PATH, font_size)
    left, top, right, bottom = text_bounds(text, font)
    width = right - left + padding * 2
    height = bottom - top + padding * 2
    image = Image.new("RGBA", (width, height), TRANSPARENT)
    draw = ImageDraw.Draw(image)
    draw.multiline_text((padding - left, padding - top), text, font=font, fill=INK, spacing=0)
    image.save(path)


def render_favicon(path):
    font = ImageFont.truetype(FONT_PATH, 56)
    left, top, right, bottom = text_bounds(MARK, font)
    text_width = right - left
    text_height = bottom - top
    image = Image.new("RGBA", (512, 512), TRANSPARENT)
    draw = ImageDraw.Draw(image)
    draw.multiline_text(
        ((512 - text_width) / 2 - left, (512 - text_height) / 2 - top),
        MARK,
        font=font,
        fill=INK,
        spacing=0,
    )
    image.save(path)
    return image


def main():
    ASSETS.mkdir(exist_ok=True)
    render_text_png(LOGO, ASSETS / "overfit-logo.png", font_size=96, padding=48)
    favicon = render_favicon(ASSETS / "favicon.png")
    favicon.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])


if __name__ == "__main__":
    main()
