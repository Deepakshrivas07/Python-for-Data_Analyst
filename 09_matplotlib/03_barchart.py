import matplotlib.pyplot as plt
import numpy as np
#PROFESSIONAL BAR CHART

products = ["Laptop", "Phone", "Tablet", "Watch", "Camera"]
sales = [120, 90, 60, 45, 70]

bars = plt.bar(products, sales, color="skyblue",
    edgecolor="black",
    linewidth=2)

#Show Value on Top of Each Bar
for bar in bars: 
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+1,
        str(bar.get_height()),
        ha="center",
        fontsize=10
    )

plt.grid(axis="y",linestyle="--")
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()