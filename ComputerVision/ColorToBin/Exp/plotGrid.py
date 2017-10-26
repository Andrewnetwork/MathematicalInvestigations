import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8)) # Notice the equal aspect ratio
ax = [fig.add_subplot(2,2,i+1) for i in range(4)]

for a in ax:
    a.set_xticklabels([])
    a.set_yticklabels([])
    a.set_aspect('equal')

fig.subplots_adjust(wspace=0, hspace=0)

plt.show()