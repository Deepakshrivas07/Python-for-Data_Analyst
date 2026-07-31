import matplotlib.pyplot as plt
import numpy as np
# SCATTER CHART

x = [1,2,3,4,5]
y1= [10,20,25,30,20]
y2 = [20,10,30,10,20]

plt.scatter(x,y1,color='green',s=20,alpha=.7,marker='*') #s stands for size
plt.scatter(x,y2,color='red',s=20,alpha=.7, marker='o')
plt.legend()

plt.show()
#REST STYLING AND ALL ARE SAME AS USED IN LINE_CHART