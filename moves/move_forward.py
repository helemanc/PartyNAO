''' NAO fa 3 passi in avanti '''

import sys

import motion

import almath

import math

import time

from naoqi import ALProxy



#def StiffnessOn(proxy):
#    # We use the "Body" name to signify the collection of all joints
#    pNames = "Body"
#    pStiffnessLists = 1.0
#    pTimeLists = 1.0
#    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP, port):



    # Init proxies.

    try:

        motionProxy = ALProxy("ALMotion", robotIP, port)

    except Exception, e:

        print "Could not create proxy to ALMotion"

        print "Error was: ", e



    try:

        postureProxy = ALProxy("ALRobotPosture", robotIP, port)

    except Exception, e:

        print "Could not create proxy to ALRobotPosture"

        print "Error was: ", e

    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e


# Set NAO in Stiffness On
#    StiffnessOn(motionProxy)

    # NAO:
    #ttsProxy.say("Faccio tre passi in avanti")
    #time.sleep(1)



    # Set NAO in Stiffness On

#    StiffnessOn(motionProxy)

    distance_x_m=0.08
    distance_y_m=0.0
    theta_deg=0.0
    # The command position estimation will be set to the sensor position when the robot starts moving, so we use sensors first and commands later.
    initPosition = almath.Pose2D(motionProxy.getRobotPosition(True))
    targetDistance = almath.Pose2D(distance_x_m, distance_y_m, theta_deg * almath.PI / 180)
    expectedEndPosition = initPosition * targetDistance
    enableArms = 0
    motionProxy.setMoveArmsEnabled(enableArms, enableArms)
    motionProxy.moveTo(distance_x_m, distance_y_m,theta_deg)





    

if __name__ == "__main__":

    robotIP = "127.0.0.1" #"192.168.1.11"

    port = 61476 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)

