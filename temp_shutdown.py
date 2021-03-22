import sys
import cv2
import numpy as np
import time
import subprocess

exposure = 160
gain = 0
expLimTrig = False

def set_quality(level):
	global exposure
	global gain
	print("level: ---------------{}".format(level))
	print("Exposure:-------------{}".format(exposure))
	print("Gain:-----------------{}".format(gain))

        if(exposure > 30000):
            expLimTrig = True
            exposure=30160
        else:
            expLimTrig = False
	    if(level < 0.35):
            if (expLimTrig == False):
	            if(level < 0.1):
                    exposure += 6000
                exposure += 2000
            else:
                if(gain < 390):
                    gain+=20
        elif (level > 0.55):
            gain = 0
            if(level > 0.9):
                exposure = 2160
            exposure -= 2000

	subprocess.call(['v4l2-ctl -d /dev/video0 -c sensor_mode=2 -c exposure={} -c gain={}'.format(exposure, gain)],shell=True)

def calculate_brightness(image):
    histogram = cv2.calcHist([image],[0],None,[256],[0,256])
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale


if __name__ == '__main__':
	#reset camera value to default
	while True:
		subprocess.call(['watch -n 10 sensors >> /home/user/temp_hist.txt'],shell=True)
        
		key=cv2.waitKey(10)
	    	if key == 27: # Check for ESC key
	                print("Escape")
	        	break;	
		
cv2.destroyAllWindows()
	
