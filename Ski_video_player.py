import cv2
import time

### Function to play the ski video
def play_videoFile(filePath,mirror=False):
	cap = cv2.VideoCapture(filePath)
	cv2.namedWindow('Video of skiier', cv2.WINDOW_NORMAL)
	cv2.moveWindow('Video of skiier', 550, 30)
	while True:
		ret_val, frame = cap.read()

		if mirror:
			frame = cv2.flip(frame, 1)
		
		cv2.imshow('Video of skiier', frame)
		if cv2.waitKey(1) == 27:
			break # esc to quit
	cv2.destroyAllWindows

# The delay is simply to sync it up with the Ski_sim.py file
time.sleep(0.5)
play_videoFile('Ski_video.mp4')