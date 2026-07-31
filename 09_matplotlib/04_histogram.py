import matplotlib.pyplot as plt
import numpy as np

#HISTOGRAM (NOTE: used when to see outliers)

data = np.random.randn(1000)
plt.hist(data,bins=30,color='blue',edgecolor='black') #bins means no. range in x axis
plt.show()