import matplotlib.pyplot as plt
import numpy as np
#PROFESSIONAL LINE CHART

x = [1,2,3,4,5]
y1= [10,20,25,30,20]
y2 = [20,10,30,10,20]

plt.figure(figsize=(10,5)) # to define the size of graph to see chart properly
plt.plot(x,y1,
        color='red',
        linewidth=2, 
        linestyle='-.',
        marker='^', #when graph line takes sharp turn we used to mark it so we use marker(o,*,D,^)
        markersize=7, # define size of marker
        markerfacecolor='yellow', #marker face color
        markeredgecolor='black', #marker edge color
        alpha=1, #opacity 
        label='2024' #label of perticular line .. it is used when there is multiple lines
)
plt.plot(x,y2,
        color='green',
        linewidth=2,
        linestyle='-.',
        marker='^',
        markersize=7,
        markerfacecolor='yellow',
        markeredgecolor='black',
        alpha=1, #opacity
        label='2025'
        )
plt.legend() # if graph has multiple lines we use legend to merge multiple line in one graph to see relation and stats
plt.grid(True)   # makes grid in background
plt.grid(color='gray', linestyle='--') #grid styes
plt.title("simple line chart") 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.fill_between(x,y1,color="red",alpha=0.3) # to color the region of line-chart for better visualization
plt.fill_between(x,y2,color="green",alpha=0.3)

for i,j in zip(x,y1):
    plt.text(i,j+1,str(j),ha='center') #shows exact value of  the turn's of line chart
for i,j in zip(x,y2):
    plt.text(i,j+1,str(j),ha='center')

plt.show() 