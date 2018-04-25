from StatFunc import StatFunc
import scipy.stats as stats
import numpy as np

class Time3DStat:
    
    def __init__(self,windowX,windowY,windowZ):
        self.windowX = windowX
        self.windowY = windowY
        self.windowZ = windowZ

    def generate(self):
        fun = StatFunc()
        ans = [np.mean(self.windowX),
            np.mean(self.windowY),
            np.mean(self.windowZ),
            np.std(self.windowX),
            np.std(self.windowY),
            np.std(self.windowZ),
        ]
        # print(ans[0])
        ans2 = [fun.mad(self.windowX,ans[0]),
            fun.mad(self.windowY,ans[1]),
            fun.mad(self.windowZ,ans[2]),
            np.max(self.windowX),
            np.max(self.windowY),
            np.max(self.windowZ),
            np.min(self.windowX),
            np.min(self.windowY),
            np.min(self.windowZ),
            fun.sma(self.windowX,self.windowY,self.windowZ),
            fun.energy(self.windowX),
            fun.energy(self.windowY),
            fun.energy(self.windowZ),
            stats.iqr(self.windowX),
            stats.iqr(self.windowY),
            stats.iqr(self.windowZ),
            # fun.entropy(self.windowX),
            # fun.entropy(self.windowY),
            # fun.entropy(self.windowZ),
        ]
        ans = ans + ans2
        arc = fun.arburg(self.windowX,4)
        ans = ans + [arc[0][1], arc[0][2], arc[0][3], arc[0][4]]
        arc = fun.arburg(self.windowY,4)
        ans = ans + [arc[0][1], arc[0][2], arc[0][3], arc[0][4]]
        arc = fun.arburg(self.windowZ,4)
        ans = ans + [arc[0][1], arc[0][2], arc[0][3], arc[0][4]]
        corr = np.corrcoef(self.windowX,self.windowY)
        ans.append(corr[0][1])
        corr = np.corrcoef(self.windowX,self.windowZ)
        ans.append(corr[0][1])
        corr = np.corrcoef(self.windowY,self.windowZ)
        ans.append(corr[0][1])

        return ans

class Time3DMag:
    def __init__(self,window):
        self.window = window

    def generate(self):
        fun = StatFunc()
        ans = [
            np.mean(self.window),
            np.std(self.window),
        ]
        ans2 = [
            fun.mad(self.window,ans[0]),
            np.max(self.window),
            np.min(self.window),
            ans[0],
            fun.energy(self.window),
            stats.iqr(self.window),
            # fun.entropy(self.window)
        ]
        ans = ans + ans2
        arc = fun.arburg(self.window,4)
        ans = ans + [arc[0][1], arc[0][2], arc[0][3], arc[0][4]]
        return ans

class FFT3DStat:

    def __init__(self,windowX,windowY,windowZ):
        self.windowX = windowX
        self.windowY = windowY
        self.windowZ = windowZ

    def generate(self):
        fun = StatFunc()
        ans = [
            np.mean(self.windowX),
            np.mean(self.windowY),
            np.mean(self.windowZ),
            np.std(self.windowX),
            np.std(self.windowY),
            np.std(self.windowZ),
        ]
        ans2 = [
            fun.mad(self.windowX,ans[0]),
            fun.mad(self.windowY,ans[1]),
            fun.mad(self.windowZ,ans[2]),
            np.max(self.windowX),
            np.max(self.windowY),
            np.max(self.windowZ),
            np.min(self.windowX),
            np.min(self.windowY),
            np.min(self.windowZ),
            fun.sma(self.windowX,self.windowY,self.windowZ),
            fun.energy(self.windowX),
            fun.energy(self.windowY),
            fun.energy(self.windowZ),
            stats.iqr(self.windowX),
            stats.iqr(self.windowY),
            stats.iqr(self.windowZ),
            # fun.entropy(self.windowX),
            # fun.entropy(self.windowY),
            # fun.entropy(self.windowZ),

            # fun.maxInds(self.windowX),
            # fun.maxInds(self.windowY),
            # fun.maxInds(self.windowZ),
            # np.average(range(1,len(self.windowX)+1),weights=self.windowX),
            # np.average(range(1,len(self.windowY)+1),weights=self.windowY),
            # np.average(range(1,len(self.windowZ)+1),weights=self.windowZ),

            stats.skew(self.windowX),
            stats.kurtosis(self.windowX),
            stats.skew(self.windowY),
            stats.kurtosis(self.windowY),
            stats.skew(self.windowZ),
            stats.kurtosis(self.windowZ)
            # fun.bandsEnergy(self.windowX,1,8),
            # fun.bandsEnergy(self.windowX,9,16),
            # fun.bandsEnergy(self.windowX,17,24),
            # fun.bandsEnergy(self.windowX,25,32),
            # fun.bandsEnergy(self.windowX,33,40),
            # fun.bandsEnergy(self.windowX,41,48),
            # fun.bandsEnergy(self.windowX,49,56),
            # fun.bandsEnergy(self.windowX,57,64),
            # fun.bandsEnergy(self.windowX,1,16),
            # fun.bandsEnergy(self.windowX,17,32),
            # fun.bandsEnergy(self.windowX,33,48),
            # fun.bandsEnergy(self.windowX,49,64),
            # fun.bandsEnergy(self.windowX,1,24),
            # fun.bandsEnergy(self.windowX,25,48),
            # fun.bandsEnergy(self.windowY,1,8),
            # fun.bandsEnergy(self.windowY,9,16),
            # fun.bandsEnergy(self.windowY,17,24),
            # fun.bandsEnergy(self.windowY,25,32),
            # fun.bandsEnergy(self.windowY,33,40),
            # fun.bandsEnergy(self.windowY,41,48),
            # fun.bandsEnergy(self.windowY,49,56),
            # fun.bandsEnergy(self.windowY,57,64),
            # fun.bandsEnergy(self.windowY,1,16),
            # fun.bandsEnergy(self.windowY,17,32),
            # fun.bandsEnergy(self.windowY,33,48),
            # fun.bandsEnergy(self.windowY,49,64),
            # fun.bandsEnergy(self.windowY,1,24),
            # fun.bandsEnergy(self.windowY,25,48),
            # fun.bandsEnergy(self.windowZ,1,8),
            # fun.bandsEnergy(self.windowZ,9,16),
            # fun.bandsEnergy(self.windowZ,17,24),
            # fun.bandsEnergy(self.windowZ,25,32),
            # fun.bandsEnergy(self.windowZ,33,40),
            # fun.bandsEnergy(self.windowZ,41,48),
            # fun.bandsEnergy(self.windowZ,49,56),
            # fun.bandsEnergy(self.windowZ,57,64),
            # fun.bandsEnergy(self.windowZ,1,16),
            # fun.bandsEnergy(self.windowZ,17,32),
            # fun.bandsEnergy(self.windowZ,33,48),
            # fun.bandsEnergy(self.windowZ,49,64),
            # fun.bandsEnergy(self.windowZ,1,24),
            # fun.bandsEnergy(self.windowZ,25,48)
        ]
        ans = ans + ans2

        return ans

class FFT3DMag:
    def __init__(self,window):
        self.window = window

    def generate(self):
        fun = StatFunc()
        ans = [
            np.mean(self.window),
            np.std(self.window),
        ]
        ans2 = [
            fun.mad(self.window,ans[0]),
            np.max(self.window),
            np.min(self.window),
            ans[0],
            fun.energy(self.window),
            stats.iqr(self.window),
            # fun.entropy(self.window),

            # fun.maxInds(self.window),
            # np.average(range(1,len(self.window)+1),weights=self.window),

            stats.skew(self.window),
            stats.kurtosis(self.window)
        ]
        ans = ans + ans2

        return ans

class DataGenerator:

    def __init__(self):
        self.fun = StatFunc()

    def genFeatures(self,bodyAX,bodyAY,bodyAZ,gravX,gravY,gravZ,gyroVecX,gyroVecY,gyroVecZ):
        # Finding jerk signals
        # For body acceleration
        bodyAccJerkX = self.fun.derivative([2*bodyAX[0]-bodyAX[1]]+bodyAX,interval=0.02)
        bodyAccJerkY = self.fun.derivative([2*bodyAY[0]-bodyAY[1]]+bodyAY,interval=0.02)
        bodyAccJerkZ = self.fun.derivative([2*bodyAZ[0]-bodyAZ[1]]+bodyAZ,interval=0.02)

        # For Gyroscope
        gyroJerkX = self.fun.derivative([2*gyroVecX[0]-gyroVecX[1]]+gyroVecX,interval=0.02)
        gyroJerkY = self.fun.derivative([2*gyroVecY[0]-gyroVecY[1]]+gyroVecY,interval=0.02)
        gyroJerkZ = self.fun.derivative([2*gyroVecZ[0]-gyroVecZ[1]]+gyroVecZ,interval=0.02)

        # Finding magnitudes
        bodyAccMag = self.fun.magnitudeVector(bodyAX, bodyAY, bodyAZ)
        gravMag = self.fun.magnitudeVector(gravX, gravY, gravZ)
        bodyAJMag = self.fun.magnitudeVector(bodyAccJerkX, bodyAccJerkY, bodyAccJerkZ)
        gyroMag = self.fun.magnitudeVector(gyroVecX, gyroVecY, gyroVecZ)
        gyroJMag = self.fun.magnitudeVector(gyroJerkX, gyroJerkY, gyroJerkZ)

        # Generating data
        tBodyAcc = Time3DStat(bodyAX, bodyAY, bodyAZ).generate()
        tGravityAcc = Time3DStat(gravX, gravY, gravZ).generate()
        tBodyAccJerk = Time3DStat(bodyAccJerkX, bodyAccJerkY, bodyAccJerkZ).generate()
        tBodyGyro = Time3DStat(gyroVecX, gyroVecY, gyroVecZ).generate()
        tBodyGyroJerk = Time3DStat(gyroJerkX,gyroJerkY,gyroJerkZ).generate()

        tBodyAccMag = Time3DMag(bodyAccMag).generate()
        # tGravityAccMag = Time3DMag(gravMag).generate()
        tBodyAccJerkMag = Time3DMag(bodyAJMag).generate()
        tBodyGyroMag = Time3DMag(gyroMag).generate()
        tBodyGyroJerkMag = Time3DMag(gyroJMag).generate()

        #Applying FFT
        # For bodyAcc and bodyAccJerk
        FFTBodyAccX = np.absolute(np.fft.fft(bodyAX))
        FFTBodyAccY = np.absolute(np.fft.fft(bodyAY))
        FFTBodyAccZ = np.absolute(np.fft.fft(bodyAZ))

        FFTBodyAccJerkX = np.absolute(np.fft.fft(bodyAccJerkX))
        FFTBodyAccJerkY = np.absolute(np.fft.fft(bodyAccJerkY))
        FFTBodyAccJerkZ = np.absolute(np.fft.fft(bodyAccJerkZ))

        # For bodyGyro
        FFTBodyGyroX = np.absolute(np.fft.fft(gyroVecX))
        FFTBodyGyroY = np.absolute(np.fft.fft(gyroVecY))
        FFTBodyGyroZ = np.absolute(np.fft.fft(gyroVecZ))

        # For bodyAccMag, bodyAccJerkMag, bodyGyroMag, bodyGyroMag
        FFTbodyAccMag = np.absolute(np.fft.fft(bodyAccMag))
        FFTbodyAccJerkMag = np.absolute(np.fft.fft(bodyAJMag))
        FFTgyroMag = np.absolute(np.fft.fft(gyroMag))
        FFTgyroJerkMag = np.absolute(np.fft.fft(gyroJMag))

        # Generating data
        fBodyAcc = FFT3DStat(FFTBodyAccX, FFTBodyAccY, FFTBodyAccZ).generate()
        fBodyAccJerk = FFT3DStat(FFTBodyAccJerkX, FFTBodyAccJerkY, FFTBodyAccJerkZ).generate()
        fBodyGyro = FFT3DStat(FFTBodyGyroX, FFTBodyGyroY, FFTBodyGyroZ).generate()

        fBodyAccMag = FFT3DMag(FFTbodyAccMag).generate()
        fBodyBodyAccJerkMag = FFT3DMag(FFTbodyAccJerkMag).generate()
        fBodyBodyGyroMag = FFT3DMag(FFTgyroMag).generate()
        fBodyBodyGyroJerkMag = FFT3DMag(FFTgyroJerkMag).generate()

        # Generating angles
        AngleBodyAccGrav = self.fun.angle(tBodyAcc[0:3],tGravityAcc[0:3])
        AngleBodyAccJerkGrav = self.fun.angle(tBodyAccJerk[0:3],tGravityAcc[0:3])
        AngleBodyGyroGrav = self.fun.angle(tBodyGyro[0:3],tGravityAcc[0:3])
        AngleBodyGyroJerkGrav = self.fun.angle(tBodyGyroJerk[0:3],tGravityAcc[0:3])
        AngleGravX = self.fun.angle([1,0,0],tGravityAcc[0:3])
        AngleGravY = self.fun.angle([0,1,0],tGravityAcc[0:3])
        AngleGravZ = self.fun.angle([0,0,1],tGravityAcc[0:3])

        # Concatenating all the data segments
        dataPoint = tBodyAcc + tGravityAcc + tBodyAccJerk + tBodyGyro + tBodyGyroJerk
        # dataPoint.append(tBodyAccJerk).append(tBodyGyro).append(tBodyGyroJerk)
        dataPoint = dataPoint + tBodyAccMag + tBodyAccJerkMag + tBodyGyroMag
        # tGravityAccMag +
        # dataPoint.append(tBodyAccMag).append(tGravityAccMag).append(tBodyAccJerkMag)
        # dataPoint.append(tBodyGyroMag).append(tBodyGyroJerkMag)
        dataPoint = dataPoint + tBodyGyroJerkMag + fBodyAcc + fBodyAccJerk + fBodyGyro
        # dataPoint.append(fBodyAcc).append(fBodyAccJerk).append(fBodyGyro)
        dataPoint = dataPoint + fBodyAccMag + fBodyBodyAccJerkMag + fBodyBodyGyroMag
        # dataPoint.append(fBodyAccMag).append(fBodyBodyAccJerkMag).append(fBodyBodyGyroMag)
        dataPoint = dataPoint + fBodyBodyGyroJerkMag + [AngleBodyAccGrav]
        # dataPoint.append(fBodyBodyGyroJerkMag).append(AngleBodyAccGrav)
        dataPoint = dataPoint + [AngleBodyAccJerkGrav, AngleBodyGyroGrav, AngleBodyGyroJerkGrav]
        # dataPoint.append(AngleBodyAccJerkGrav).append(AngleBodyGyroGrav).append(AngleBodyGyroJerkGrav)
        dataPoint = dataPoint + [AngleGravX, AngleGravY, AngleGravZ]
        return dataPoint