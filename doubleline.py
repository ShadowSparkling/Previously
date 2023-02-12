from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x = [1,2,3,4,7]
y = [1,2,3,7,5]

x1 = [0,1,2,4,7]
y1 = [5,4,3,2,8]

plt.plot(x,y,'g',label='line one',linewidth = 5)
plt.plot(x1,y1,'b',label='line two',linewidth = 5)

plt.title("Epic info")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.grid(True,color='k')
plt.show()

