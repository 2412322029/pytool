# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:09:59 2022

@author: Molly Jack
"""

import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.font_manager import FontProperties 
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
x = np.arange(1,10) 
y = 2*x +2
plt.title("测试",fontproperties=font) 
plt.xlabel("x 轴",fontproperties=font) 
plt.ylabel("y 轴",fontproperties=font) 
plt.plot(x,y) 
plt.show()
