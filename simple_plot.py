#!/usr/bin/env python
#==========================================================#
#            Set Python Path
#==========================================================#
import pandas as pd                     # useful for tables of data
import numpy as np                      # useful for math
import matplotlib.pyplot as plt         # plot
from sys import argv                    # allows argument variable
from scipy import stats                # stats

# to run type
# $ python script_name data_file_name
script, data_file, xaxis, yaxis, plot_name= argv

#df_data = pd.read_csv(data_file, delim_whitespace=True, header=None, dtype=np.float64)
df_data = pd.read_csv(data_file, header=None, dtype=np.float64)

print 'here is the first few rows of the datafile'
print df_data.head()

x = df_data[0]
#print x

y = df_data[1]
#print y


plt.scatter(x,y)

#r-squared calculation
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
predict_y = intercept + slope * x

plt.plot(x,y,'go')
plt.plot(x, predict_y, 'k-')
plt.legend(('data', 'line-regression'), 'upper left')
plt.autoscale(True)


#linear regression line, trendline plot
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.legend(('data', 'line-regression'), 'upper left')
plt.autoscale(True)


plt.xlabel('%s'%xaxis)
plt.ylabel('%s'%yaxis)
plt.savefig('%s'%plot_name)
plt.close()

