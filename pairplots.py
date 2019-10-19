import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='ticks')

tips = sns.load_dataset('tips')

# g = sns.FacetGrid(tips, hue='time')
#
# g.map(plt.scatter,'total_bill', 'tip')
# g.add_legend()

g = sns.FacetGrid(tips, row='smoker', col='time', margin_titles=True)
g.map(sns.regplot, 'size', 'total_bill', color='.3', fit_reg=False, x_jitter=.1)

plt.show()

