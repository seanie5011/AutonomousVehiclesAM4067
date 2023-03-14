# importing libraries
import os
import cv2
from PIL import Image

# Folder which contains all the images
# from which video is to be generated
images_path = os.getcwd() + '//AV_test2_images'
os.listdir(images_path)

# name of video to make
video_name = 'AV_test2_video.mp4'
# frames per second
fps = 30

# get all images
images = list(os.listdir(images_path))

# setting the frame width and frame height
# to the width and height of first image
frame = cv2.imread(images_path + '//' + images[0])
height, width, layers = frame.shape

# create the writer
video = cv2.VideoWriter(video_name, 0, fps, (width, height))

# Appending the images to the video one by one
for image in images:
	frame = cv2.imread(images_path + '//' + image)
	video.write(frame)

# Release all space and windows once done
video.release()
cv2.destroyAllWindows()