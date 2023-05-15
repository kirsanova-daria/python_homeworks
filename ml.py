import matplotlib.pyplot as plt
import numpy as np

np.random.seed(13)
f, ax = plt.subplots(2, 2)
f.set_figheight(8)
f.set_figwidth(13)
f.suptitle('Plot examples', fontsize=20)
x, y = np.random.multivariate_normal([20, 10], [[1,0.7],[0.7,1]], 5000).T
ax[0,0].scatter(x, y, edgecolors = 'black')
ax[0,0].set_title('Scatter plot example')

x = np.random.geometric(p=0.1, size=3000)
ax[0,1].hist(x, bins = 40)
ax[0,1].set_title('Hist plot example')

x = np.linspace(0, 6)
ax[1,0].plot(np.log(x), color = 'black', label = 'log(x)')
ax[1,0].plot(np.log(2*x), color = 'red', label = 'log(2x)')
ax[1,0].legend()
ax[1,0].set_title('Line plot example')

x = np.arange('2021-01-01', '2021-01-15', dtype='datetime64[D]')
y = np.random.normal(loc=5, size = 14)
ax[1,1].bar(x, y)
ax[1,1].set_xticklabels(x, rotation=90)
ax[1,1].set_title('Bar plot example')

f.set_tight_layout(True)
