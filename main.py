#258-259 columns then each row 0-f
def setupBlockElements(elements):
    start = 0x2580
    end = 0x259F
    for i in range(start, end + 1):
        elements.append(chr(i))
    return elements

def setupBraileElements(elements):
    start = 0x2800
    end = 0x28FF
    for i in range(start, end + 1):
        elements.append(chr(i))
    return elements

def setupBoxElements(elements):
    start = 0x2500
    end = 0x257F
    for i in range(start, end + 1):
        elements.append(chr(i))
    return elements

def setupLegacyElements(elements):
    start = 0x1FB00
    end = 0x1FBFA
    for i in range(start, end + 1):
        elements.append(chr(i))
    return elements
def printElements(elements):
    for i in elements:
        print(i+" ", end="")
    print("\n");

#L-system fractals / procedural plants
def fractalPlants():
    pass

#Boids flocking simulation
def boidsFlocking():
    pass
def getGoodBoxElements(box_elements):
    #box-elements main directions
    vertical = box_elements[2]
    horizontal = box_elements[0]
    left = box_elements[36]
    up = box_elements[52]
    right = box_elements[28]
    down = box_elements[43]
    full = box_elements[59]
    directions = []
    directions.append(vertical)
    directions.append(horizontal)
    directions.append(left)
    directions.append(box_elements[37])
    directions.append(box_elements[38])
    directions.append(right)
    directions.append(up)
    directions.append(down)
    directions.append(full)
    printElements(directions)



block_elements = []
block_elements = setupBlockElements(block_elements)
braile_elements = []
braile_elements = setupBraileElements(braile_elements)
box_elements = []
box_elements = setupBoxElements(box_elements)
legacy_elements = []
legacy_elements = setupLegacyElements(legacy_elements) 
#printElements(block_elements)
#printElements(box_elements)
#printElements(braile_elements)
#printElements(legacy_elements)

#change photo into asci art. 
#   -figure out which asci elements take most to least pixels per character
#   -hardcode each asci that takes the most to least pixel per character
#   -intensity level represents how many character will be used to represent different levels of intensity. 
#   -pixelize each image to make it easier to change to asci characters#    -preprocess each image to black and white to create intensity level of light. 

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
pixelated.save('temp.jpg')
#pixelated.show()
small.show()

small_pixels = small.load()
small_width, small_height = small.size

rgb_asci_map = {}
color_offset = 255 // len(colors_sorted)
color_range = []
basic_asci = [' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']
#setup max color range for each character. 
#' ' . , : ; + * ? % S # @
for i in range(len(colors_sorted)):
    color_range.append(color_offset*(i+1))
    max_rgb = color_offset*(i+1)
    min_rgb = color_offset*(i)
    rgb_asci_map[basic_asci[i]] = [min_rgb, max_rgb]

scale = 4
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
small.show()
