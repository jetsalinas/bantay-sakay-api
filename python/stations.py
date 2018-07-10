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
            Station(0, "Baclaran", 0, 0, 0, 0.3, 0),
            Station(1, "EDSA", 0, 0, 100, 0.5, 0.1),
            Station(2, "Libertad", 0, 0, 200, 0.3, 0.2),
            Station(3, "Gil Puyat", 0, 0, 300, 0.6, 0.4),
            Station(4, "Vito Cruz", 0, 0, 400, 0.3, 0.3),
            Station(5, "Quirino", 0, 0, 500, 0.3, 0.3),
            Station(6, "Perdo Gil", 0, 0, 600, 0.4, 0.3),
            Station(7, "UN Avenue", 0, 0, 700, 0.2, 0.4),
            Station(8, "Central", 0, 0, 800, 0.5, 0.3),
            Station(9, "Carriedo", 0, 0, 900, 0.6, 0.2),
            Station(10, "Doroteo Jose", 0, 0, 1000, 0.6, 0.7),
            Station(11, "Bambang", 0, 0, 1100, 0.6, 0.3),
            Station(12, "Tayuman", 0, 0, 1200, 0.5, 0.2),
            Station(13, "Blumentritt", 0, 0, 1300, 0.4, 0.5),
            Station(14, "Abad Santos", 0, 0, 1400, 0.3, 0.5),
            Station(15, "R. Papa", 0, 0, 1500, 0.2, 0.3),
            Station(16, "5th Avenue", 0, 0, 1600, 0.3, 0.2),
            Station(17, "Monumento", 0, 0, 1700, 0.4, 0.2),
            Station(18, "Balitntawak", 0, 0, 1800, 0.3, 0.4),
            Station(19, "Roosevelt", 0, 0, 1900, 0, 0.3)
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
        