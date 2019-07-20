#!/usr/bin/env python
# coding: utf-8

# In[52]:


from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
#from tesseract import image_to_string

from scipy import misc
import imageio
import cv2
import os
import math

#crear directorio para los frames del video
if not os.path.exists('image_frames'):
    os.makedirs('image_frames')
    
test_vid = cv2.VideoCapture('testvideo.mp4')
frameRate = test_vid.get(3)

index = 0
while test_vid.isOpened():
    ret,frame = test_vid.read()
    frameId = test_vid.get(1)
    if not ret:
        break
        
#asignar un nombre a nuestros archivos:
    name = './image_frames/frame' + str(index) + "." + str(int(frameId)) + '.png'
    
#asignar nuestro print statement
    if (frameId % math.floor(frameRate) == 0):
        print ('Extracting frames...' + name)
        cv2.imwrite(name, frame)
        index = index + 1
        #path = "./image_frames/frame0.png"

        demo = Image.open(name)
        

        
        #def long_slice( slice_size):
        """slice an image into parts slice_size tall"""
        #slice_size = 1000
        cuts = 3
        slice_size = height / cuts
        
        img = Image.open(name)
        width, height = img.size
        upper = 0
        left = 0
        slices = int(math.ceil(height/slice_size))
        
        
        
        count = 1
        for slice in range(slices):
            #if we are at the end, set the lower bound to be the bottom of the image
            if count == slices:
                lower = height
            else:
                lower = int(count * slice_size)  

            bbox = (left, upper, width, lower)
            working_slice = img.crop(bbox)
            upper += slice_size
            count +=1
            #save the slice
            if count == 4:
                slice_path = './image_frames/frame' + str(index) + "." + str(int(frameId)) + str(count) + '.png'
                working_slice.save(os.path.join(slice_path))
                os.remove(name)
                text = pytesseract.image_to_string(slice_path, lang = 'eng')
                print(text)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break     
            


test_vid.release()
cv2.destroyAllWindows()  #destruir todas las ventanas abiertas


# In[ ]:




