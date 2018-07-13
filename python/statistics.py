import random

class Statistics:

    def __init__(self, headwayTime=210, cycleTime=5400, running=1, totalTrains=19):
        self.headwayTime = headwayTime
        self.cycleTime = cycleTime
        self.running = running
        self.totalTrains = totalTrains

    def updateCycleTimeRandom(self):
        deltaTime = 30
        self.cycleTime += random.randint(-deltaTime, deltaTime)
        self.cycleTime = 5700 if self.cycleTime > 5700 else self.cycleTime
        self.cycleTime = 5100 if self.cycleTime < 5100 else self.cycleTime

    def updateHeadwayTimeRandom(self):
        deltaTime = 30
        self.headwayTime += random.randint(-deltaTime, deltaTime)
        self.headwayTime = 240 if self.headwayTime > 240 else self.headwayTime
        self.headwayTime = 180 if self.headwayTime < 180 else self.headwayTime