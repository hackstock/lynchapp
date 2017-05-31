import cv2
import os
video = cv2.VideoCapture('./video/movie.mp4')
image_count = 0
os.mkdir('frames')

while True:
    success, frame = video.read()
    if not success:
        break
    cv2.imwrite(os.path.join('frames',"frame_{:d}.jpg".format(image_count)), frame)
    image_count += 1

