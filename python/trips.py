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

    def __init__(self, name, description, tripNodes):
        self.name = name
        self.description = description
        self.tripNodes = tripNodes

    def toDict(self):
        return {
            "name": self.name,
            "description": self.description,
            "nodes": [tripNode.toDict() for tripNode in self.tripNodes]
            }

class Trips:

    def __init__(self, attractions):
        self.trips = [
            Trip("Museum Run", "description", [TripNode(0, attractions[0])

            ])
        ]

    def toDict(self):
        return [trip.toDict() for trip in self.trips] 