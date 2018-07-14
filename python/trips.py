class TripNode:

    def __init__(self, tripIndex, attraction):
        self.tripIndex = tripIndex
        self.attraction = attraction

    def toDict(self):
        return {
            "tripIndex": self.tripIndex,
            "attraction": self.attraction.toDict()
        }

class Trip:

    def __init__(self, name, description, tripNodes, imageUrl):
        self.name = name
        self.description = description
        self.tripNodes = tripNodes
        self.imageUrl = imageUrl

    def toDict(self):
        return {
            "name": self.name,
            "description": self.description,
            "imageUrl": self.imageUrl,
            "nodes": [tripNode.toDict() for tripNode in self.tripNodes]
            }

class Trips:

    def __init__(self, attractions):
        self.trips = [
            Trip("Museum Run", "Discover a series of Manila's finest museums", [TripNode(0, attractions[0]),
            TripNode(1, attractions[1]),
            TripNode(2, attractions[2])
            ], "http://www.mcadmanila.org.ph/wp-content/uploads/2016/11/MCAD-SDA-1024x630-e1479456928953.jpg"),
            Trip("Bargain and Bites", "Find the cheapest and most delicious eats in the city.", [], "https://www.kawalingpinoy.com/wp-content/uploads/2013/07/tokneneng2680.jpg")
        ]

    def toDict(self):
        return [trip.toDict() for trip in self.trips] 