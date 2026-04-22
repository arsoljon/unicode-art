from PIL import Image, ImageDraw, ImageFont
import numpy as np
import string

# Config
font_path = "DejaVuSansMono.ttf"  # use any monospace font
font_size = 32
chars = string.printable  # or limit to ASCII 32–126
print(chars)

font = ImageFont.truetype(font_path, font_size)

def glyph_density(char):
    # render character to image
    img = Image.new("L", (font_size, font_size), color=0)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), char, fill=255, font=font)

    arr = np.array(img) / 255.0  # normalize
    return arr.mean()  # weighted density

densities = [(c, glyph_density(c)) for c in chars]

# sort from light → dark
densities.sort(key=lambda x: x[1])

ramp = "".join([c for c, _ in densities])
print(ramp)


def image_to_ascii(image_path, ramp, width=100):
    img = Image.open(image_path).convert("L")

    # keep aspect ratio (characters are taller than wide)
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.5)

    img = img.resize((width, height))
    arr = np.array(img) / 255.0

    ascii_img = ""
    for row in arr:
        for pixel in row:
            idx = int(pixel * (len(ramp) - 1))
            ascii_img += ramp[idx]
        ascii_img += "\n"

    return ascii_img

print(image_to_ascii("input.jpg", ramp))


def glyph_signature(char, grid=3):
    img = Image.new("L", (font_size, font_size), 0)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), char, fill=255, font=font)

    arr = np.array(img) / 255.0
    h, w = arr.shape

    cell_h, cell_w = h // grid, w // grid
    sig = []

    for y in range(grid):
        for x in range(grid):
            cell = arr[y*cell_h:(y+1)*cell_h,
                       x*cell_w:(x+1)*cell_w]
            sig.append(cell.mean())

    return np.array(sig)
    
    
    def best_match(patch, glyph_sigs):
    # patch is same grid shape flattened
    return min(glyph_sigs.items(),
               key=lambda kv: np.linalg.norm(patch - kv[1]))[0]
               
    arr = arr ** 0.8
