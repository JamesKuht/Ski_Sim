# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as mpl

# Create a pandas dataframe which has all of the sensor data in it, normalised to 100
leftSkiFront = 40
leftSkiLeft = 37
leftSkiRight = 63
leftSkiRear = 60
rightSkiFront = 41
rightSkiLeft = 45
rightSkiRight = 55
rightSkiRear = 59

data = {
	'leftSkiLeftSide':[leftSkiFront, leftSkiLeft, leftSkiLeft, leftSkiRear],
	'leftSkiRightSide':[leftSkiFront, leftSkiRight, leftSkiRight, leftSkiRear],
	'gap':[0,0,0,0],
	'rightSkiLeftSide':[rightSkiFront, rightSkiLeft, rightSkiLeft, rightSkiRear],
	'rightSkiRightSide':[rightSkiFront, rightSkiRight, rightSkiRight, rightSkiRear]
}

df = pd.DataFrame(data=data)

#### Build the heatmap plot - this website should help: \
#### https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

fig, ax = plt.subplots()
cmap = mpl.cm.hot_r
norm = mpl.colors.Normalize(vmin=0, vmax=100)
heatplot = ax.imshow(df, cmap=cmap, norm=norm)
ax.set_title("Heatmap of pressure on your Skis")

# We want to show all ticks...
ax.set_xticks(np.arange(5))
ax.set_yticks(np.arange(4))

# ... and label them with the respective list entries
#ax.set_xticklabels(['       Left','Ski       ','','       Right', 'Ski       '])
#ax.set_yticklabels(['Front','Middle','Middle','Rear'])

# add heatbar
cbar = fig.colorbar(heatplot, label='%weight on ski')
tick_spacing = 1

# Configuring the graph
plt.axis('off')

plt.show()
