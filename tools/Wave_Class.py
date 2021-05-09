import math

PI = math.pi

class Wave:
    def __init__(self, wavelength, wavespeed, waveamplitude):
        self.wavelength = wavelength
        self.wavespeed = wavespeed
        self.waveamplitude = waveamplitude
        self.xpos = -1
        self.ypos = -1
        self.startingPhase = 0
        
    def setPos(self, x, y):
        self.xpos = x
        self.ypos = y
        
    def setPhase(self, phase):
        self.startingPhase = phase
    
    def getWaveFunction(self):
        def generatedFunction(d, t):
            k = 2 * PI / self.wavelength
            omega = 2 * PI * self.wavespeed / self.wavelength
            return self.waveamplitude * math.sin(k * d - omega * t + self.startingPhase)
        return generatedFunction