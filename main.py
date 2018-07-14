"""
RESTFUL api for Hackatren Bantay Sakay app
:Author:     Jose Salinas
:Author:     Maded Batara III
:Version:    v20180709
"""

from flask import Flask
from flask import jsonify

from flask_cors import CORS

from python.stations import StationsService
from python.trains import TrainsService
from python.statistics import Statistics
from python.attractions import AttractionService

app = Flask(__name__)
CORS(app=app)

#######
# APP #
#######

trains = TrainsService()

@app.route('/api/trains', methods=['GET'])
def get_trains():
    trains.updateTrainsPositionConst()
    trains.updateTrainLoadRandom()
    return jsonify(trains.getAllTrainsDict())

stations = StationsService()

@app.route('/api/stations', methods=['GET'])
def get_station_statistics():
    stations.updateStationsRandom()
    return jsonify(stations.getAllStationsDict())

statistics = Statistics()

@app.route('/api/statistics', methods=['GET'])
def get_global_statistics():
    statistics.updateCycleTimeRandom()
    statistics.updateHeadwayTimeRandom()
    return jsonify(statistics.toDict())

attractions = AttractionService()

@app.route('/api/attractions', methods=['GET'])
def get_attractions():
    return jsonify(attractions.getAttractions())


if __name__ == "__main__":
    app.run(debug=True)
