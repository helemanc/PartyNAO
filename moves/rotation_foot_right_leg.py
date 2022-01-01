''' Rotazione piede RLeg e ritorno in posizione:

    NAO senza staccare i piedi da terra ruota internamente

    RLeg, attende qualche secondo,e poi lo ruota nuovamente

    per tornare alla posizione di partenza '''



import sys

import motion

import almath

import math

import time

from naoqi import ALProxy



def StiffnessOn(proxy):

    # We use the "Body" name to signify the collection of all joints

    pNames = "Body"

    pStiffnessLists = 0.5

    pTimeLists = 0.5

    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)



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



    # Set NAO in Stiffness On

    StiffnessOn(motionProxy)



    # Send NAO to Pose Init

    postureProxy.goToPosture("StandInit", 0.1)



    motionProxy.wbEnable(True)



    # Legs/Feet Configuration

    stateName = "Plane"

    supportLeg = "RLeg"

    motionProxy.wbFootState(stateName, supportLeg)



    stateName = "Fixed"

    supportLeg = "LLeg"

    motionProxy.wbFootState(stateName, supportLeg)





    # Cartesian foot trajectory

    # Warning: Needs a PoseInit before executing

    space      =  motion.FRAME_ROBOT

    axisMask   = 63                     # control all the effector's axes

    isAbsolute = False



    # Lower the Torso and move to the side

    effector = "Torso"

    path     = [0.0, 0.00, 0.00, 0.0, 0.0, 0.05]

    timeList = 1.0 # seconds

    motionProxy.positionInterpolation(effector, space, path,

                                axisMask, timeList, isAbsolute)



    time.sleep(0.02) # wait a few seconds



    # Back to the inizial position

    postureProxy.goToPosture("StandInit", 1.5)



    motionProxy.wbEnable(False)





    

if __name__ == "__main__":

    robotIP = "127.0.0.1"#"192.168.11.3"

    port = 61476 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)

