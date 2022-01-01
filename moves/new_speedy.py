# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.00538107, [3, -0.0666667, 0], [3, 1, 0]], [0.00538107, [3, -1, 0], [3, 0.12, 0]], [0.00538107, [3, -0.12, 0], [3, 0.0933333, 0]], [0.00538107, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.671952, [3, -0.133333, 0], [3, 0.12, 0]], [-0.179564, [3, -0.12, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.00691104, [3, -0.0666667, 0], [3, 1, 0]], [-0.00691104, [3, -1, 0], [3, 0.12, 0]], [-0.00691104, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.00691104, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.0802851, [3, -0.133333, 0], [3, 0.12, 0]], [0.00378046, [3, -0.12, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.35, [3, -0.0666667, 0], [3, 1, 0]], [-0.000245917, [3, -1, -0.129619], [3, 0.12, 0.0155543]], [0.0855211, [3, -0.12, 0], [3, 0.0933333, 0]], [0.0855211, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00356753, [3, -0.133333, 0], [3, 0.12, 0]], [0.0859301, [3, -0.12, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.000615553, [3, -0.0666667, 0], [3, 1, 0]], [-0.000615553, [3, -1, 0], [3, 0.12, 0]], [-0.000615553, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.000615553, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.000615553, [3, -0.133333, 0], [3, 0.12, 0]], [-0.129592, [3, -0.12, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-1.00757, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.00757, [3, -0.0933333, 0], [3, 0.08, 0]], [-1.00757, [3, -0.08, 0], [3, 0.0666667, 0]], [-1.00757, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.00757, [3, -0.0933333, 0], [3, 0.0933333, 0]], [-1.00757, [3, -0.0933333, 0], [3, 0.0666667, 0]], [-1.00757, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.00757, [3, -0.0933333, 0], [3, 0.106667, 0]], [-1.00757, [3, -0.106667, 0], [3, 0.08, 0]], [-1.00757, [3, -0.08, 0], [3, 0.0933333, 0]], [-1.00757, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.0431317, [3, -0.133333, 0], [3, 0.12, 0]], [-0.0431317, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.0408853, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.0408853, [3, -0.133333, 0], [3, 0.12, 0]], [-0.40948, [3, -0.12, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-1.38682, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.38682, [3, -0.0933333, 0], [3, 0.08, 0]], [-1.38682, [3, -0.08, 0], [3, 0.0666667, 0]], [-1.38682, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.38682, [3, -0.0933333, 0], [3, 0.0933333, 0]], [-1.38682, [3, -0.0933333, 0], [3, 0.0666667, 0]], [-1.38682, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.38682, [3, -0.0933333, 0], [3, 0.106667, 0]], [-1.38682, [3, -0.106667, 0], [3, 0.08, 0]], [-1.38682, [3, -0.08, 0], [3, 0.0933333, 0]], [-1.38682, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.000992024, [3, -0.133333, -0.00299798], [3, 0.12, 0.00269818]], [0.00170616, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.00913449, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.00913449, [3, -0.133333, 0], [3, 0.12, 0]], [-1.1934, [3, -0.12, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.25, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.25, [3, -0.0933333, 0], [3, 0.08, 0]], [0.25, [3, -0.08, 0], [3, 0.0666667, 0]], [0.25, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.25, [3, -0.0933333, 0], [3, 0.0933333, 0]], [0.25, [3, -0.0933333, 0], [3, 0.0666667, 0]], [0.25, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.25, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.25, [3, -0.106667, 0], [3, 0.08, 0]], [0.25, [3, -0.08, 0], [3, 0.0933333, 0]], [0.25, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.54, [3, -0.133333, 0], [3, 0.12, 0]], [0.54, [3, -0.12, 0], [3, 0.0933333, 0]], [0, [3, -0.0933333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.12, 0]], [0.299054, [3, -0.12, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.459859, [3, -0.0666667, 0], [3, 1, 0]], [-0.000323106, [3, -1, 0], [3, 0.12, 0]], [-0.294961, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.294961, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.000820612, [3, -0.133333, -0.0734738], [3, 0.12, 0.0661264]], [0.12384, [3, -0.12, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.00330668, [3, -0.0666667, 0], [3, 1, 0]], [0.00330668, [3, -1, 0], [3, 0.12, 0]], [0.404916, [3, -0.12, 0], [3, 0.0933333, 0]], [0.404916, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00681927, [3, -0.133333, 0], [3, 0.12, 0]], [0.0956123, [3, -0.12, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.00677235, [3, -0.0666667, 0], [3, 1, 0]], [-0.00677235, [3, -1, 0], [3, 0.12, 0]], [-0.132645, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.132645, [3, -0.0933333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.12, 0]], [-0.166761, [3, -0.12, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.7, [3, -0.0666667, 0], [3, 1, 0]], [0.00762625, [3, -1, 0], [3, 0.12, 0]], [0.129154, [3, -0.12, 0], [3, 0.0933333, 0]], [0.129154, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00984467, [3, -0.133333, 0.0381144], [3, 0.12, -0.0343029]], [-0.0880975, [3, -0.12, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[1.39681, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.39681, [3, -0.0933333, 0], [3, 0.08, 0]], [1.39681, [3, -0.08, 0], [3, 0.0666667, 0]], [1.39681, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.39681, [3, -0.0933333, 0], [3, 0.0933333, 0]], [1.39681, [3, -0.0933333, 0], [3, 0.0666667, 0]], [1.39681, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.39681, [3, -0.0933333, 0], [3, 0.106667, 0]], [1.39681, [3, -0.106667, 0], [3, 0.08, 0]], [1.39681, [3, -0.08, 0], [3, 0.0933333, 0]], [1.39681, [3, -0.0933333, 0], [3, 0.133333, 0]], [-2.08567, [3, -0.133333, 0], [3, 0.12, 0]], [-2.08548, [3, -0.12, -0.000188019], [3, 0.0933333, 0.000146237]], [-0.00258784, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.00258784, [3, -0.133333, 0], [3, 0.12, 0]], [1.47184, [3, -0.12, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.291799, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.291799, [3, -0.0933333, 0], [3, 0.08, 0]], [0.2918, [3, -0.08, 0], [3, 0.0666667, 0]], [0.2918, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.2918, [3, -0.0933333, 0], [3, 0.0933333, 0]], [0.2918, [3, -0.0933333, 0], [3, 0.0666667, 0]], [0.2918, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.2918, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.291799, [3, -0.106667, 0], [3, 0.08, 0]], [0.291799, [3, -0.08, 0], [3, 0.0933333, 0]], [0.291799, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.0141797, [3, -0.133333, 0], [3, 0.12, 0]], [0.0338253, [3, -0.12, 0], [3, 0.0933333, 0]], [0.012892, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.012892, [3, -0.133333, 0], [3, 0.12, 0]], [0.181483, [3, -0.12, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.00274344, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.00274344, [3, -0.0933333, 0], [3, 0.08, 0]], [0.00274345, [3, -0.08, 0], [3, 0.0666667, 0]], [0.00274345, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.00274345, [3, -0.0933333, 0], [3, 0.0933333, 0]], [0.00274345, [3, -0.0933333, 0], [3, 0.0666667, 0]], [0.00274345, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.00274345, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.00274344, [3, -0.106667, 0], [3, 0.08, 0]], [0.00274344, [3, -0.08, 0], [3, 0.0933333, 0]], [0.00274344, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00274344, [3, -0.133333, 0], [3, 0.12, 0]], [0.00274344, [3, -0.12, 0], [3, 0.0933333, 0]], [0.00274344, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00274344, [3, -0.133333, 0], [3, 0.12, 0]], [0.0945625, [3, -0.12, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.35, [3, -0.0666667, 0], [3, 1, 0]], [-0.000245917, [3, -1, 0], [3, 0.12, 0]], [-0.000245917, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.00201699, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.00201699, [3, -0.133333, 0], [3, 0.12, 0]], [0.0856671, [3, -0.12, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.00286675, [3, -0.0666667, 0], [3, 1, 0]], [-0.179769, [3, -1, 0], [3, 0.12, 0]], [-0.179769, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.00431251, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.0314159, [3, -0.133333, 0], [3, 0.12, 0]], [0.126924, [3, -0.12, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.0349066, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.54462, [3, -0.0933333, 0], [3, 0.08, 0]], [1.54462, [3, -0.08, 0], [3, 0.0666667, 0]], [1.54462, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.54462, [3, -0.0933333, 0], [3, 0.0933333, 0]], [1.54462, [3, -0.0933333, 0], [3, 0.0666667, 0]], [1.54462, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.0349066, [3, -0.0933333, 0], [3, 0.106667, 0]], [1.02276, [3, -0.106667, 0], [3, 0.08, 0]], [0.0349066, [3, -0.08, 0], [3, 0.0933333, 0]], [0.0437942, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.043292, [3, -0.133333, 0], [3, 0.12, 0]], [0.043292, [3, -0.12, 0], [3, 0.0933333, 0]], [0.0360991, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.0360991, [3, -0.133333, 0], [3, 0.12, 0]], [0.410546, [3, -0.12, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[1.45386, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.41197, [3, -0.0933333, 0], [3, 0.08, 0]], [1.41197, [3, -0.08, 0], [3, 0.0666667, 0]], [1.41197, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.41197, [3, -0.0933333, 0], [3, 0.0933333, 0]], [1.41197, [3, -0.0933333, 0], [3, 0.0666667, 0]], [1.41197, [3, -0.0666667, 0], [3, 0.0933333, 0]], [2.08567, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.315905, [3, -0.106667, 0.167552], [3, 0.08, -0.125664]], [0.190241, [3, -0.08, 0], [3, 0.0933333, 0]], [0.190258, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00764632, [3, -0.133333, 0], [3, 0.12, 0]], [0.00764632, [3, -0.12, 0], [3, 0.0933333, 0]], [0.000111945, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.000111945, [3, -0.133333, 0], [3, 0.12, 0]], [1.19464, [3, -0.12, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0, [3, -0.0933333, 0], [3, 0.08, 0]], [0, [3, -0.08, 0], [3, 0.0666667, 0]], [0, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0, [3, -0.0933333, 0], [3, 0.0933333, 0]], [0, [3, -0.0933333, 0], [3, 0.0666667, 0]], [0, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.69, [3, -0.106667, 0.137143], [3, 0.08, -0.102857]], [0.28, [3, -0.08, 0], [3, 0.0933333, 0]], [0.28, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.0030505, [3, -0.133333, 0.00338945], [3, 0.12, -0.0030505]], [0, [3, -0.12, 0], [3, 0.0933333, 0]], [0, [3, -0.0933333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.12, 0]], [0.299054, [3, -0.12, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.45, [3, -0.0666667, 0], [3, 1, 0]], [-0.424115, [3, -1, 0], [3, 0.12, 0]], [-0.424115, [3, -0.12, 0], [3, 0.0933333, 0]], [0, [3, -0.0933333, 0], [3, 0.133333, 0]], [-1.53589, [3, -0.133333, 0], [3, 0.12, 0]], [0.125192, [3, -0.12, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.000709385, [3, -0.0666667, 0], [3, 1, 0]], [-0.790634, [3, -1, 0], [3, 0.12, 0]], [-0.79046, [3, -0.12, -0.000174504], [3, 0.0933333, 0.000135725]], [-0.00489601, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.211185, [3, -0.133333, 0], [3, 0.12, 0]], [-0.102119, [3, -0.12, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.00677235, [3, -0.0666667, 0], [3, 1, 0]], [0.0610865, [3, -1, 0], [3, 0.12, 0]], [-0.00677235, [3, -0.12, 0.0363247], [3, 0.0933333, -0.0282525]], [-0.132645, [3, -0.0933333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.12, 0]], [-0.166761, [3, -0.12, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.2, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.7, [3, -0.0666667, 0], [3, 1, 0]], [0.00762625, [3, -1, 0], [3, 0.12, 0]], [0.00762625, [3, -0.12, 0], [3, 0.0933333, 0]], [0.00633415, [3, -0.0933333, 0], [3, 0.133333, 0]], [1.46433, [3, -0.133333, 0], [3, 0.12, 0]], [-0.0853161, [3, -0.12, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.13439, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-0.1265, [3, -0.0933333, 0], [3, 0.08, 0]], [-0.1265, [3, -0.08, 0], [3, 0.0666667, 0]], [-0.1265, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-0.1265, [3, -0.0933333, 0], [3, 0.0933333, 0]], [-0.1265, [3, -0.0933333, 0], [3, 0.0666667, 0]], [-0.1265, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-0.345575, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.13439, [3, -0.106667, 0], [3, 0.08, 0]], [-2.08567, [3, -0.08, 0], [3, 0.0933333, 0]], [2.08567, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00340527, [3, -0.133333, 0.731813], [3, 0.12, -0.658632]], [-2.08567, [3, -0.12, 0], [3, 0.0933333, 0]], [-2.08395, [3, -0.0933333, -0.00172307], [3, 0.133333, 0.00246152]], [-0.000166379, [3, -0.133333, -0.623518], [3, 0.12, 0.561166]], [1.47011, [3, -0.12, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[-0.0575959, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-0.0606406, [3, -0.0933333, 1.94189e-08], [3, 0.08, -1.66448e-08]], [-0.0606406, [3, -0.08, 0], [3, 0.0666667, 0]], [-0.0606406, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-0.0606406, [3, -0.0933333, 0], [3, 0.0933333, 0]], [-0.0606406, [3, -0.0933333, 0], [3, 0.0666667, 0]], [-0.0606406, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.32645, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.314159, [3, -0.106667, 0], [3, 0.08, 0]], [-0.289725, [3, -0.08, 0.00193936], [3, 0.0933333, -0.00226259]], [-0.291987, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.0142155, [3, -0.133333, 0], [3, 0.12, 0]], [-0.0142155, [3, -0.12, 0], [3, 0.0933333, 0]], [-0.034855, [3, -0.0933333, 0], [3, 0.133333, 0]], [-0.00982102, [3, -0.133333, 0], [3, 0.12, 0]], [-0.179067, [3, -0.12, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.2, 0.48, 0.72, 0.92, 1.2, 1.48, 1.68, 1.96, 2.28, 2.52, 2.8, 3.2, 3.56, 3.84, 4.24, 4.6])
keys.append([[0.129154, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.119863, [3, -0.0933333, 9.70944e-08], [3, 0.08, -8.32238e-08]], [0.119863, [3, -0.08, 0], [3, 0.0666667, 0]], [0.119863, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.119863, [3, -0.0933333, 0], [3, 0.0933333, 0]], [0.119863, [3, -0.0933333, 0], [3, 0.0666667, 0]], [0.119863, [3, -0.0666667, 0], [3, 0.0933333, 0]], [-1.82387, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.975639, [3, -0.106667, 0], [3, 0.08, 0]], [0.424115, [3, -0.08, 0], [3, 0.0933333, 0]], [0.426678, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.0036081, [3, -0.133333, 0], [3, 0.12, 0]], [0.0036081, [3, -0.12, 0], [3, 0.0933333, 0]], [0.00622056, [3, -0.0933333, 0], [3, 0.133333, 0]], [0.00622056, [3, -0.133333, 0], [3, 0.12, 0]], [0.097347, [3, -0.12, 0], [3, 0, 0]]])

def main(IP, port):
  try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    motion = ALProxy("ALMotion", IP, port)
    #motion = ALProxy("ALMotion")
    motion.angleInterpolationBezier(names, times, keys)
  except BaseException, err:
    print err

