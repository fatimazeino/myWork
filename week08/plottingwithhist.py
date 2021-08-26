# plottingwithplot.py
# this program plots a histogram of the salaries 
# Author: Fatima Zeino

import numpy as np 
import matplotlib.pyplot as plt

minsalary = 20000
maxsalary = 80000
numberofentries = 10

#np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, numberofentries)

plt.hist(salaries)
plt.show()