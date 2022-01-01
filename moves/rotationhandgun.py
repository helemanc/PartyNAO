
import sys

import motion

import almath

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

    # Moving

    ########## Arms ###########

    # Right Arm in "Posizione Iniziale Arms #1"

    # Left Arm in "Posizione Iniziale Arms #2"

    RShoulderPitch = 67.7

    RShoulderRoll = -26.4

    RElbowYaw = 90.9

    RElbowRoll = 88.5

    RWristYaw = 80

    RHand = 0.35

    LShoulderPitch = 78.0

    LShoulderRoll = 16.6

    LElbowYaw = -68.3

    LElbowRoll = -49.2

    LWristYaw = 4.3

    LHand = 0.0



    names = "LArm"

    angleLists = [ LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                   LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD ]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)



    names = "RArm"

    angleLists = [ RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                   RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD ]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)



    #time.sleep(0.02)



    # Open RHand
    RHandAngle = 0.90
    
    names = "RHand"
    angleLists = [ RHandAngle ]
    timeLists = 0.5
    motionProxy.angleInterpolation(names, angleLists, timeLists, True)
    
    # NAO:
    #ttsProxy.say("Inserisci il ventaglio nella mano per favore")
    
    #time.sleep(1)
    
    # NAO:
    #ttsProxy.say("Grazie")
    
    # Close RHand
    names = "RHand"
    timeLists = 0.5
    RHandAngle = 0.05
    angleLists = [ RHandAngle ]
    motionProxy.angleInterpolation(names, angleLists, timeLists, True)
    
    # Ruoto ventaglio
    RShoulderPitch = 67.7
    RShoulderRoll = -26.4
    RElbowYaw = 90.9
    RElbowRoll = 88.5
    RWristYaw = 60
    RHand = 0.10







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


