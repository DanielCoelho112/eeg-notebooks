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
time_begin = 5000
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
init_time = time.time()
begin = True
for image in color_images:

    if begin == True:
        now = time.time()
        while True:
            imshow_fullscreen ('screen', color_break)
            cv2.waitKey(1)
            now_begin = time.time()
            if (now_begin - now)>5:
                begin=False
                print('time during begin was {}'.format(now_begin-now))
                break

    # color
    now = time.time()
    while True:
        imshow_fullscreen ('screen', image)
        cv2.waitKey(1)
        now_color = time.time()
        if (now_color - now)>1:
            print('time during color image was {}'.format(now_color-now))
            break

    now = time.time()
    while True:
        imshow_fullscreen ('screen', color_break)
        cv2.waitKey(1)
        now_break = time.time()
        if (now_break - now)>2:
            print('time during break image was {}'.format(now_break-now))
            break

final_time = time.time()
elapsed_time = final_time-init_time
print('total time was {}'.format(elapsed_time))


