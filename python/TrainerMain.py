from DataGenerator import *
from Sampler import TrainSampler
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation
import socket, traceback
import threading, time, os

class TrainerMainModel(threading.Thread):

    host = ''
    port = 5555
    samp = {
        '4': [],
        '82': [],
        '83': []
    }
    execute = True
    subject = 0
    act = 1

    def __init__(self):
        super(TrainerMainModel,self).__init__()
        # self.readingCounter = 0
        # self.resultListY = []
        q = []
        self.cols = pd.read_csv("colums.csv")
        self.myDataset = pd.DataFrame(columns=self.cols['0'].tolist())
        self.pointCount = 0

        # Ask for subject and activity
        print("Enter subject ID: ")
        self.subject = int(input())
        print("Enter Activity: ")
        self.act = input()

        self.sampler = TrainSampler(self,[self.subject, self.act])

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.s.bind((self.host, self.port))

        for i in range(0,3):
            message, address = self.s.recvfrom(8192)
            message = str(message)
            message = message[2:len(message)-1].split(", ")
            q.append(message)

        while q[0][0] != q[1][0]:
            message, address = self.s.recvfrom(8192)
            message = str(message)
            message = message[2:len(message)-1].split(", ")
            q.append(message)
            q.remove(q[0])

    def run(self):
        while self.execute:
            try:
                for i in range(0,3):
                    message, address = self.s.recvfrom(8192)
                    message = str(message)
                    message = message[2:len(message)-1].split(", ")
                    # print(message)
                    message[0] = float(message[0])
                    # message[1] = int(message[1])
                    message[2] = float(message[2])
                    message[3] = float(message[3])
                    message[4] = float(message[4])
                    # print(message)
                    self.samp[message[1]] = message[2:]
                self.sampler.add(self.samp)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                traceback.print_exc()

    def addPoint(self,dataPoint):
        self.myDataset.loc[self.pointCount] = dataPoint
        self.pointCount = self.pointCount + 1
        print(self.pointCount)
            

if __name__ == "__main__":
    try:
        myModel = TrainerMainModel()
        myModel.start()
        time.sleep(100000)
        # input()
    except (KeyboardInterrupt):
        # print("KeyBoardInterrupt")
        myModel.execute = False
        file_path = "datasets/" + str(myModel.subject) + "/"
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
        except OSError:
            print("Error in creating directories!!")
        print("Saving dataset...")
        myModel.myDataset.to_csv(file_path + myModel.act + ".csv")

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# def animate(i):
#     ax1.clear()
#     ax1.plot(myModel.resultListY)

# anim = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()
# myModel.join()