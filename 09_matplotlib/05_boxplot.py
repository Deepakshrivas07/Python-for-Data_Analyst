import matplotlib.pyplot as plt
import numpy as np

#BOXPLOT (it is used to detect the outliers(symbol: O))
#median,min,max and outliers
data = np.random.randn(1000)
plt.boxplot(data)
plt.show() 