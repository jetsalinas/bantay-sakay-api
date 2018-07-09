"""
RESTFUL api for Hackatren Bantay Sakay app
:Author:     Jose Salinas
:Author:     Maded Batara III
:Version:    v20180709
"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)

#######
# APP #
#######

@app.route('/api/trains', methods=['GET'])
def get_trains():
    pass

@app.route('/api/stations', methods=['GET'])
def get_station_statistics():
    stations = {
        "0": {
            "name": "Baclaran",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "1": {
            "name": "EDSA",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
       "2": {
            "name": "Libertad",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "3": {
            "name": "Gil Puyat",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "4": {
            "name": "Vito Cruz",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "5": {
            "name": "Quirino",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "6": {
            "name": "Pedro Gil",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "7": {
            "name": "UN Avenue",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "8": {
            "name": "Central",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "9": {
            "name": "Carriedo",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "10": {
            "name": "Doroteo Jose",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "11": {
            "name": "Bambang",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "12": {
            "name": "Tayuman",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "13": {
            "name": "Blumentritt",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "14": {
            "name": "Abad Santos",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "15": {
            "name": "R. Papa",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "16": {
            "name": "5th Avenue",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "17": {
            "name": "Monumento",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "18": {
            "name": "Balitntawak",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        },
        "19": {
            "name": "Roosevelt",
            "latitude": 0,
            "longitude": 0,
            "position": 0,
            "stationLoad": 0
        }
    }

    return jsonify(stations)

@app.route('/api/statistics', methods=['GET'])
def get_global_statistics():
    pass

if __name__ == "__main__":
    app.run(debug=True)
