import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np

# cat = [1,2,3,4,5,6]
# dog = [0,9,7,3,5,1]

# fig, ax = plt.subplots(2)
# ax[0].plot(dog, label="dog")
# ax[0].plot(cat, label="cat")
# ax[0].legend()

# ax[1].bar(dog, cat)

# plt.show()

jet= plt.get_cmap('jet')
colors = pl.cm.jet(np.linspace(0,1000,9001))

x = np.arange(14)
y = np.sin(x / 2)


for i in range(1000):
    plt.plot(x+i, y, label=f"{i}", color=colors[i])

plt.legend(loc = 'best')

plt.show()