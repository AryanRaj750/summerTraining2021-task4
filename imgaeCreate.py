#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2, numpy, imutils

class ImageProcessing:
    def __init__(self, pic):
        self._pic = pic
        self._pic = cv2.imread(f"{pic}")
        self._pic1 = imutils.resize(self._pic, width=300)
    def showImage(self):
        cv2.imshow(f"{self._pic}", self._pic)
        cv2.waitKey(1000)
        
    def cropOne(self, x1, x2, y1, y2):
        self._x1 = int(x1)
        self._x2 = int(x2)
        self._y1 = int(y1)
        self._y2 = int(y2)
        self._cropped_pic = self._pic1[self._x1 : self._x2, self._y1 : self._y2]
        
    def swapImages(self, pic1, pic2, width=300):
        _pic1 = cv2.imread(f"{pic1}")
        _pic2 = cv2.imread(f"{pic2}")
        self._pic1 = imutils.resize(_pic1, width=300, inter=3)
        self._pic2 = imutils.resize(_pic2, width=300, inter=3)
        pic = numpy.empty_like(self._pic1)
        pic = self._pic1[ : self._pic1.shape[0], :self._pic1.shape[1] ]
        self.Swap_pic1 = self._pic2[ : self._pic2.shape[0], : self._pic2.shape[1] ]
        self.Swap_pic2 = pic[ :, :]
        cv2.imshow(f"{pic1}", self.Swap_pic1)
        cv2.waitKey(1000)
        cv2.imshow(f"{pic2}", self.Swap_pic2)
        cv2.waitKey(1000)
    def combineTwoImage(self, img1, img2, width=300):
        _img1 = cv2.imread(f"{img1}")
        _img2 = cv2.imread(f"{img2}")
        self._img1 = imutils.resize(_img1, height=300, inter=3)
        self._img2 = imutils.resize(_img2, height=300, inter=3)
        
        #x1 = cv2.resize(self._img1, ())
        combined_image = numpy.hstack((self._img1, self._img2))
        
        """
        sinImg = numpy.empty((self._img1.shape[0], self._img1.shape[1]+self._img2.shape[1], 3))
        print(sinImg.shape)
        for i in range(self._img1.shape[0]):
            for j in range(self._img1.shape[1]):
                for k in self._img1:
                    sinImg[i][j] = k
        
        for i in range(self._img1.shape[0]):
            for j in range(self._img1.shape[1], self._img1.shape[1] + self._img2.shape[1]):
                for k in self._img2:
                    sinImg[i][j] = k
                    """
        cv2.imshow("combined image", combined_image)   
        cv2.waitKey(1000)
        
    def showCropImage(self):
        cv2.imshow(f"{self._pic}", self._cropped_pic)
        cv2.waitKey(1000)
def closeImages():
    cv2.destroyAllWindows()     
import numpy, cv2, imutils


###class for creating image
class PlainImage:
    def __init__(self, width=800, height=1000, colorCode=[0,0,0], height_of_house=200,
                 width_of_house=200, position_of_house_x1=200, position_of_house_y1=400, thickness =2,
                 front_width=50,gallary_height=20,staircase_width=15):

        self._width = width
        self._height = height
        self._colorCode = colorCode
        self._height_of_house = height_of_house
        self._width_of_house = width_of_house
        self._position_of_house_x1 = position_of_house_x1
        self._position_of_house_y1 = position_of_house_x1
        self._position_of_house_x2 = position_of_house_x1 + height_of_house
        self._position_of_house_y2 = position_of_house_y1 + width_of_house
        self._thickness = thickness
        self._front_width = front_width
        self._staircase_width = staircase_width
        self._gallary_height = gallary_height
        image = [[[ pixelColor for pixelColor in self._colorCode] for j in range(self._height)] for i in range(self._width) ]
        img1 = numpy.array(image)
        self._image = numpy.uint8(img1)
    def boundary(self, color=[255,255,255]): 
        self._color = color
        #construcing left wall edge
        for i in range(self._position_of_house_x1, self._position_of_house_x2):
            for j in range(self._position_of_house_y1, self._position_of_house_y1 + self._thickness):
                for k in self._color:
                    #x[i][j] = reset
                    self._image[i][j] = k

        #construcing right wall edge
        for i in range(self._position_of_house_x1, self._position_of_house_x2):
            for j in range(self._position_of_house_y2, self._position_of_house_y2 + self._thickness):
                for k in self._color:
                    self._image[i][j] = k

        #construcing top wall edge
        for i in range(self._position_of_house_x1, self._position_of_house_x1 + self._thickness):
            for j in range(self._position_of_house_y1, self._position_of_house_y2 + self._thickness):
                for k in self._color:
                    self._image[i][j] = k
        #construcing bottom wall edge
        for i in range(self._position_of_house_x2 - self._thickness, self._position_of_house_x2):
            for j in range(self._position_of_house_y1,self._position_of_house_y2):
                for k in self._color:
                    self._image[i][j] = k
    def fillboundary(self, newImg, left = 20, Top=5):
        pimg = cv2.imread(f"{newImg}")
        newImg = imutils.resize(pimg, width=320, height=850)
        #new1 =  [[[ c for c in newImg[a][b] ]for b in range(300)] for a in range(194)]
        for a in range(15,newImg.shape[0]):
            for b in range(newImg.shape[1]):
                for c in newImg[a][b]:
                    self._image[self._position_of_house_x1 + Top + a][self._position_of_house_y1 + left + b] = c
        
    def frontBase(self, fcolor=[174,0,87], bcolor =[255,255,255]):
        #construcing houseleft front edge 
        self._fcolor = fcolor 
        self._bcolor = bcolor
        p = 0
        for i in range(self._position_of_house_x2, self._position_of_house_x2 + self._front_width):    
            for j in range(self._position_of_house_y1-p, self._position_of_house_y1 + self._thickness -p):
                for k in self._bcolor:
                    self._image[i][j] = k
            p += 1
        #construcing house right front edge           
        p = 0
        t = 0
        z = 602
        for i in range(self._position_of_house_x2, self._position_of_house_x2 + self._front_width + self._staircase_width):   
            for j in range(self._position_of_house_y2-p, self._position_of_house_y2 + self._thickness +1-t):
                for k in self._bcolor:
                    self._image[i][j] = k
            if p>=10:
                t += 1
            p += 1

        #color front space
        p = 0
        for i in range(self._position_of_house_x2, self._position_of_house_x2 + self._front_width):    
            for j in range(self._position_of_house_y1 + self._thickness - p, self._position_of_house_y2-p):
                for k in self._fcolor:
                    self._image[i][j] = k
            p += 1
        #design staircase   
        for i in range(self._position_of_house_x2 + self._front_width, self._position_of_house_x2 + self._front_width +
                       self._staircase_width):
            for j in range(self._position_of_house_y1 - self._front_width, self._position_of_house_y2 - self._front_width +1):
                for k in self._bcolor:
                    self._image[i][j] = k
    def show(self):
        image = numpy.array(self._image)
        image = numpy.uint8(image)
        cv2.imshow("image", image)
        cv2.waitKey(1000)


# In[ ]:


# "./tasks/om.jpg"
# "./tasks/shanati.jfif"
#img1 = PlainImage()
#img1.boundary()
#img1.frontBase()
#img1.fillboundary("./tasks/om.jpg", Top =-5, left=25)
#img1.show()


# In[3]:


#task 4.2, 4.3, of summer training 
#Initialising object
img = ImageProcessing("./tasks/om2.jpg")


# In[4]:


img.showImage()


# In[6]:


#Task 4.2 swaping two images by loop
img.swapImages("./tasks/om2.jpg", "./tasks/shanati.jfif" )


# In[8]:


#task 4.3 combining two images
img.combineTwoImage( "./tasks/om2.jpg", "./tasks/shanati.jfif")


# In[7]:


closeImages()


# In[ ]:




