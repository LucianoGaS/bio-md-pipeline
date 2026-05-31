# data visualization
import re
import numpy as np
import matplotlib.pyplot as plt

x_data = []
y_data = []
file = open('temperature.xvg', 'r')

for line in file:
  # extract axis labels   
  line = line.strip( )
  if "xaxis" in line:
      xaxis = line.split("\"")[1]
  elif "yaxis" in line:
      yaxis = "Temperature " + line.split("\"")[1]          
  
  # store data values for the axes
  "\"".join(line)
  if not line.startswith(('#','@')):
      x_data.append(float(re.split("\s+", line)[0]))
      y_data.append(float(re.split("\s+", line)[1]))

#graph
plt.plot(x_data, y_data)
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.show()
