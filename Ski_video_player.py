import cv2
import time

### Play the ski video
def play_videoFile(filePath,mirror=False):
	cap = cv2.VideoCapture(filePath)
	cv2.namedWindow('Video of skiier', cv2.WINDOW_AUTOSIZE)
	while True:
		ret_val, frame = cap.read()

		if mirror:
			frame = cv2.flip(frame, 1)
		
		cv2.imshow('Video of skiier', frame)
		if cv2.waitKey(1) == 27:
			break # esc to quit
	cv2.destroyAllWindows

time.sleep(0.5)
play_videoFile('Ski_video.mp4')