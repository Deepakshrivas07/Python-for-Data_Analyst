import matplotlib.pyplot as plt

products = ["Laptop","Phone","Tablet","Watch","Camera"]
sales = [120,90,60,45,70]

explode = [0.0,.1,0,0,0] # extract piece

plt.figure(figsize=(7,7)) #figure size

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%", #autopercent % → Format specifier , 1.1f → One digit after the decimal, %% → Display the % symbol
    startangle=90,
    explode=explode,
    shadow=True, # 3d view
    wedgeprops={
        "edgecolor":"black"
    }
)

plt.title("Product Sales Distribution")

plt.show()