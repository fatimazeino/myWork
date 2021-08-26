# numpylist.py
# this program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000)
# Author: Fatima Zeino

import numpy as np

minsalary = 20000
maxsalary = 80000
numberofentries = 10

#np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, numberofentries)
print (salaries)

salariesplus = salaries + 5000
print (salariesplus)

salariesmult = salaries * 1.05
print (salariesmult)

newsalaries = salariesmult.astype(int)
print (newsalaries)