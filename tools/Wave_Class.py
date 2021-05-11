import math

PI = math.pi


class Wave:
    def __init__(self, wavelength, wavespeed, waveamplitude):
        self.wavelength = wavelength
        self.wavespeed = wavespeed
        self.waveamplitude = waveamplitude
        self.xpos = 0
        self.ypos = 0
        self.startingPhase = 0

    def setPos(self, x, y):
        self.xpos = x
        self.ypos = y

    def setPhase(self, phase):
        self.startingPhase = phase

    def getWaveFunction(self, spreading=False):
        k = 2 * PI / self.wavelength
        omega = 2 * PI * self.wavespeed / self.wavelength

        def generatedFunction(d, t=0):
            if(spreading):
                if(d > (t * self.wavespeed)):
                    return 0
            return self.waveamplitude * math.sin(k * d - omega * t + self.startingPhase)

        return generatedFunction

    def distanceFunction(self):
        def generatedFunction(x, y):
            return math.sqrt((x - self.xpos) ** 2 + (y - self.ypos) ** 2)
        
        return generatedFunction
