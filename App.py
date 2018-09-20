# -*- coding: utf-8 -*-
import naoqi
from naoqi import ALProxy
import time
import main
import speech
import Arm

IP = "169.254.199.42" 
PORT = 9559
tts = ALProxy("ALTextToSpeech", IP, PORT)

while True:
    colour=speech.colour(IP,PORT)
    if colour=='Green':
        LH,LS,LV=50,55,5
        UH,US,UV=105,255,255
        finish_flag=main.main(IP,PORT,LH,LS,LV,UH,US,UV)
    elif colour=='Blue':
        LH,LS,LV=107,50,50
        UH,US,UV=130,255,255
        finish_flag=main.main(IP,PORT,LH,LS,LV,UH,US,UV)
        if finish_flag==True:
            tts.say("I will pick next one")
            continue
        

