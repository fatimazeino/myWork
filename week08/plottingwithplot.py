# plottingwithplot.py
# this program plots the function y = x2 ,
# makes a list that has, the same number random values as salaries and Makes scatter plot of this data.
# Author: Fatima Zeino


import numpy as np 
import matplotlib.pyplot as plt

minsalary = 20000
maxsalary = 80000
numberofentries = 10

np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, numberofentries)
ages = np.random.randint(low =21, high=65, size=numberofentries)

plt.scatter(ages, salaries, label="salaries")
#plt.show()

xpoint = np.array(range(1,101))
ypoint = xpoint * xpoint

plt.plot(xpoint, ypoint, color='r', label="x squared")

plt.title("random plot")
plt.xlabel("Salaires")
plt.ylabel("Äges")
plt.legend()
#plt.show()
plt.savefig('prettier-plot.png')

