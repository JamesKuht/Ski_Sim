import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import config

#### Preparation ####

# For text formatting
class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

### This code calculates the number of lines in you csv file we can loop through them
file = open('ski_sim_data.csv', 'r')
reader = csv.reader(file)
lines = len(list(reader)) - 1
file.close()

csv_import = pd.read_csv('ski_sim_data.csv')

### Loop through every line of the csv outputting for each
for i in range(lines):
	data = {
		'leftSkiLeftSide':[csv_import['leftSkiFront'][i], csv_import['leftSkiLeft'][i], csv_import['leftSkiLeft'][i], csv_import['leftSkiRear'][i]],
		'leftSkiRightSide':[config.leftSkiFront, config.leftSkiRight, config.leftSkiRight, config.leftSkiRear],
		'gap':[0,0,0,0],
		'rightSkiLeftSide':[config.rightSkiFront, config.rightSkiLeft, config.rightSkiLeft, config.rightSkiRear],
		'rightSkiRightSide':[config.rightSkiFront, config.rightSkiRight, config.rightSkiRight, config.rightSkiRear]
	}

	df = pd.DataFrame(data=data)
	print(df)


#### Build the heatmap plot ####

fig, ax = plt.subplots()
cmap = mpl.cm.hot_r
norm = mpl.colors.Normalize(vmin=0, vmax=100)
heatplot = ax.imshow(df, cmap=cmap, norm=norm)
ax.set_title("Heatmap of pressure on your Skis")

# We want to show all ticks...
ax.set_xticks(np.arange(5))
ax.set_yticks(np.arange(4))

# add heatbar
cbar = fig.colorbar(heatplot, label='%weight on ski')
tick_spacing = 1

#### Offer advice on ski technique ####

# Front-back weighting sensing - ensure the skier has weight on front of skis
front_weight = config.leftSkiFront + config.rightSkiFront
rear_weight = config.leftSkiRear + config.rightSkiRear
frontback_percentage = int((rear_weight/(rear_weight + front_weight))*100)

ideal_frontback_percentage = 50

if frontback_percentage <= ideal_frontback_percentage:
	message1 = 'Your front-back weight distribution is spot-on'
else:
	message1 = '{}% of your weight is on the back of your skis, you\
 need to move your weight forward to make turning easier'.format(frontback_percentage)

print(color.BOLD + "*Front-back balance* " + color.END + message1)

# turning sensing of direction
leftSkiLeft = int((config.leftSkiLeft/(config.leftSkiRight + config.leftSkiLeft))*100)
rightSkiLeft = int((config.rightSkiLeft/(config.rightSkiRight + config.rightSkiLeft))*100)
leftSkiRight = int((config.leftSkiRight/(config.leftSkiRight + config.leftSkiLeft))*100)
rightSkiRight = int((config.rightSkiRight/(config.rightSkiRight + config.rightSkiLeft))*100)

# sensing of ski symmetry (i.e. if you're turning left are both of your skis matched?)
leftTurnRatio = int((config.rightSkiLeft/(config.leftSkiLeft + config.rightSkiLeft))*100)
rightTurnRatio = int((config.leftSkiRight/(config.leftSkiRight + config.rightSkiRight))*100)

turn_threshold = 55
ski_symmetry_upper_threshold = 52
ski_symmetry_lower_threshold = 48

# left turn
if rightSkiLeft > turn_threshold:
	if leftTurnRatio > ski_symmetry_upper_threshold:
		print(color.BOLD + "*Ski Angulation* " + color.END +\
		"You're not angulating your inside (left) ski enough, this will reduce the \
effectiveness of your turn")
	elif leftTurnRatio < ski_symmetry_lower_threshold:
		print(color.BOLD + "*Ski Angulation* " + color.END +\
		"You're angulating your inside (left) ski too much, this will reduce your \
balance during your turn")
	else:
		print(color.BOLD + "*Ski Angulation* " + color.END +\
		"Your ski angulation is good whilst turning left")

# right turn
if leftSkiRight > turn_threshold:
	if rightTurnRatio > ski_symmetry_upper_threshold:
		print(color.BOLD + "*Ski Angulation* " + color.END + "You're not angulating your\
		inside (right) ski enough, this will reduce the effectiveness of your turn")
	elif rightTurnRatio < ski_symmetry_lower_threshold:
		print(color.BOLD + "*Ski Angulation* " + color.END +\
		"You're angulating your inside (right) ski too much, this will reduce your \
balance during your turn")
	else:
		print(color.BOLD + "*Ski Angulation* " + color.END +\
		"Your side-to-side ski balance is good whilst turning right")

# Configuring & showing the graph
plt.axis('off')
plt.show()
