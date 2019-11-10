import random
import math

class BlasterShot:
    __RangeOfSensor = 500 # centimeters

    def __init__(self, distance):
        self.blasterRadius = 2 # centimeters
        self.distance = distance
        self.calculateHit()
    
    def calculateHit(self):
        self.maximumHitRadius = pow(math.e,self.distance) * self.blasterRadius - self.blasterRadius

        self.randomHitradius = random.uniform(0, self.maximumHitRadius)



newBlasterHit = BlasterShot(1)
print(newBlasterHit.randomHitradius)