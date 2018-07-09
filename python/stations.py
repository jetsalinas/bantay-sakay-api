class Station:
    
    def __init__(self, index, name, latitude, longitude, position, load, comment=None):
        self.index = index
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.position = position
        self.load = load
        self.comment = comment

    def toDict(self):
        return {
            "index": self.index,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "position": self.position,
            "load": self.load
        }

    def toJson(self):
        return jsonify(self.toDict())


class Stations:

    def __init__(self):
        self.stations = [
            Station(0, "Baclaran", 0, 0, 0, 0),
            Station(1, "EDSA", 0, 0, 100, 0),
            Station(2, "Libertad", 0, 0, 200, 0),
            Station(3, "Gil Puyat", 0, 0, 300, 0),
            Station(4, "Vito Cruz", 0, 0, 400, 0),
            Station(5, "Quirino", 0, 0, 500, 0),
            Station(6, "Perdo Gil", 0, 0, 600, 0),
            Station(7, "UN Avenue", 0, 0, 700, 0),
            Station(8, "Central", 0, 0, 800, 0),
            Station(9, "Carriedo", 0, 0, 900, 0),
            Station(10, "Doroteo Jose", 0, 0, 1000, 0),
            Station(11, "Bambang", 0, 0, 1100, 0),
            Station(12, "Tayuman", 0, 0, 1200, 0),
            Station(13, "Blumentritt", 0, 0, 1300, 0),
            Station(14, "Abad Santos", 0, 0, 1400, 0),
            Station(15, "R. Papa", 0, 0, 1500, 0),
            Station(16, "5th Avenue", 0, 0, 1600, 0),
            Station(17, "Monumento", 0, 0, 1700, 0),
            Station(18, "Balitntawak", 0, 0, 1800, 0),
            Station(19, "Roosevelt", 0, 0, 1900, 0)
        ]

    def getAllStations(self):
        return self.stations

    def getAllStationsDict(self):
        return [station.toDict() for station in self.stations]