class TrainsETAService:

    def __init__(self):
        self.etaFirstNorth = 210
        self.etaSecondNorth = 420
        self.etaFirstSouth = 210
        self.etaSecondSouth = 420

    def toDict(self):
        return {
            "etaFirstNorth": self.etaFirstNorth,
            "etaSecondNorth": self.etaSecondNorth,
            "etaFirstSouth": self.etaFirstSouth,
            "etaSecondSouth": self.etaSecondSouth
        }

    def updateETA(self):
        delta = 10
        self.etaFirstNorth -= delta
        self.etaSecondNorth -= delta
        if self.etaFirstNorth == 0:
            self.etaFirstNorth = self.etaSecondNorth
            self.etaSecondNorth = 420

        self.etaFirstSouth -= delta
        self.etaSecondSouth -= delta
        if self.etaFirstSouth == 0:
            self.etaFirstSouth = self.etaSecondSouth 
            self.etaSecondSouth = 420
