from matplotlib import pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow=True,
            explode=(0,0.2,0.3,0),
            autopct='%1.1f%%')

plt.title("Epic info")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.show()

