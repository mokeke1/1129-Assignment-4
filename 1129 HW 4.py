#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


#1
np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12]])
    


# In[8]:


#2 and #3
xpts = np.arange(1,7)
ypts = np.arange(5, 11)
plt.plot(xpts, ypts)
plt.show()


# In[13]:


#4 
xpts = np.array([0, 1, 2, 3, 4])
ypts = np.array([1, 2, 3, 4, 5])
xpts2 = np.array([0, 1, 2, 3, 4])
ypts2 = np.array([5, 6, 7, 8, 9])
xpts3 = np.array([0, 1, 2, 3, 4])
ypts3 = np.array([9, 10, 11, 12, 13])
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.plot(xpts, ypts, xpts2, ypts2, xpts3, ypts3)
plt.show()


# In[15]:


#5
xpts = np.array([1, 2, 3, 4, 5])
ypts = np.array([1, 2, 9, 16, 25])
plt.subplot(1,3,1)
plt.plot(xpts, ypts)
xpts2 = np.array([1, 2, 3, 4, 5])
ypts2 = np.array([5, 6, 7, 8, 9])
plt.subplot(1,3,2)
plt.plot(xpts2, ypts2)
xpts3 = np.array([1, 2, 3, 4, 5])
ypts3 = np.array([1, 8, 27, 64, 125])
plt.subplot(1,3,3)
plt.plot(xpts3, ypts3)
plt.show()


# In[ ]:




