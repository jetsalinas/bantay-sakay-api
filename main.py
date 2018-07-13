"""
RESTFUL api for Hackatren Bantay Sakay app
:Author:     Jose Salinas
:Author:     Maded Batara III
:Version:    v20180709
"""

from flask import Flask
from flask import jsonify

from python.stations import StationsService
from python.trains import TrainsService

app = Flask(__name__)

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

@app.route('/api/statistics', methods=['GET'])
def get_global_statistics():
    pass

if __name__ == "__main__":
    app.run(debug=True)
