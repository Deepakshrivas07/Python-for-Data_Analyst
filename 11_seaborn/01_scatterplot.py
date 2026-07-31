import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style("darkgrid") #to set background(grid)
tips = sns.load_dataset("tips") #Popular ones:tip,siris,penguins,titanic,diamonds,flights ,mpg
# print(tips.head()) 
#hue parameter determines which column in the dataset is used for color encoding to distinguish different categories or groups within the visualization.
sns.scatterplot(data=tips,x='total_bill',y='tip', hue='sex') 
plt.show()