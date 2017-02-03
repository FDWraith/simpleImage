
def createImage():
    sumString = "";

    #Header
    sumString += "P3 500 500 255\n"
    
    for i in range(500):
        for j in range(500):
            R = ( i * j ) % 256
            G = ( i * j / 2 ) % 256
            B = ( i * j / 3 ) % 256

            sumString += "%s %s %s\n"%(R,G,B)
    return sumString

def commitImage():
    f = open( "img.ppm", "w")
    string = createImage()
    f.write( string )


commitImage()
