import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

#### Preparation ####

# For text formatting
class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Ideally all sensor data would be normalised to an int within a range 0-100
leftSkiFront = 40
leftSkiLeft = 37
leftSkiRight = 63
leftSkiRear = 60
rightSkiFront = 41
rightSkiLeft = 45
rightSkiRight = 55
rightSkiRear = 59

# Pop the data into a pandas dataframe for speed/ease of heatmap creation
data = {
	'leftSkiLeftSide':[leftSkiFront, leftSkiLeft, leftSkiLeft, leftSkiRear],
	'leftSkiRightSide':[leftSkiFront, leftSkiRight, leftSkiRight, leftSkiRear],
	'gap':[0,0,0,0],
	'rightSkiLeftSide':[rightSkiFront, rightSkiLeft, rightSkiLeft, rightSkiRear],
	'rightSkiRightSide':[rightSkiFront, rightSkiRight, rightSkiRight, rightSkiRear]
}

df = pd.DataFrame(data=data)


#### Build the heatmap plot ####

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

# Configuring & showing the graph
plt.axis('off')
plt.show()


#### Offer advice on ski technique ####

# Front-back weighting sensing - ensure the skier has weight on front of skis
front_weight = leftSkiFront + rightSkiFront
rear_weight = leftSkiRear + rightSkiRear
frontback_percentage = int((rear_weight/(rear_weight + front_weight))*100)

ideal_frontback_percentage = 50

if frontback_percentage <= ideal_frontback_percentage:
	message1 = 'Your front-back weight distribution is spot-on'
else:
	message1 = '{}% of your weight is on the back of your skis, you\
 need to move your weight forward to make turning easier'.format(frontback_percentage)

print(color.BOLD + "*Front-back balance* " + color.END + message1)

# turning sensing of direction
leftSkiLeft = int((leftSkiLeft/(leftSkiRight + leftSkiLeft))*100)
rightSkiLeft = int((rightSkiLeft/(rightSkiRight + rightSkiLeft))*100)
leftSkiRight = int((leftSkiRight/(leftSkiRight + leftSkiLeft))*100)
rightSkiRight = int((rightSkiRight/(rightSkiRight + rightSkiLeft))*100)

# sensing of ski symmetry (i.e. if you're turning left are both of your skis matched?)
leftTurnRatio = int((rightSkiLeft/(leftSkiLeft + rightSkiLeft))*100)
rightTurnRatio = int((leftSkiRight/(leftSkiRight + rightSkiRight))*100)

turn_threshold = 55
ski_symmetry_upper_threshold = 53
ski_symmetry_lower_threshold = 47

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

