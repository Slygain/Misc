import Image,ImageDraw,sys
from random import randint as rint

def randgradient():
    img = Image.new("RGB", (300,300), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    r,g,b = rint(0,255), rint(0,255), rint(0,255)
    dr = (rint(0,255) - r)/300.
    dg = (rint(0,255) - g)/300.
    db = (rint(0,255) - b)/300.
    for i in range(300):
        r,g,b = r+dr, g+dg, b+db
        # draw a line from x,y to x,y with a fill of rgb
        draw.line((i,0,i,300), fill=(int(r),int(g),int(b)))

    img.save("out.png", "PNG")

    
    
class AWindow:
    
    width = 8
    height = 8
    def generateWindow(self):
        #GENERATE OUTLINE -- DONE
        #GENERATE FILLING

        #generate 1 of 4 levels of brightness
        # changed to 1-2 so that a majority are of low level brightness
        brightness = rint(0,1)
        brightwindow = rint(0,200)
        # every now and again, someone leaves a light on at work.
        if brightwindow == 22:
            brightness = 4
        #test code
        # brightness = 2
        if(brightness != 0):
        #generate initial RGB
            r = rint(1,64)*brightness-1
            g = rint(1,64)*brightness-1
            b = rint(1,64)*brightness-1
            for i in range(self.width): 
                for j in range(self.height):
                    #outline of window should be black
                    if (i == 0) or (i == self.width-1):
                        self.mArray[i][j] = "#000000"
                    elif (j == 0) or (j == self.height-1):
                        self.mArray[i][j] = "#000000"
                    else: 
                        # generate colour based off initial RGB
                        #j == 0-3 
                        # j == 4-7
                        newr = r + rint(-32,32)
                        if newr > 255:
                            newr = 254
                        if newr < 0:
                            newr = 0
                            
                        newg = g + rint(-32,32)
                        if newg > 255:
                            newg = 254
                        if newg < 0:
                            newg = 0
                            
                        newb = b + rint(-32,32)
                        if newb > 255:
                            newb = 254
                        if newb < 0:
                            newb = 0
                        
                        #g = newr
                        #b = newr
                        
                            
                        #convert to 2 digit hex number:
                        stringR = '%x'%newr
                        if(len(stringR) == 1):
                            stringR = str(0) +'%x'%newr
            
                        stringG = '%x'%newg
                        if(len(stringG) == 1):
                            stringG = str(0) +'%x'%newg

                        stringB = '%x'%newb
                        if(len(stringB) == 1):
                            stringB = str(0) +'%x'%newb
  
                        self.mArray[i][j] = "#" + stringR + stringG + stringB
        else:
            for i in range(self.width): 
                for j in range(self.height):
                    self.mArray[i][j] = "#000000"

                
    def getArray(self):
        return self.mArray
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.mArray = [["#ff0000" for col in range(self.width)] for row in range(self.height)]
        self.generateWindow()

def test():
    thewindow = AWindow(8,8)
    
# Generate a building -- DONE    
def	generateBuilding(size, filename):
    #create base image
    print "Creating File: ",filename
    print "Requested Windows is: ",size

    img = Image.new("RGB", (size,size), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    print "Creating Array"
    #create windows
    amountwindows = size / 8

    #initial slow down whilst creating the array.
    windowArray = [[AWindow(8,8) for col in range(amountwindows)] for row in range(amountwindows)]
    
    print "Starting window creation"

    for i in range(amountwindows):
        if amountwindows%16 == 0:
            print "Windows created",(i+1)*8,"/",size
        for j in range(amountwindows):
            tempArray = windowArray[i][j].getArray()
            for x in range(windowArray[i][j].getWidth()):
                for y in range(windowArray[i][j].getHeight()):
                    draw.line((i*8+x,j*8+y,i*8+x,j*8+y), fill=(tempArray[x][y]))
        
    print "All Windows created, now saving file"
    img.save(filename, "PNG")
    

    
if __name__ == "__main__":
    #randgradient()
    generateBuilding(1024, "test.png")
    #test()



