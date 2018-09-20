# Cooperative-Robot-Nao
Project by Dinghuang Zhang
Hardware settings
Place the robot and the box, distance between robot and box is 8cm, and the high is same as robot foundation about waist.
Software settings
1.	Power on robot and press chest button then wait for 3 minuets until robot say something.
2.	Open the folder named NaoMK7 this is the final vision of the code. Which include.
3.	If more key word need add to project please find the library in speech.py 

App.py	Start program and set target color, if the surrounding light change, change the color threshold here.
Main.py	Picking process combine vision recognition.
Detection.py	Vision recognition for target hand and center point
Speech.py	Speech recognition 
MoveArm.py	Location check and move arm according to Arm.py
Hand.py	Choose hand to pick and hold
Arm.py	Inverse kinematic values

And all the code is available in Google Drive at https://drive.google.com/open?id=1B2eXUXg5A04eGfd2kP-wmQQk89akots0
