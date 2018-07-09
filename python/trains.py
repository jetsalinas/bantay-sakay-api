class Train:

    def __init__(self, index, tag, position, load, status, comment=None):
        self.index = index
        self.tag = tag
        self.position = position
        self.load = load
        self.status = status
        self.comment = comment

    def toDict(self):
        return {
            "index": self.index,
            "tag": self.tag,
            "position": self.position,
            "load": self.load,
            "status": self.status,
            "comment": self.comment
        }

class Trains:

    def __init__(self):
        self.trains = [
            Train(0, "ABC", 0, 0, 0)
        ]

    def getAllTrainsDict(self):
        return [train.toDict() for train in self.trains ]

