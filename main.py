"""
RESTFUL api for Hackatren Bantay Sakay app
:Author:     Jose Salinas
:Author:     Maded Batara III
:Version:    v20180709
"""

from flask import Flask
from flask import jsonify

from python.stations import Stations

app = Flask(__name__)

#######
# APP #
#######

@app.route('/api/trains', methods=['GET'])
def get_trains():
    pass

stations = Stations()

@app.route('/api/stations', methods=['GET'])
def get_station_statistics():
    return jsonify(stations.getAllStationsDict())

@app.route('/api/statistics', methods=['GET'])
def get_global_statistics():
    pass

if __name__ == "__main__":
    app.run(debug=True)
