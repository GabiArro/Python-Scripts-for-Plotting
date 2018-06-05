#!/usr/bin/env python
#==========================================================#
#            Set Python Path
#==========================================================#
import pandas as pd                     # useful for tables of data
import numpy as np                      # useful for math
import matplotlib.pyplot as plt         # plot
from sys import argv                    # allows argument variable

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

x_2 = df_data[2]
#print x

y_2 = df_data[3]
#print y'

x_3 = df_data[4]
#print x

y_3 = df_data[5]
#print y'

x_4 = df_data[6]
#print x

y_4 = df_data[7]
#print y'

x_5 = df_data[8]
#print x

y_5 = df_data[9]
#print y'

x_6 = df_data[10]
#print x

y_6 = df_data[11]
#print y'

x_7 = df_data[12]
#print x

y_7 = df_data[13]
#print y'


plt.plot(x,y, label='700ppm')
plt.plot(x_2,y_2, label='200ppm')
plt.plot(x_3,y_3, label='500pm')
plt.plot(x_4,y_4, label='554ppm')
plt.plot(x_5,y_5, label='300ppm')
plt.plot(x_6,y_6, label='400ppm')
plt.plot(x_7,y_7, label='600ppm')


plt.legend()
plt.subplots_adjust()
plt.subplots_adjust(bottom=0.2) # <-- Change the 0.02 to work for your plot.
plt.legend(loc=9, bbox_to_anchor=(0.5,-0.1),
           fancybox=True, shadow=True, ncol=4)


plt.xlabel('%s'%xaxis)
plt.ylabel('%s'%yaxis)
plt.savefig('%s'%plot_name)
plt.close()

