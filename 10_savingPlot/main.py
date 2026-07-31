import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1,11)
sales_in_cr = np.array([1,2.4,5.4,1.4,6,4,6,8.4,9,7])
plt.figure(figsize=(10,5))
plt.plot(days,
        sales_in_cr,
        color = 'red',
        marker='o',
        markerfacecolor='red',
        linestyle='--',
         )

plt.title('REVANUE:')
plt.xlabel('DAYS')
plt.xlabel('SALES IN CR.')
plt.grid(True)
plt.grid(color='gray',linestyle='-',alpha=0.5)
# plt.savefig('revanue.png')
plt.savefig('revanue.pdf')
plt.show()
