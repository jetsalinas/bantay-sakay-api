import csv

attractionURL = "attractions.csv"

class Attraction():

    def __init__(self, name, address, latitude, longitude, stationName, stationIndex, description=None, image=None, remarks=None, tags=None, resources=None):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.image = image
        self.stationName = stationName,
        self.stationIndex = stationIndex,
        self.remarks = remarks
        self.tags = tags
        self.resources = resources

    def toDict(self):
        return {
            "name": self.name,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "stationName": self.stationName,
            "stationIndex": self.stationIndex,
            "description": self.description,
            "imageUrl": self.image,
            "remarks": self.remarks,
            "tags": self.tags,
            "resources": self.resources
        }

class AttractionService:
    
    def __init__(self):
        self.attractions = []
        with open(attractionURL) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                newAttraction = Attraction(None, None, None, None, None, None)
                newAttraction.name = row[0]
                newAttraction.address = row[1]
                newAttraction.latitude = float(row[2])
                newAttraction.longitude = float(row[3])
                newAttraction.stationName = row[4]
                newAttraction.stationIndex = int(row[5])
                newAttraction.description = row[6]
                newAttraction.image = row[7]
                newAttraction.remarks = row[8].split(' ')
                newAttraction.tags = row[9].split(' ')
                newAttraction.resources = row[10].split(' ')
                self.attractions.append(newAttraction)

    def getAttractions(self):
        return [attraction.toDict() for attraction in self.attractions]


    def getAttraction(self, attractionName):
        for attraction in self.attractions:
            if attraction.name == attractionName:
                return attraction.toDict()

    def getAttractionsPerStation(self):
        
        result = []
        
        stationNames = [
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

        for i in stationNames:
            stationArr = []
            for j in self.attractions:
                if i == j.stationName:
                    stationArr.append({"stationName": i, "data": j.toDict()})
            if stationArr != []:
                result.append(stationArr)
        return result

    def getAttractionPerStation(self, station):
        result = []
        station = int(station)
        for attraction in self.attractions:
            if station == attraction.stationIndex:
                result.append(attraction.toDict())

        return result