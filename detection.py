import naoqi
from PIL import Image
import time
import cv2
import numpy as np
from naoqi import ALProxy
import math
import Hand
IP = "169.254.199.42" 
PORT = 9559
flag=1
blockwidth = 4
tts = ALProxy("ALTextToSpeech", IP, PORT)

def getframe(IP,PORT):
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    resolution = 2   # VGA
    colorSpace = 11  # RGB
   
    camProxy.setParam(18, flag)
    videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
    # Get a camera image.
    t0 = time.time()
    # Time the image transfer.
    #print "acquisition delay ", t1 - t0
    naoImage = camProxy.getImageRemote(videoClient)
    t1 = time.time()
    camProxy.unsubscribe(videoClient)
    # Set the image size and pixel array.
    imageWidth = 640
    imageHeight = 480
    array = naoImage[6]
    # Create a PIL Image from our pixel array.
    im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
    ci = np.array(im)  
    r, g, b = cv2.split(ci) 
    ci = cv2.merge([b, g, r])
    return ci

def target(IP,PORT,LH,LS,LV,UH,US,UV):
    detection=0
    image=getframe(IP,PORT)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of green color in HSV
    #lower_green = np.array([50,55,5])
    #upper_green = np.array([105,255,255])
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])
    
    lower_colo = np.array([LH,LS,LV])
    upper_colo = np.array([UH,US,UV])
    mask = cv2.inRange(hsv, lower_colo, upper_colo)
    
    resf=cv2.medianBlur(mask,5)

    ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for i in range(len(contours)):
        area=cv2.contourArea(contours[i])
        d=cv2.minAreaRect(contours[i])
        cen=d[1]
        if d[1][1]>d[1][0]:
            a=d[1][1]
            b=d[1][0]
        else:
            a=d[1][0]
            b=d[1][1]
        if a!=0.0 and b!=0.0:
            if a/b>0.5 and a/b<5 and area>12000:
                detection=1
                print("area",area)
                tts.say("I see the brick")
                
    return detection

def check(IP,PORT,LH,LS,LV,UH,US,UV):
    detection=0
    image=getframe(IP,PORT)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of green color in HSV
    #lower_green = np.array([50,55,5])
    #upper_green = np.array([105,255,140])
    #mask = cv2.inRange(hsv, lower_green, upper_green)
    
    lower_colo = np.array([LH,LS,LV])
    upper_colo = np.array([UH,US,UV])
    mask = cv2.inRange(hsv, lower_colo, upper_colo)
    resf=cv2.medianBlur(mask,5)

    ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for i in range(len(contours)):
        area=cv2.contourArea(contours[i])
        d=cv2.minAreaRect(contours[i])
        cen=d[1]
        if  area>5000 and area<16000:
            detection=1
            print("area",area)
            tts.say("I see the brick")
    return detection

def getcenter(IP,PORT,LH,LS,LV,UH,US,UV):
    x=y=z=0
    detection=0
    image=getframe(IP,PORT)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #lower_green = np.array([50,55,5])
    #upper_green = np.array([105,255,140])
    #mask = cv2.inRange(hsv, lower_green, upper_green)

    lower_colo = np.array([LH,LS,LV])
    upper_colo = np.array([UH,US,UV])
    mask = cv2.inRange(hsv, lower_colo, upper_colo)
    resf=cv2.medianBlur(mask,5)

    ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for i in range(len(contours)):
        area=cv2.contourArea(contours[i])
        d=cv2.minAreaRect(contours[i])
        cen=d[1]
        if d[1][1]>d[1][0]:
            a=d[1][1]
            b=d[1][0]
        else:
            a=d[1][0]
            b=d[1][1]
        if a!=0.0 and b!=0.0:
            if a/b>0.6 and a/b<5 and area>12000:
                point=contours[i]
                detection=1
                
    if detection==1:
        c=cv2.moments(point)
        xf=c['m10']/c['m00']
        yf=c['m01']/c['m00']
        x=round(xf,2)
        y=round(yf,2)
    else:
        #tts.say("I can not see the green brick")
        print("error")

    return (x,y)


def hand(IP,PORT):
    findhand=0
    image=getframe(IP,PORT)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of green color in HSV
    lower_green = np.array([5,45,5])
    upper_green = np.array([12,255,255])
   
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    resf=cv2.medianBlur(mask,5)

    ret, binary = cv2.threshold(resf, 2, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for i in range(len(contours)):
        area=cv2.contourArea(contours[i])
        d=cv2.minAreaRect(contours[i])
        cen=d[1]
        a=d[1][1]
        b=d[1][0]
        if a!=0.0 and b!=0.0:
            if area>35000:
                findhand=1
                print("area",area)
                tts.say("I see your hand")
    return findhand

def recenter(IP,PORT,CK,Left_H,Right_H,x,y,LH,LS,LV,UH,US,UV):
    if CK==1:
        Hand.choose(IP,PORT,Left_H,Right_H)
        pick_flag=True
        again_flag=False
    else:
        nx,ny=getcenter(IP,PORT,LH,LS,LV,UH,US,UV)
        if nx<=x+25 and nx>=x-25 and ny<=y+25 and ny>=y-25:
            Hand.choose(IP,PORT,Left_H,Right_H)
            pick_flag=True
            again_flag=False
            print("step")
        else:
            pick_flag=False
            again_flag=True
            print("step2")
    return pick_flag,again_flag
    








