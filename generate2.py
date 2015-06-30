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

    
def glRgbaFromHsl ( h,  sl,  l):


    v = 0.0
    r = 0.0
    g = 0.0
    b = 0.0

    r = l   # default to gray
    g = l
    b = l
    if (l <= 0.5):
        v = l * (1+sl)
    else:
        v = l + sl - l * sl
    if (v > 0 ):
        m = 0.0
        sv  = 0.0
        sextant = 0
        fract = 0.0
        vsf = 0.0
        mid1 = 0.0
        mid2 = 0.0

        m = l + l - v
        sv = (v - m ) / v
        h = h * 6.0
        sextant = int(h)
        fract = h - sextant
        vsf = v * sv * fract
        mid1 = m + vsf
        mid2 = v - vsf
        if sextant == 0:
            r = v
            g = mid1 
            b = m
        elif sextant == 1:
          r = mid2
          g = v
          b = m
        elif sextant == 2:
          r = m
          g = v
          b = mid1
        elif sextant == 3:
          r = m
          g = mid2
          b = v
        elif sextant == 4:
          r = mid1
          g = m
          b = v
        elif sextant == 5:
          r = v;
          g = m;
          b = mid2;

    glRgba = [r, g, b]
    return glRgba

    
    
    
    
    
class AWindow:
    
    width = 8
    height = 8
    def generateWindow(self):
        #GENERATE OUTLINE -- DONE
        #GENERATE FILLING

        #generate 1 of 4 levels of brightness
        brightness = rint(0,4)
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

        
        
        
class ABuilding:
    SEGMENTS_PER_TEXTURE  = 64
    ONE_SEGMENT = 1.0
    size = 512
    _segment_size = 1.0
    def RANDOM_COLOR_SHIFT(self): 
        return ((rint(0,10)) / 50.0)
    def RANDOM_COLOR_VAL(self):
        return ((rint(0,256)) / 256.0)
    def RANDOM_COLOR_LIGHT(self):
        return ((200 + rint(0,56)) / 256.0)
    
    x = 0
    y = 0
    run = 0
    run_length = 0
    lit_density = 0
    colourR = 0.0
    colourG = 0.0
    colourB = 0.0
    lit = 1
    
    def __init__(self):
        SEGMENTS_PER_TEXTURE  = 64
        ONE_SEGMENT = (1.0 / self.SEGMENTS_PER_TEXTURE)
        self.size = 512
        _segment_size = self.size / self.SEGMENTS_PER_TEXTURE
        
        
        self.x = 0
        self.y = 0
        self.run = 0
        self.run_length = 0
        self.lit_density = 0
        self.colourR = 0.0
        self.colourG = 0.0
        self.colourB = 0.0
        self.lit = 1
        self.mArray = [["#000000" for col in range(self.size)] for row in range(self.size)]
        self.createBuilding()
        
    def createBuilding(self):
        for self.y in range(self.SEGMENTS_PER_TEXTURE):
            if(not(self.y%8)):
                self.run = 0
                self.run_length = rint(0,9) + 2
                self.lit_density = 2 + rint(0,2) + rint(0,2)
                self.lit = 0
            for self.x in range(self.SEGMENTS_PER_TEXTURE):
                if(self.run < 1):
                    self.run = rint(0,self.run_length)
                    self.lit = rint(0,self.lit_density)
                if(self.lit != 0):
                    self.colourR = (0.5 + rint(0,128)/256 + self.RANDOM_COLOR_SHIFT())
                    self.colourG = (0.5 + rint(0,128)/256 + self.RANDOM_COLOR_SHIFT())
                    self.colourB = (0.5 + rint(0,128)/256 + self.RANDOM_COLOR_SHIFT())
                else:
                    self.colourR = (rint(0,40) / 256.0)
                    self.colourG = (rint(0,40) / 256.0)
                    self.colourB = (rint(0,40) / 256.0)
                
                self.drawWindow(self.x * self._segment_size,self.y * self._segment_size, self._segment_size, self.colourR,self.colourG,self.colourB)
                self.run = self.run - 1
    
    def drawWindow(self,x,y,segsize,R,G,B):
        margin = segsize /3
        half = segsize / 2
        i = 0
       
        type = rint(0,8)
        
        if type == 0: #filled, 1pixel frame
            self.drawRect(x + 1, y + 1, x + segsize - 1, y + segsize - 1, R,G,B)
        elif type == 1: #vertical
            self.drawRect(x + margin, y + 1, x + segsize - margin, y + segsize - 1, R,G,B)
        elif type == 2: #side-by-side pair
            self.drawRect(x + 1, y + 1, x + half - 1, y + segsize - margin, R,G,B)
            self.drawRect(x + half + 1, y + 1, x + segsize - 1, y + segsize - margin,  R,G,B)
        elif type == 3: #blinds
            self.drawRect(x + 1, y + 1, x + segsize - 1, y + segsize - 1, R,G,B)
            if(segsize - 2 > 1):
                i = rint(0,int(segsize - 2))
            self.drawRect (x + 1, y + 1, x + segsize - 1, y + i + 1, R * 0.3,G * 0.3,B * 0.3)
        elif type == 4: #vert stripes
            self.drawRect(x + 1, y + 1, x + segsize - 1, y + segsize - 1, R,G,B)
            self.drawRect(x + margin, y + 1, x + margin, y + segsize - 1, R * 0.7,G * 0.7,B * 0.7)
            self.drawRect(x + segsize - margin - 1, y + 1, x + segsize - margin - 1, y + segsize - 1, R * 0.3,G * 0.3,B * 0.3)
        elif type == 5: #wide horizontal
            self.drawRect(x + 1, y + 1, x + segsize - 1, y + segsize - margin, R,G,B)
        elif type == 6: #4-pane
            self.drawRect(x + 2, y + 1, x + segsize - 1, y + segsize - 1, R,G,B)
            self.drawRect(x + 2, y + half, x + segsize - 1, y + half, R * 0.2,G * 0.2,B * 0.2)
            self.drawRect(x + half, y + 1, x + half, y + segsize - 1, R * 0.2,G * 0.2,B * 0.2)
        elif type == 7: #single narrow
            self.drawRect(x + half - 1, y + 1, x + half + 1, y + segsize - margin, R,G,B)
        elif type == 8: # horizontal
            self.drawRect(x + 1, y + margin, x + segsize - 1, y + segsize - margin - 1, R,G,B)
        
        
    def setmVal(self,x,y,r,g,b,a):
        #set colour to point
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
            
        newa = a + rint(-32,32)
        if newa > 255:
            newa = 254
        if newa < 0:
            newa = 0
            
        stringR = '%x'%newr
        if(len(stringR) == 1):
            stringR = str(0) +'%x'%newr
        stringG = '%x'%newg
        if(len(stringG) == 1):
            stringG = str(0) +'%x'%newg
        stringB = '%x'%newb
        if(len(stringB) == 1):
            stringB = str(0) +'%x'%newb
        stringA = '%x'%newa
        if(len(stringA) == 1):
            stringA = str(0) +'%x'%newa
            
        self.mArray[x][y] = "#" + stringR + stringG + stringB + stringA
        print self.mArray[x][y]

    def drawRect(self,left,top,right,bottom,R,G,B):
        repeats = 0
        height = 0
        i = 0
        j = 0
        noiseR = 0
        noiseG = 0
        noiseB = 0
        noiseA = 0
        color_noise = [0,0,0]
        average = (R+G+B)/3.0
        bright = average
        potential = int(average*255.0)
        
        if(bright != 0):
            for i in range(int(left+1),int(right-1)):
                for j in range(int(top + 1), int(bottom - 1)):
                    hue = 0.2 + rint(0,100) / 300.0 + rint(0,100) / 300.0 + rint(0,100) / 300.0
                    color_noise = glRgbaFromHsl (hue, 0.3, 0.5);
                    noiseR = color_noise[0]
                    noiseG = color_noise[1]
                    noiseB = color_noise[2]
                    noiseA = rint (potential) / 144.0;
                    colR = self.RANDOM_COLOR_VAL()
                    colG = self.RANDOM_COLOR_VAL()
                    colB = self.RANDOM_COLOR_VAL()
                    colA = rint(0,potential) / 144.0
                    setmVal(i,j,colR,colG,colB,colA)
                    print "success"
                    
                    
                    #texture point
        else:
            repeats = rint(0,6) + 1
            height = (bottom - top) + (rint(0,3) - 1) + (rint(0,3) - 1)
            for i in range(left,right):
                if (rint(0,3) == 0):
                    repeats = rint(0,4) + 1
                if (rint(0,6) == 0): 
                    height = bottom - top
                    height = rint(0,height)
                    height = rint(0,height)
                    height = rint(0,height)
                    height = ((bottom - top) + height) / 2
              
                for j in range(0,1): 
                  #  glColor4f (0, 0, 0, rint(0,256) / 256.0)
                    setmVal(i,bottom - height,0,0,0)
                   # glColor4f (0, 0, 0, rint(0,256) / 256.0)
                    setmVal(i,bottom,0,0,0)

    def getArray(self):
        return self.mArray
            
                    
                    
def test():
    thewindow = AWindow(8,8)
    
# Generate a building -- DONE    
def	generateBuilding(size, filename):
    #create base image
    img = Image.new("RGB", (size,size), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    #create windows
    amountwindows = size / 8
    windowArray = [[AWindow(8,8) for col in range(amountwindows)] for row in range(amountwindows)]
    
    for i in range(amountwindows):
        for j in range(amountwindows):
            tempArray = windowArray[i][j].getArray()
            for x in range(windowArray[i][j].getWidth()):
                for y in range(windowArray[i][j].getHeight()):
                    draw.line((i*8+x,j*8+y,i*8+x,j*8+y), fill=(tempArray[x][y]))
   

    img.save(filename, "PNG")
    
def	generateBuilding2(size, filename):
    #create base image
    img = Image.new("RGBA", (size,size), "#FFFFFFFF")
    draw = ImageDraw.Draw(img)
    
    fred = ABuilding()
    #create windows
    for i in range(0,size):
        for j in range(0,size):
            draw.line((i,j,i,j), fill=(fred.getArray()[i][j]))
   

    img.save(filename, "PNG")
    
if __name__ == "__main__":
    #randgradient()
    generateBuilding(512, "bob.png")
    generateBuilding2(512, "fred.png")
    #test()
    
