from matplotlib import pyplot as plt
days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,5,8]
working = [7,5,3,7,9]
playing = [4,6,8,2,9]

plt.plot([],[],color='m',label = 'Sleeping',linewidth=5)
plt.plot([],[],color='c',label = 'Eating',linewidth=5)
plt.plot([],[],color='y',label = 'Working',linewidth=5)
plt.plot([],[],color='k',label = 'Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','y','k'])

plt.title("Epic info")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.show()