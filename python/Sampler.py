from DataGenerator import DataGenerator
from ProcessThreads import *
import time

# 82 = Linear Acc
# 83 = Gravity

class TrainSampler:
    def __init__(self,caller,extra):
        self.gyro = [[],[],[]]
        self.grav = [[],[],[]]
        self.acc = [[],[],[]]
        self.caller = caller
        self.extra = extra
        self.time = 0
        self.len = 0

    def add(self,sample):
        # print(sample['4'][0])
        # print(self.gyro)
        # print(self.acc)
        # print(self.grav)
        self.gyro[0].append(sample[4][0])
        self.gyro[1].append(sample[4][1])
        self.gyro[2].append(sample[4][2])
        
        self.acc[0].append(sample[82][0])
        self.acc[1].append(sample[82][1])
        self.acc[2].append(sample[82][2])

        self.grav[0].append(sample[83][0])
        self.grav[1].append(sample[83][1])
        self.grav[2].append(sample[83][2])

        if len(self.gyro[0]) == 128:
            # print(self.gyro)
            # print(self.acc)
            # print(self.grav)
            # Spawn thread for data generation
            # print("len = " + str(len(self.acc[0])))
            self.captureThread = CaptureThread(self.caller,list(self.gyro),list(self.acc),
            list(self.grav),list(self.extra))
            # print("Spawn")
            self.captureThread.start()

            self.gyro[0] = self.gyro[0][64:]
            self.gyro[1] = self.gyro[1][64:]
            self.gyro[2] = self.gyro[2][64:]

            self.acc[0] = self.acc[0][64:]
            self.acc[1] = self.acc[1][64:]
            self.acc[2] = self.acc[2][64:]

            self.grav[0] = self.grav[0][64:]
            self.grav[1] = self.grav[1][64:]
            self.grav[2] = self.grav[2][64:]
            # print("len = " + str(len(self.acc[0])))
            print(time.clock())
import numpy as np
# a = np.zeros(4)
# a[0] = 1
# a[1] = -2.5
# a[2] = 3.4
# a[3] = 0
# print(a.conj())
# x = [0,1,2,3]
# print(x[0:-1])