import random

class Train:

    def __init__(self, index, tag, direction, position, load, status, station, comment=None):
        self.index = index
        self.tag = tag
        self.direction = direction
        self.position = position
        self.load = load
        self.status = status
        self.station = station
        self.comment = comment

    def toDict(self):
        return {
            "index": self.index,
            "tag": self.tag,
            "direction": self.direction,
            "position": self.position,
            "load": self.load,
            "status": self.status,
            "comment": self.comment,
            "self.station": self.station
        }

class TrainsService:

    def __init__(self):
        self.trains = [
            Train(0, "A-1", 1, 0, 0.5, 1, "Baclaran"),
            Train(1, "B-1", 1, 100, 0.3, 1, "EDSA"),
            Train(2, "C-1", 1, 200, 0.3, 1, "Libertad"),
            Train(3, "D-1", 1, 300, 0.7, 1, "Gil Puyat"),
            Train(4, "E-1", 1, 400, 0.9, 1, "Vito Cruz"),
            Train(5, "F-1", 1, 500, 0.9, 1, "Quirino"),
            Train(6, "G-1", 1, 600, 0.7, 1, "Pedro Gil"),
            Train(7, "H-1", 1, 700, 0.8, 1, "UN Avenue"),
            Train(8, "I-1", 1, 800, 0.7, 1, "Central"),
            Train(9, "J-1", 1, 900, 0.3, 1, "Carriedo"),
            Train(10, "K-1", 1, 1000, 0.6, 1, "Doroteo Jose"),
            Train(11, "L-1", 1, 1100, 0.5, 1, "Bambang"),
            Train(12, "M-1", 1, 1200, 0.7, 1, "Tayuman"),
            Train(13, "N-1", 1, 1300, 0.8, 1, "Blumentritt"),
            Train(14, "O-1", 1, 1400, 0.6, 1, "Abad Santos"),
            Train(15, "P-1", 1, 1500, 0.5, 1, "R. Papa"),
            Train(16, "Q-1", 1, 1600, 0.7, 1, "5th Avenue"),
            Train(17, "R-1", 1, 1700, 0.8, 1, "Monumento"),
            Train(18, "S-1", 1, 1800, 0.9, 1, "Balintawak"),
            Train(19, "T-1", 1, 1900, 0.3, 1, "Roosevelt")
        ]

        self.stationPositions = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
        self.stationNames = [
            "Baclaran",
            "EDSA",
            "Libertad",
            "Gil Puyat",
            "Vito Cruz",
            "Quirino",
            "Pedro Gil",
            "UN Avenue",
            "Central",
            "Carriedo",
            "Doroteo Jose",
            "Bambang",
            "Tayuman",
            "Blumentritt",
            "Abad Santos",
            "R. Papa",
            "5th Avenue",
            "Monumento",
            "Banlintawak",
            "Roosevelt"
        ]

    def getAllTrainsDict(self):
        return [train.toDict() for train in self.trains ]

    def updateTrainsPositionConst(self):
        deltaPos = 10
        for train in self.trains:
            if train.direction == 0 or train.status == 0:
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

        for c, position in enumerate(self.stationPositions):
            if train.position == position:
                train.station = self.stationNames[c]

    def updateTrainLoadRandom(self):
        deltaLoad = 0.4
        for train in self.trains:
            if train.position in self.stationPositions and train.status != 0:
                train.load += random.uniform(-deltaLoad, deltaLoad)
                train.load = 1.1 if (train.load > 1.1) else train.load
                train.load = 0 if (train.load < 0) else train.load