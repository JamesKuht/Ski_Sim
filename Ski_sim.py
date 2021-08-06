import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import csv
import time
import config

#### Preparation ####

# For text formatting
class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

###Functions
## A function to offer tutoring on front-rear weight balance
def skiTutorFR(lFront, lRear, rFront, rRear):
	front_weight = lFront + rFront
	rear_weight = lRear + rRear
	frontback_percentage = int((rear_weight/(rear_weight + front_weight))*100)

	ideal_frontback_percentage = 50
	if frontback_percentage <= ideal_frontback_percentage:
		message1 = 'Your front-back weight distribution is spot-on'
	else:
		message1 = '{}% of your weight is on the back of your skis, you \
need to move your weight forward to make turning easier'.format(frontback_percentage)
	return message1

### A function to offer tutoring on left-right angulation balance
def skiTutorLR(lLeft, lRight, rLeft, rRight):
	message2 = ""
	# normalizing ratios to be value out of 100 (not required if synthetic data like I have)
	leftSkiLeftNorm = int((lLeft/(lRight + lLeft))*100)
	rightSkiLeftNorm = int((rLeft/(rRight + rLeft))*100)
	leftSkiRightNorm = int((lRight/(lRight + lLeft))*100)
	print("leftSkiRightNorm is: " + str(leftSkiRightNorm))
	rightSkiRightNorm = int((rRight/(rRight + rLeft))*100)

	# sensing of ski symmetry (i.e. if you're turning left are both of your skis matched?)
	leftTurnRatio = int((rLeft/(lLeft + rLeft))*100)
	rightTurnRatio = int((lRight/(lRight + rRight))*100)
	print("rightTurnRatio is: " + str(rightTurnRatio))
	turn_threshold = 55
	ski_symmetry_upper_threshold = 52
	ski_symmetry_lower_threshold = 48

	# left turn
	if rightSkiLeftNorm > turn_threshold:
		if leftTurnRatio > ski_symmetry_upper_threshold:
			message2 = "*Ski Angulation* You're not angulating your inside (left) ski enough, this will reduce the \
effectiveness of your turn"
		elif leftTurnRatio < ski_symmetry_lower_threshold:
			message2 = "*Ski Angulation* You're angulating your inside (left) ski too much, this will reduce your \
balance during your turn"
		else:
			message2 = "Your ski angulation is good whilst turning left"

	# right turn
	if leftSkiRightNorm > turn_threshold:
		if rightTurnRatio > ski_symmetry_upper_threshold:
			message2 = "*Ski Angulation* You're not angulating your \
inside (right) ski enough, this will reduce the effectiveness of your turn"
		elif rightTurnRatio < ski_symmetry_lower_threshold:
			message2 = "*Ski Angulation* You're angulating your inside (right) ski too much, this will reduce your \
balance during your turn"
		else:
			message2 = "*Ski Angulation* Your side-to-side ski balance is good whilst turning right"
	return message2

### This code calculates the number of lines in you csv file we can loop through them
file = open('ski_sim_data.csv', 'r')
reader = csv.reader(file)
lines = len(list(reader)) - 1
file.close()

csv_import = pd.read_csv('ski_sim_data.csv')

### Loop through every line of the csv outputting for each
for i in range(lines):
	leftSkiFront, leftSkiLeft, leftSkiRight, leftSkiRear, rightSkiFront, rightSkiLeft, rightSkiRight, rightSkiRear = csv_import['leftSkiFront'][i], csv_import['leftSkiLeft'][i], csv_import['leftSkiRight'][i], csv_import['leftSkiRear'][i], csv_import['rightSkiFront'][i], csv_import['rightSkiLeft'][i], csv_import['rightSkiRight'][i], csv_import['rightSkiRear'][i]
	data = {
		'leftSkiLeftSide':[leftSkiFront, leftSkiLeft, leftSkiLeft, leftSkiRear],
		'leftSkiRightSide':[leftSkiFront, leftSkiRight, leftSkiRight, leftSkiRear],
		'gap':[0,0,0,0],
		'rightSkiLeftSide':[rightSkiFront, rightSkiLeft, rightSkiLeft, rightSkiRear],
		'rightSkiRightSide':[rightSkiFront, rightSkiRight, rightSkiRight, rightSkiRear]
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
	frontRearAdvice = skiTutorFR(leftSkiFront, leftSkiRear, rightSkiFront, rightSkiRear)
	print(frontRearAdvice)

	# Turning advice
	turningAdvice = skiTutorLR(leftSkiLeft,leftSkiRight, rightSkiLeft, rightSkiRight)
	print(turningAdvice)

	# Configuring & showing the graph
	plt.axis('off')
	plt.show()
	time.sleep(0.5)