import matplotlib.pyplot as plt

population_ages=[23,32,22,54,54,76,46,34,76,98,39,54,76,64,63,17,9,94,43,24,46,84,34]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('Ae difference')
plt.ylabel('No. of people')
plt.title("Histogram")
plt.legend()
plt.show()


