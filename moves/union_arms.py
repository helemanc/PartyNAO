''' Movimento Completo Unire le braccia '''



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



    # Set NAO in Stiffness On

#    StiffnessOn(motionProxy)


    # Moving

    ########## Start position ###########

    RShoulderPitch = 67.7

    RShoulderRoll = -26.4

    RElbowYaw = 90.9

    RElbowRoll = 88.5

    RWristYaw = 59.2

    RHand = 0.35

    LShoulderPitch = 80.2

    LShoulderRoll = 24.1

    LElbowYaw = -90.0

    LElbowRoll = -4.4

    LWristYaw = 0.5

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

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)





    #time.sleep(0.2) # Waiting between the two movements





    ####### Movement arms  ###########



    # Open/extend arms

    RShoulderPitch = 58.8

    RShoulderRoll = -25.9

    RElbowYaw = 90.6

    RElbowRoll = 25.0

    RWristYaw = 3.2

    RHand = 0.35

    

    LShoulderPitch = 58.8

    LShoulderRoll = 25.9

    LElbowYaw = -90.6

    LElbowRoll = -25.0

    LWristYaw = -59.4

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

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    

    RWristYaw = 59.4

    motionProxy.post.angleInterpolation("RWristYaw", RWristYaw * almath.TO_RAD, 1, True)



    time.sleep(0.1) # For a better movements synchronization



    # Close arms

    RShoulderPitch = 45.9

    RShoulderRoll = 15.3

    RElbowRoll = 21.6

    

    LShoulderPitch = 45.9

    LShoulderRoll = -15.3

    LElbowRoll = -21.6



    names = "LArm"

    angleLists = [ LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                   LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD ]

    timeLists = 1.0

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    

    names = "RArm"

    angleLists = [ RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                   RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD ]

    timeLists = 1.0

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)



    # Wait a few seconds

    #time.sleep(1)



    # Go to final position

    RShoulderPitch = 78.0

    RShoulderRoll = -16.6

    RElbowYaw = 68.3

    RElbowRoll = 49.2

    RWristYaw = 4.3

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

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)





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

