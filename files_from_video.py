# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
video_path = "AV_test1.mp4"
cam = cv2.VideoCapture(video_path)

# the path we want to store the images
image_path = 'images'
try:
	# creating a folder named images
	if not os.path.exists(image_path):
		os.makedirs(image_path)
# if not created then raise error
except OSError:
	print(f'Error creating {image_path}/ directory')

# frame in the video we are looking at
current_frame = 0
while True:
	# reading from frame
	# ret is False if no frames left
	ret, frame = cam.read()

	if ret:
		# if video is still left continue creating images
		name =f'{image_path}/frame_{current_frame:05}.jpg'
		print(f'Creating {name}')

		# writing the extracted images
		cv2.imwrite(name, frame)

		# increasing counter so that it will
		# show how many frames are created
		current_frame += 1
	else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
