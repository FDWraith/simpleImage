import math

def createImage():
    sumString = "";

    #Header
    sumString += "P3 500 500 255\n"
    
    for i in range(500):
        for j in range(500):
            R = ( math.sin(i) + math.cos(j) ) % 256
            G = ( j * math.sin(i) ) % 256
            B = ( j * math.sin(i) ) % 256

            sumString += "%s %s %s\n"%(R,G,B)
    return sumString

def commitImage():
    f = open( "img.ppm", "w")
    string = createImage()
    f.write( string )


commitImage()
