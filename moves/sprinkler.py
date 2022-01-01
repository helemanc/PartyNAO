# Choregraphe simplified export in Python.
from naoqi import ALProxy
import right_arm
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1, 2.48, 7, 7.92])
keys.append([-0.12583, -0.233874, -0.173384, -0.173384])

names.append("HeadYaw")
times.append([1, 2.48, 7, 7.92])
keys.append([-0.0107799, 0.912807, 0.21932, 0.21932])

names.append("LAnklePitch")
times.append([1, 2.32, 7, 7.92])
keys.append([0.095066, -0.214803, -0.406552, -0.406552])

names.append("LAnkleRoll")
times.append([1, 2.32, 7, 7.92])
keys.append([-0.116542, -0.14262, -0.11961, -0.11961])

names.append("LElbowRoll")
times.append([1, 2.4, 3, 7, 7.92])
keys.append([-0.400331, -0.0349066, -0.0459781, -0.358915, -0.358915])

names.append("LElbowYaw")
times.append([1, 2.4, 3, 7, 7.92])
keys.append([-1.21037, -1.48956, -1.48035, -1.26099, -1.26099])

names.append("LHand")
times.append([1, 2.4, 3, 7, 7.92])
keys.append([0.3056, 0.9616, 0.9592, 0.9616, 0.9616])

names.append("LHipPitch")
times.append([1, 2.32, 7, 7.92])
keys.append([0.136568, -0.144154, -0.268407, -0.268407])

names.append("LHipRoll")
times.append([1, 2.32, 7, 7.92])
keys.append([0.115092, 0.233211, 0.173384, 0.173384])

names.append("LHipYawPitch")
times.append([1, 2.32, 7, 7.92])
keys.append([-0.1733, -0.288349, -0.28068, -0.28068])

names.append("LKneePitch")
times.append([1, 2.32, 7, 7.92])
keys.append([-0.090548, 0.539926, 0.820649, 0.820649])

names.append("LShoulderPitch")
times.append([1, 2.4, 2.48, 3, 7, 7.92])
keys.append([1.53089, -0.420357, -0.560251, -0.417134, -0.0966839, -0.0966839])

names.append("LShoulderRoll")
times.append([1, 1.8,1.9, 2.0, 2.1, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1])
keys.append([0.13495, 0.819114, 0.461692, 0.610865, 0.223402, 0.460767, 0.0436332, 0.312414, -0.0610865, 0.207694, -0.195477, 0.0593412, -0.159578, -0.159578])

names.append("LWristYaw")
times.append([1, 2.4, 3, 3.44, 3.8, 7, 7.92])
keys.append([0.121144, 0.312894, 0.131882, 0.0663225, 0.0663225, -0.29457, -0.29457])

names.append("RAnklePitch")
times.append([1, 2.32, 7, 7.92])
keys.append([0.10282, -0.0199001, -0.263807, -0.263807])

names.append("RAnkleRoll")
times.append([1, 2.32, 7, 7.92])
keys.append([0.07214, 0.116626, 0.0828778, 0.0828778])

names.append("RElbowRoll")
times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
keys.append([0.385075, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53558, 1.53558])

names.append("RElbowYaw")
times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
keys.append([1.18421, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.36982, 1.36982])

names.append("RHand")
times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
keys.append([0.3068, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7692, 0.7692])

names.append("RHipPitch")
times.append([1, 2.32, 7, 7.92])
keys.append([0.130348, 0.138018, -0.251617, -0.251617])

names.append("RHipRoll")
times.append([1, 2.32, 7, 7.92])
keys.append([-0.06592, -0.0383082, -0.0291041, -0.0291041])

names.append("RHipYawPitch")
times.append([1, 2.32, 7, 7.92])
keys.append([-0.1733, -0.288349, -0.28068, -0.28068])

names.append("RKneePitch")
times.append([1, 2.32, 7, 7.92])
keys.append([-0.0904641, 0.0798099, 0.676537, 0.676537])

names.append("RShoulderPitch")
times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
keys.append([1.51103, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.544529, -0.544529])

names.append("RShoulderRoll")
times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
keys.append([-0.113558, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.075208, -0.075208])

names.append("RWristYaw")
times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
keys.append([0.105804, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.820649, 0.820649])

def main(ip, port):
    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", ip, port)
        #motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)
        right_arm.main(ip, port)
    except BaseException, err:
        print err
