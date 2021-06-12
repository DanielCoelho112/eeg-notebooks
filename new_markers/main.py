import cv2
from os import listdir
from os.path import isfile, join
import time

mypath='markers/'

# function to display a fullscreen image
def imshow_fullscreen (winname, img):
    cv2.namedWindow (winname, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty (winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow (winname, img)


# get image names into a list
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
names_colors = sorted(onlyfiles)
name_image_break = names_colors.pop(-1)

# time in miliseconds
time_color = 1000
time_break = 2000

# cicle to show fullscreen imagens with the right times



color_images = []
for name_color in names_colors:
    color_images.append(cv2.imread(mypath+name_color))
color_break = cv2.imread(mypath+name_image_break)
    
#imshow_fullscreen ('screen', color_break)
#cv2.waitKey(0)



print("Press ENTER to begin")
input()

for image in color_images:
    # color
    now = time.time()
    imshow_fullscreen ('screen', image)
    cv2.waitKey(time_color)
    now2 = time.time()
    print('time during color image was {}'.format(now2-now))

    # break
    imshow_fullscreen ('screen', color_break)
    key = cv2.waitKey(time_break)
    print('time during break image was {}'.format(time.time()-now2))

    if key == 27:#if ESC is pressed, exit loop
        cv2.destroyAllWindows()
        break

