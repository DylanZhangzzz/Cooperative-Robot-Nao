# -*- coding: utf-8 -*-
import math
import naoqi
import numpy
import cv2
from naoqi import ALProxy
import Arm
import time
import MoveArm
#IP = "169.254.67.145"
IP = "169.254.199.42" 
PORT = 9559

proxy = ALProxy("ALMotion",IP,PORT)
names = "Body"
stiffness = 1.0
proxy.stiffnessInterpolation(names, stiffness, 1.0)
proxy.setAngles("HeadPitch",0.157,0.2)

def choose(IP,PORT,LH,RH):
    if LH==1:
        proxy.setAngles("LHand",0.25,0.2)
        time.sleep(0.5)
        Arm.Left_Arm(IP,PORT)
        time.sleep(0.5)
        pick_flag=True
    elif RH==1:
        proxy.setAngles("RHand",0.25,0.2)
        time.sleep(0.5)
        Arm.Right_Arm(IP,PORT)
        time.sleep(0.5)
        pick_flag=True
    else:
        pick_flag=False
    return pick_flag
