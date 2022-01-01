''' Rotazione piede LLeg e rotazione busto:

    NAO senza staccare i piedi da terra ruota esternamente

    LLeg, attende qualche secondo,e poi ruota il busto nella

    direzione che ha assunto il piede LLeg'''



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



    # Legs/Feet configuration

    stateName = "Fixed"

    supportLeg = "RLeg"

    motionProxy.wbFootState(stateName, supportLeg)



    stateName = "Plane"

    supportLeg = "LLeg"

    motionProxy.wbFootState(stateName, supportLeg)





    # Cartesian foot trajectory

    # Warning: Needs a PoseInit before executing

    space      =  motion.FRAME_ROBOT

    axisMask   = 63                     # control all the effector's axes

    isAbsolute = False



    # Lower the Torso and move to the side

    effector = "Torso"

    path     = [0.0, 0.0, 0.15, 0.0, 0.0, 0.05]

    timeList = 1.0 # seconds

    motionProxy.positionInterpolation(effector, space, path,

                                axisMask, timeList, isAbsolute)



    motionProxy.wbEnable(False)



    time.sleep(0.02) # waiting a few seconds

    

    motionProxy.wbEnable(True)



    # New Legs/Feet configuration

    stateName = "Fixed"

    supportLeg = "LLeg"

    motionProxy.wbFootState(stateName, supportLeg)



    stateName = "Plane"

    supportLeg = "RLeg"

    motionProxy.wbFootState(stateName, supportLeg)



    postureProxy.goToPosture("StandInit", 1.5)



    motionProxy.wbEnable(False)



   

    

if __name__ == "__main__":

    robotIP = "127.0.0.1"

    port = 61476 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)

