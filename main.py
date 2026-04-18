#change photo into asci art. 
#   -figure out which asci elements take most to least pixels per character
#   -hardcode each asci that takes the most to least pixel per character
#   -intensity level represents how many character will be used to represent different levels of intensity. 
#   -pixelize each image to make it easier to change to asci characters
#   -preprocess each image to black and white to create intensity level of light. 

from PIL import Image
img_location = "pictures/shinji.jpg"
img = Image.open(img_location)
pixels = img.load()
width, height = img.size
pixel_size = 5
bw = img.convert("L")
small = bw.resize((img.width // pixel_size, img.height // pixel_size), resample = Image.NEAREST)

small = small.quantize(colors=10).convert("RGB")
colors = small.getcolors(maxcolors=10)
colors_sorted = sorted(colors, key=lambda x: sum(x[1]))
pixelated = small.resize(img.size, Image.NEAREST)

small_pixels = small.load()
small_width, small_height = small.size

def setup_asci_range(colors_sorted):
    #setup max color range for each character. 
    #' ' . , : ; + * ? % S # @
    rgb_asci_map = {}
    color_offset = 255 // len(colors_sorted)
    basic_asci = [' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']
    if (len(colors_sorted) <= len(basic_asci)):
        for i in range(len(colors_sorted)):
            max_rgb = color_offset*(i+1)
            min_rgb = color_offset*(i)
            rgb_asci_map[basic_asci[i]] = [min_rgb, max_rgb]
    return rgb_asci_map

rgb_asci_map = setup_asci_range(colors_sorted)

def printImage(small, rgb_asci_map, scale = 4):
    small_width, small_height = small.size
    small_pixels = small.load()
    for y in range(small_height):
        for x in range(small_width):
            current_rgb = small_pixels[x,y]
            current_r = current_rgb[0]
            for key in rgb_asci_map:
                r_min = rgb_asci_map[key][0]
                r_max = rgb_asci_map[key][1]
                if(current_r >= r_min and current_r < r_max):
                    for i in range(scale):
                        print(key, end="")
        print("\n")

printImage(small, rgb_asci_map)
