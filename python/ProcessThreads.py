import threading
from DataGenerator import DataGenerator

class CaptureThread(threading.Thread):
    def __init__(self,caller,gyro,acc,grav,ext):
        super(CaptureThread,self).__init__()
        self.caller = caller
        self.gyro = gyro
        self.acc = acc
        self.grav = grav
        self.gen = DataGenerator()
        self.extra = ext

    def run(self):
        self.dataPoint = self.gen.genFeatures(self.acc[0],self.acc[1],
            self.acc[2],self.grav[0],self.grav[1],
            self.grav[2],self.gyro[0],self.gyro[1],self.gyro[2])
        self.dataPoint = self.dataPoint + self.extra
        self.caller.addPoint(self.dataPoint)


class ProcessThread(threading.Thread):
    def __init__(self,caller,gyro,acc,grav,classifier,ext=None):
        super(ProcessThread,self).__init__()
        self.caller = caller
        self.gyro = gyro
        self.acc = acc
        self.grav = grav
        self.gen = DataGenerator()
        self.extra = ext
        self.classifier = classifier

    def run(self):
        self.dataPoint = self.gen.genFeatures(self.acc[0],self.acc[1],
            self.acc[2],self.grav[0],self.grav[1],
            self.grav[2],self.gyro[0],self.gyro[1],self.gyro[2])
        if self.extra is not None:
            self.dataPoint = self.dataPoint + self.extra
        self.caller.resultList.append(self.classifier.predict(self.dataPoint))

# test = CaptureThread([[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[])
# test.start()