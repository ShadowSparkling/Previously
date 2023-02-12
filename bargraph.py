from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[2,4,6,8,10],label="Example One", color = 'b')
plt.bar([2,4,6,8,10],[3,4,5,6,8],label="Example Two",color = 'g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')


plt.title('Info')

plt.show()




