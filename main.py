#change photo into asci art. 
#   -figure out which asci elements take most to least pixels per character
#   -hardcode each asci that takes the most to least pixel per character
#   -intensity level represents how many character will be used to represent different levels of intensity. 
#   -pixelize each image to make it easier to change to asci characters
#   -preprocess each image to black and white to create intensity level of light. 

from PIL import Image
import time
import asci_utils
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
    v2_asci_map = {}
    v3_asci_map = {}
    rgb_asci_map = {}
    color_offset = 255 // len(colors_sorted)
    basic_asci = [' ', '.', ',', ':', ';', '+', '*', '?', 'S', '#', '@']
    v2_asci = [' ', '.', ',', ':', ';', '+', '*', '?', 'S', '#', '@']
    v3_asci = [' ', '.', ',', ':', ';', '+', '*', '?', 'S', '#', '@']
    if (len(colors_sorted) <= len(basic_asci)):
        for i in range(len(colors_sorted)):
            max_rgb = color_offset*(i+1)
            min_rgb = color_offset*(i)
            rgb_asci_map[basic_asci[i]] = [min_rgb, max_rgb]
    return rgb_asci_map


def printImage(small, rgb_asci_map, scale = 2):
    small_width, small_height = small.size
    small_pixels = small.load()
    full_art = []
    full_art_codes = []
    truth_keeper = []
    for y in range(small_height):
        sub_art = []
        sub_art_codes = []
        sub_truth = []
        for x in range(small_width):
            current_rgb = small_pixels[x,y]
            current_r = current_rgb[0]
            for key in rgb_asci_map:
                spacer = " "
                r_min = rgb_asci_map[key][0]
                r_max = rgb_asci_map[key][1]
                if(current_r >= r_min and current_r < r_max):
                    for i in range(scale):
                        sub_art.append(str(key))
                        sub_art_codes.append(ord(key))
                        spacer = " "
                        if spacer == str(key):
                            sub_truth.append(True)
                        else:
                            sub_truth.append(False)
            #print(key, end="")
        truth_keeper.append(sub_truth)
        full_art.append("".join(sub_art))
        full_art_codes.append(sub_art_codes)
        #print("\n")
    return full_art, truth_keeper, full_art_codes


def updateImage(full_art, truth_keeper, full_art_codes, offset = 1, changes = 1, maxChanges = 300, sleep = 0.1):
    char_min = 32
    char_max = 126
    #print from the full code set
    updated_full_art = []
    while(changes < maxChanges):
        for line_index, line in enumerate(full_art_codes):
            #convert back into regular char
            updated_line = []
            for code_index, code in enumerate(line):
                if(truth_keeper[line_index][code_index] == False):
                    code = code + offset
                    if(code>=char_max):
                        code = char_min  
                    symbol = chr(code)
                else:
                    symbol = chr(code)
                full_art_codes[line_index][code_index] = code
                updated_line.append(symbol)
            print("".join(updated_line))
            #line = "".join(line)
        changes += 1
        go_back=len(full_art_codes)
        print(f"\033[{go_back}A", end="", flush=True)
        print(f"\033[J", end="")
        time.sleep(sleep)
    #print from the basic full text set
    for line in full_art:
        pass
        #print(line)

#def printImage(small, rgb_asci_map, scale = 2):
#    pass
    
rgb_asci_map = setup_asci_range(colors_sorted)
full_art, truth_keeper, full_art_codes = printImage(small, rgb_asci_map)
updateImage(full_art, truth_keeper,full_art_codes)


