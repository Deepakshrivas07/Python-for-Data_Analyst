import seaborn as sns;
import  matplotlib.pyplot as plt

flights=sns.load_dataset('flights')
print(flights.head())
sns.lineplot(data = flights,x="month",y="passengers",hue="year")

plt.show()