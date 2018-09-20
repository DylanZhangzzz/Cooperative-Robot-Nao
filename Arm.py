from naoqi import ALProxy
import time
#IP="169.254.67.145"
IP = "169.254.199.42" 
PORT=9559
proxy = ALProxy("ALMotion",IP,PORT)
names = "Body"
stiffness = 1.0
proxy.stiffnessInterpolation(names, stiffness, 1.0)
#proxy.setAngles("HeadPitch",0.157,0.2)


def Reset(IP,PORT):
    proxy.setAngles("RShoulderPitch",0.42,0.2)
    proxy.setAngles("RShoulderRoll",-0.8,0.2)
    proxy.setAngles("RElbowYaw",0.16,0.2)
    proxy.setAngles("RElbowRoll",0.94,0.2)
    proxy.setAngles("RWristYaw",1.33,0.2)

    proxy.setAngles("LShoulderPitch",0.37,0.2)
    proxy.setAngles("LShoulderRoll",0.8,0.2)
    proxy.setAngles("LElbowYaw",-0.16,0.2)
    proxy.setAngles("LElbowRoll",-0.94,0.2)
    proxy.setAngles("LWristYaw",-1.33,0.2)
    
    proxy.setAngles("RHand",1,0.2)
    proxy.setAngles("LHand",1,0.2)


def B1(IP,PORT):
    proxy.setAngles("LShoulderPitch",0.38,0.2)
    proxy.setAngles("LShoulderRoll",0.1,0.2)
    proxy.setAngles("LElbowYaw",-0.4,0.2)
    proxy.setAngles("LElbowRoll",-0.56,0.2)
    proxy.setAngles("LWristYaw",-1.22,0.2)

def B2(IP,PORT):
    proxy.setAngles("LShoulderPitch",0.35,0.2)
    proxy.setAngles("LShoulderRoll",-0.15,0.2)
    proxy.setAngles("LElbowYaw",-0.3,0.2)
    proxy.setAngles("LElbowRoll",-0.4,0.2)
    proxy.setAngles("LWristYaw",-1.3,0.2)

def B3(IP,PORT):
    proxy.setAngles("RShoulderPitch",0.38,0.2)
    proxy.setAngles("RShoulderRoll",0.15,0.2)
    proxy.setAngles("RElbowYaw",0.3,0.2)
    proxy.setAngles("RElbowRoll",0.4,0.2)
    proxy.setAngles("RWristYaw",1.3,0.2)

def B4(IP,PORT):
    proxy.setAngles("RShoulderPitch",0.4,0.2)
    proxy.setAngles("RShoulderRoll",-0.14,0.2)
    proxy.setAngles("RElbowYaw",0.3211,0.2)
    proxy.setAngles("RElbowRoll",0.6981,0.2)
    proxy.setAngles("RWristYaw",1.22,0.2)

def C1(IP,PORT):
    proxy.setAngles("LShoulderRoll",0.31,0.2)
    proxy.setAngles("LShoulderPitch",0.31,0.2)
    proxy.setAngles("LElbowYaw",0,0.2)
    proxy.setAngles("LElbowRoll",-0.98,0.2)
    proxy.setAngles("LWristYaw",-1.48,0.2)

def C2(IP,PORT):
    proxy.setAngles("LShoulderPitch",0.31,0.2)
    proxy.setAngles("LShoulderRoll",0.09,0.2)
    proxy.setAngles("LElbowYaw",-0.05,0.2)
    proxy.setAngles("LElbowRoll",-0.9,0.2)
    proxy.setAngles("LWristYaw",-1.48,0.2)

def C3(IP,PORT):
    proxy.setAngles("RShoulderPitch",0.35,0.2)
    proxy.setAngles("RShoulderRoll",-0.09,0.2)
    proxy.setAngles("RElbowYaw",0.05,0.2)
    proxy.setAngles("RElbowRoll",0.9,0.2)
    proxy.setAngles("RWristYaw",1.48,0.2)

def C4(IP,PORT):
    proxy.setAngles("RShoulderPitch",0.4,0.2)
    proxy.setAngles("RShoulderRoll",-0.3,0.2)
    proxy.setAngles("RElbowYaw",0.0802,0.2)
    proxy.setAngles("RElbowRoll",0.98,0.2)
    proxy.setAngles("RWristYaw",1.48,0.2)

def D1(IP,PORT):
    proxy.setAngles("LShoulderPitch",0.4,0.2)
    proxy.setAngles("LShoulderRoll",0.46,0.2)
    proxy.setAngles("LElbowYaw",-0.082,0.2)
    proxy.setAngles("LElbowRoll",-1.29,0.2)
    proxy.setAngles("LWristYaw",-1.31,0.2)

def D2(IP,PORT):
    proxy.setAngles("LShoulderPitch",0.4,0.2)
    proxy.setAngles("LShoulderRoll",0.18,0.2)
    proxy.setAngles("LElbowYaw",-0.08,0.2)
    proxy.setAngles("LElbowRoll",-1.22,0.2)
    proxy.setAngles("LWristYaw",-1.3,0.2)

def D3(IP,PORT):
    proxy.setAngles("RShoulderPitch",0.438,0.2)
    proxy.setAngles("RShoulderRoll",-0.1833,0.2)
    proxy.setAngles("RElbowYaw",0.0820,0.2)
    proxy.setAngles("RElbowRoll",1.22,0.2)
    proxy.setAngles("RWristYaw",1.2985,0.2)

def D4(IP,PORT):
    proxy.setAngles("RShoulderPitch",0.44,0.2)
    proxy.setAngles("RShoulderRoll",-0.4381,0.2)
    proxy.setAngles("RElbowYaw",0.0820,0.2)
    proxy.setAngles("RElbowRoll",1.2898,0.2)
    proxy.setAngles("RWristYaw",1.3107,0.2)

## hold it
def Left_Arm(IP,PORT):
    proxy.setAngles("LShoulderPitch",-0.4189,0.2)
    proxy.setAngles("LShoulderRoll",-0.3142,0.2)
    proxy.setAngles("LElbowYaw",0.6283,0.2)
    proxy.setAngles("LElbowRoll",-0.349,0.2)
    proxy.setAngles("LWristYaw",-0.978,0.2)

def Right_Arm(IP,PORT):
    proxy.setAngles("RShoulderPitch",-0.4189,0.2)
    proxy.setAngles("RShoulderRoll",0.3142,0.2)
    proxy.setAngles("RElbowYaw",-0.349,0.2)
    proxy.setAngles("RElbowRoll",0.349,0.2)
    proxy.setAngles("RWristYaw",0.978,0.2)
