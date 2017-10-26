import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

dimension =2
plt.figure(figsize = (dimension,dimension))
gs1 = gridspec.GridSpec(dimension, dimension)
gs1.update(wspace=0.025, hspace=0.05) # set the spacing between axes.

for i in range(dimension*dimension):
   # i = i + 1 # grid spec indexes from 0
    ax1 = plt.subplot(gs1[i])
    plt.axis('on')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.set_aspect('equal')

plt.show()