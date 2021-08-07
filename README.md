# Ski Simulator Tutorial System
#### Video Demo: https://youtu.be/qPGKIj_S5Z8
#### Description: A program to create a heatmap showing your positioning on skis, and offering you helpful feedback to improve your technique.

V simple file structure:
1. Ski_sim.py is the python file which does everything,
2. Config.py create the variables & writes them to a csv file. It also contains some example data for different turns which you can use to test the program.
3. ski_sim_data.csv is the csv file
4. Ski_video_player.py is the python file which uses openCV to play the video 'Ski_video.mp4
5. Ski_video.mp4 is a video which is loosely synced to some data in ski_sim_data.csv to illustrate how the heatmap and tutorial suggestions might change during use of the ski simulator


How to run the program:
1. First you need to create some data - do this by running 'config.py' (adjust the settings in config.py to suit the data you'd like to create)
2. You'll then notice that ski_sim_data.csv is populated with some example data
3. To then show the heatmap with the data, run Ski_sim.py
4. If you'd like the heatmap to show in sync with an example video, run both Ski_sim.py & Ski_video_player.py ( you can do this by writing:
'$ python Ski_sim.py & Ski_video_player.py &' into the terminal)
5. Exit the program by pressing 'control-c'

Versions of packages:
* Python 3.7.6 64-bit base:conda
* Matplotlib (this is crucial or it segfaults - to update all anaconda write'>> conda update --all') 3.4.2
* opencv-python (cv2) 4.5.3.56
* numpy 1.20.3
* pandas 1.3.1


