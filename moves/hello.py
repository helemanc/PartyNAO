# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
keys.append([0.29602, -0.170316, -0.340591, -0.0598679, -0.193327, -0.01078])

names.append("HeadYaw")
times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
keys.append([-0.135034, -0.351328, -0.415757, -0.418823, -0.520068, -0.375872])

names.append("LElbowRoll")
times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
keys.append([-1.37902, -1.29005, -1.18267, -1.24863, -1.3192, -1.18421])

names.append("LElbowYaw")
times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
keys.append([-0.803859, -0.691876, -0.679603, -0.610574, -0.753235, -0.6704])

names.append("LHand")
times.append([1.48, 4.52])
keys.append([0.238207, 0.240025])

names.append("LShoulderPitch")
times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
keys.append([1.11824, 0.928028, 0.9403, 0.862065, 0.897349, 0.842125])

names.append("LShoulderRoll")
times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
keys.append([0.363515, 0.226991, 0.20398, 0.217786, 0.248467, 0.226991])

names.append("LWristYaw")
times.append([1.48, 4.52])
keys.append([0.147222, 0.11961])

names.append("RElbowRoll")
times.append([0.64, 1.4, 1.68, 2.08, 2.4, 2.64, 3.04, 3.32, 3.72, 4.44])
keys.append([1.38524, 0.242414, 0.349066, 0.934249, 0.680678, 0.191986, 0.261799, 0.707216, 1.01927, 1.26559])

names.append("RElbowYaw")
times.append([0.64, 1.4, 2.08, 2.64, 3.32, 3.72, 4.44])
keys.append([-0.312978, 0.564471, 0.391128, 0.348176, 0.381923, 0.977384, 0.826783])

names.append("RHand")
times.append([1.4, 3.32, 4.44])
keys.append([0.853478, 0.854933, 0.425116])

names.append("RShoulderPitch")
times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
keys.append([0.247016, -1.17193, -1.0891, -1.26091, -1.14892, 1.02015])

names.append("RShoulderRoll")
times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
keys.append([-0.242414, -0.954191, -0.460242, -0.960325, -0.328317, -0.250085])

names.append("RWristYaw")
times.append([1.4, 3.32, 4.44])
keys.append([-0.312978, -0.303775, 0.182504])

def main(robotIP, port):
  try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    motion = ALProxy("ALMotion", robotIP, port)
    #motion = ALProxy("ALMotion")
    motion.angleInterpolation(names, keys, times, True)
  except BaseException, err:
    print err

