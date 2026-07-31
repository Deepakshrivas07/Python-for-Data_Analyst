import seaborn as sns;
import  matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
print(tips.head())
sns.boxplot(data = tips,x="day",y="total_bill")

plt.show()