import random

class Statistics:

    def __init__(self, headwayTime=210, cycleTime=5400, status=1, totalTrains=29):
        self.headwayTime = headwayTime
        self.cycleTime = cycleTime
        self.status = status
        self.totalTrains = totalTrains

    def updateCycleTimeRandom(self):
        deltaTime = 10
        self.cycleTime += random.randint(-deltaTime, deltaTime)
        self.cycleTime = 5700 if self.cycleTime > 5700 else self.cycleTime
        self.cycleTime = 5100 if self.cycleTime < 5100 else self.cycleTime

    def updateHeadwayTimeRandom(self):
        deltaTime = 10
        self.headwayTime += random.randint(-deltaTime, deltaTime)
        self.headwayTime = 240 if self.headwayTime > 240 else self.headwayTime
        self.headwayTime = 180 if self.headwayTime < 180 else self.headwayTime

    def toDict(self): 
        return {
            "headwayTime": self.headwayTime,
            "cycleTime": self.cycleTime,
            "status": self.status,
            "totalTrains": self.totalTrains
        }