#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[9]:



import numpy as np
import cv2
import pyautogui


# In[10]:


# Specify resolution
resolution = (1920, 1080)
#setting fps
g = 60;
#creating dimension

#creating video format
f = cv2.VideoWriter_fourcc(*"xvid")
#variable for storing the video
u = cv2.VideoWriter("reec.avi",f,g,resolution)
# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
# Resize this window
cv2.resizeWindow("Live", 480, 270)

#creating loop for clicking photos in milli seconds using pyautogui
while True:
    image = pyautogui.screenshot()
    arr = np.array(image)
    #providing original colour to the video
    colour = cv2.cvtColor(arr,cv2.COLOR_BGR2RGB)
    #using write function to acess the file in python as it changes the file every time loops run
    u.write(colour)
  
    # Display the recording screen
    cv2.imshow('Live', colour)
  # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
#creating a release function 
u.release()
# Destroy all windows
cv2.destroyAllWindows()
#display message
print("---END---")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




