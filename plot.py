# data visualization
import re
import numpy as np
import matplotlib.pyplot as plt

x_data = []
y_data = []
file_name = input('File name without extension:')

file = open(file_name + '.xvg', 'r')

for line in file:
  # extract axis labels   
  line = line.strip( )
  if "xaxis" in line:
      xaxis = line.split("\"")[1]
  elif "yaxis" in line:
      if file_name.lower() not in line.split("\"")[1].lower():
        yaxis = file_name.capitalize() + " " + line.split("\"")[1]
      else:
        yaxis = line.split("\"")[1]  
  
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
