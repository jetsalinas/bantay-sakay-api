class Train:

    def __init__(self, index, tag, direction, position, load, status, comment=None):
        self.index = index
        self.tag = tag
        self.direction = direction
        self.position = position
        self.load = load
        self.status = status
        self.comment = comment

    def toDict(self):
        return {
            "index": self.index,
            "tag": self.tag,
            "direction": self.direction,
            "position": self.position,
            "load": self.load,
            "status": self.status,
            "comment": self.comment
        }

class TrainsService:

    def __init__(self):
        self.trains = [
            Train(0, "A-1", 1, 0, 0.0, 0),
            Train(0, "B-1", 1, 100, 0.3, 0),
            Train(0, "C-1", 1, 200, 0.3, 0),
            Train(0, "D-1", 1, 300, 0.7, 0),
            Train(0, "E-1", 1, 400, 0.9, 0),
            Train(0, "F-1", 1, 500, 0.9, 0),
            Train(0, "G-1", 1, 600, 0.7, 0),
            Train(0, "H-1", 1, 700, 0.8, 0),
            Train(0, "I-1", 1, 800, 0.7, 0),
            Train(0, "J-1", 1, 900, 0.3, 0),
            Train(0, "K-1", 1, 1000, 0.6, 0),
            Train(0, "L-1", 1, 1100, 0.5, 0),
            Train(0, "M-1", 1, 1200, 0.7, 0),
            Train(0, "N-1", 1, 1300, 0.8, 0),
            Train(0, "O-1", 1, 1400, 0.6, 0),
            Train(0, "P-1", 1, 1500, 0.5, 0),
            Train(0, "Q-1", 1, 1600, 0.7, 0),
            Train(0, "R-1", 1, 1700, 0.8, 0),
            Train(0, "S-1", 1, 1800, 0.9, 0),
            Train(0, "T-1", 1, 1900, 0.3, 0)
        ]

    def getAllTrainsDict(self):
        return [train.toDict() for train in self.trains ]

    def updateTrainsPositionConst(self):
        deltaPos = 10
        for train in self.trains:
            if train.direction == 0:
                continue
            if train.direction == 1:
                if train.position == 1900:
                    train.direction = 2
                else:
                    train.position += 10
            if train.direction == 2:
                if train.position == 0:
                    train.direction = 1
                else:
                    train.position -= 10

