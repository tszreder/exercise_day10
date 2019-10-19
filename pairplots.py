import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='ticks')

tips = sns.load_dataset('tips')

g = sns.FacetGrid(tips, col='time')

plt.show()

print('Pairplots added')