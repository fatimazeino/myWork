# plottingwithchart.py
# this program Makes a pie chart of list of counties.
# Author: Fatima Zeino

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import count
from numpy.lib.arraysetops import unique
from numpy.lib.utils import _lookfor_generate_cache

possiblecounties = ['mayo', 'galway', 'rosommon', 'dublin', 'donegal']
counties = np.random.choice(
    possiblecounties,
    p=[0.1,0.3,0.2,0.12,0.28],
    size=(100)
)
unique, counts =np.unique(counties, return_counts=True)
#plt.pie(counts, labels=unique)
plt.bar(unique,counts)
plt.show()