from datetime import time
import random

class Station:
    
    def __init__(self, index, name, latitude, longitude, position, loadNorth, loadSouth, comment=None):
        self.index = index
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.position = position
        self.loadNorth = loadNorth
        self.loadSouth = loadSouth
        self.comment = comment

    def toDict(self):
        return {
            "index": self.index,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "position": self.position,
            "loadNorth": self.loadNorth,
            "loadSouth": self.loadSouth
        }

class StationsService:

    def __init__(self):
        self.stations = [
            Station(0, "Baclaran", 14.534353, 120.998320, 0, 0.3, 0),
            Station(1, "EDSA", 14.538762, 121.000616, 100, 0.5, 0.1),
            Station(2, "Libertad", 14.547850, 120.998600, 200, 0.3, 0.2),
            Station(3, "Gil Puyat", 14.554256, 120.997092, 300, 0.6, 0.4),
            Station(4, "Vito Cruz", 14.563433, 120.994828, 400, 0.3, 0.3),
            Station(5, "Quirino", 14.5703397, 120.9893693, 500, 0.3, 0.3),
            Station(6, "Perdo Gil", 14.5766113, 120.9868406, 600, 0.4, 0.3),
            Station(7, "UN Avenue", 14.5825552, 120.9824323, 700, 0.2, 0.4),
            Station(8, "Central", 14.5927811, 120.9794726, 800, 0.5, 0.3),
            Station(9, "Carriedo", 14.5992548, 120.9791743, 900, 0.6, 0.2),
            Station(10, "Doroteo Jose", 14.6054454,120.9798723, 1000, 0.6, 0.7),
            Station(11, "Bambang", 14.6054712, 120.9733062, 1100, 0.6, 0.3),
            Station(12, "Tayuman", 14.6166698, 120.980539, 1200, 0.5, 0.2),
            Station(13, "Blumentritt", 14.6227507, 120.9813466, 1300, 0.4, 0.5),
            Station(14, "Abad Santos", 14.6306559, 120.979239, 1400, 0.3, 0.5),
            Station(15, "R. Papa", 14.6360562, 120.9801443, 1500, 0.2, 0.3),
            Station(16, "5th Avenue", 14.6444254, 120.9813945, 1600, 0.3, 0.2),
            Station(17, "Monumento", 14.6543722, 120.9817053, 1700, 0.4, 0.2),
            Station(18, "Balitntawak", 14.6543722, 120.9817053, 1800, 0.3, 0.4),
            Station(19, "Roosevelt", 14.6575508, 121.0190023, 1900, 0, 0.3)
        ]

    def getAllStations(self):
        return self.stations

    def getAllStationsDict(self):
        return [station.toDict() for station in self.stations]

    def updateStationsRandom(self):
        deltaLoad = 0.01
        for station in self.stations:
            station.loadNorth += random.uniform(-deltaLoad, deltaLoad)
            station.loadNorth = 1.1 if (station.loadNorth > 1.1) else station.loadNorth
            station.loadNorth = 0 if (station.loadNorth < 0) else station.loadNorth  

            station.loadSouth += random.uniform(-deltaLoad, deltaLoad)
            station.loadSouth = 1.1 if (station.loadSouth > 1.1) else station.loadSouth
            station.loadSouth = 0 if (station.loadSouth < 0) else station.loadSouth  
        