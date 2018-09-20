# -*- coding: utf-8 -*-
import math
import naoqi
import numpy
import cv2
import detection
from naoqi import ALProxy
import Arm
import time
import MoveArm
import Hand
IP = "169.254.199.42" 
PORT = 9559
tts = ALProxy("ALTextToSpeech", IP, PORT)
motion= ALProxy("ALMotion", IP, PORT)
motion.wakeUp()

proxy = ALProxy("ALMotion",IP,PORT)

names = "Body"
stiffness = 1.0
proxy.stiffnessInterpolation(names, stiffness, 1.0)
proxy.setAngles("HeadPitch",0.157,0.2)
Arm.Reset(IP,PORT)



def main(IP,PORT,LH,LS,LV,UH,US,UV):
    finish=False
    Arm.Reset(IP,PORT)
    Hand_flag=False
    break_all=False
    again_flag=False
    Right_H=0
    Left_H=0
    tts.say("I am waiting!")
    target=detection.target(IP,PORT,LH,LS,LV,UH,US,UV)
    print ("target",target)
    
    while target==1:# main loop
        x,y=detection.getcenter(IP,PORT,LH,LS,LV,UH,US,UV)#
        Left_H,Right_H=MoveArm.movement(IP,PORT,x,y)
        print Left_H,Right_H
        time.sleep(1)
        Hand_flag = True
        if Hand_flag==True:
            target_hand=0
            pick_flag=False
            CK=detection.check(IP,PORT,LH,LS,LV,UH,US,UV)
            print("check",CK)
            pick_flag,again_flag=detection.recenter(IP,PORT,CK,Left_H,Right_H,x,y,LH,LS,LV,UH,US,UV)
            print pick_flag,again_flag
        if again_flag==True:# try again
            continue           
        while pick_flag==True:
            target_hand=detection.hand(IP,PORT)
            print("hand",target_hand)
            if target_hand==1:
                tts.say("I will relesae it")
                while Right_H==1:
                    proxy.setAngles("RHand",1,0.2)
                    proxy.setAngles("RShoulderPitch",-0.087,0.2)
                    tts.say("I finish the job")
                    Arm.Reset(IP,PORT)
                    Right_H=0
                    pick_flag=False
                    target=0
                    finish=True
                    continue
                    
                while Left_H==1:
                    proxy.setAngles("LHand",1,0.2)
                    proxy.setAngles("LShoulderPitch",-0.087,0.2)
                    tts.say("I finish the job")
                    Arm.Reset(IP,PORT)
                    Left_H=0
                    pick_flag=False
                    target=0
                    finish=True
                    continue
        
        return finish
                    
          
            


        
