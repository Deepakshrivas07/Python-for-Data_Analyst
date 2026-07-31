import seaborn as sns;
import  matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
#corr means corelation and numeric_only means shows relation in number btwn 0 to 1
corr = tips.corr(numeric_only=True)
#heat map used to show the relation between columns by putting columns in x and y axis both
# sns.set_context("paper")
plt.figure(figsize=(10,6))
sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=True # gives value inside box
)
plt.show()