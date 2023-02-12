from matplotlib import pyplot as plt
 
x = [1,5,3,4,5,6,7,8]
y = [2,3,4,5,6,7,8,1]
plt.scatter(x,y,label="skitscat",color='r',s=25,marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Scatter Plot")
plt.legend()
plt.show()



