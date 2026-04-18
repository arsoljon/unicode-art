
#258-259 columns then each row 0-f
def setupBlockElements():
    elements = []
    start = 0x2580
    end = 0x259F
    for i in range(start, end + 1):
        elements.append(chr(i))
    return elements

def setupBraileElements():
    elements = []
    start = 0x2800
    end = 0x28FF
    for i in range(start, end + 1):
        elements.append(chr(i))
    return elements

def setupBoxElements():
    elements = []
    start = 0x2500
    end = 0x257F
    for i in range(start, end + 1):
        elements.append(chr(i))
    return elements

def setupLegacyElements():
    elements = []
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



block_elements = setupBlockElements()
braile_elements = setupBraileElements()
box_elements = setupBoxElements()
legacy_elements = setupLegacyElements() 

