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
            Train(0, "ABC", 1, 0, 0, 0)
        ]

    def getAllTrainsDict(self):
        return [train.toDict() for train in self.trains ]

