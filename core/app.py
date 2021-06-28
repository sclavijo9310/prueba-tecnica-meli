from flask import Flask, jsonify, request, abort
from core.functions import get_message, get_location, validate_data
from core.data import satellites_data as satellites
from core.exceptions import SatelliteNotFound, MissingData

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def common_response():
    try:
        validate_data()  # Raise exception if information is incomplete
    except MissingData:
        return abort(404, 'Satellite data is incomplete')

    x, y = get_location([satellite.distance for satellite in satellites])
    return jsonify({
        "position": {
            "x": x,
            "y": y
        },
        "message": get_message([satellite.message for satellite in satellites])
    })


@app.route('/')
def index():
    return jsonify({'message': 'Online and ready'})


@app.route('/topsecret/', methods=['POST'])
@app.route('/topsecret-split/', methods=['POST'])
def topsecret():
    for raw_data in request.json['satellites']:
        satellites_found = [satellite for satellite in satellites if satellite.name == raw_data['name']]
        if len(satellites_found) > 0:
            try:
                satellites_found[0].distance = raw_data['distance']
                satellites_found[0].message = raw_data['message']
            except KeyError:
                return abort(422, 'Missing information')
        else:
            raise SatelliteNotFound('No satellite found with name "{}"'.format(raw_data['name']))

    return common_response()


@app.route('/topsecret-split/')
def topsecret_split_info():
    return common_response()


@app.route('/topsecret-split/<string:satellite_name>', methods=['POST'])
def topsecret_split(satellite_name):
    satellites_found = [satellite for satellite in satellites if satellite.name == satellite_name]
    if len(satellites_found) > 0:
        try:
            satellites_found[0].distance = request.json['distance']
            satellites_found[0].message = request.json['message']
        except KeyError:
            return abort(422, 'Missing information')
    else:
        raise SatelliteNotFound('No satellite found with name "{}"'.format(satellite_name))

    return jsonify({'message': 'success'})


@app.route('/topsecret/', methods=['DELETE'])
def delete_data():
    for satellite in satellites:
        satellite.distance = None
        satellite.message = None

    return jsonify({'message': 'data successfully removed'})


@app.route('/topsecret-split/<string:satellite_name>', methods=['DELETE'])
def delete_satellite_data(satellite_name):
    satellites_found = [satellite for satellite in satellites if satellite.name == satellite_name]
    if len(satellites_found) > 0:
        satellites_found[0].distance = None
        satellites_found[0].message = None
    else:
        raise SatelliteNotFound('No satellite found with name "{}"'.format(satellite_name))

    return jsonify({'message': 'data successfully removed'})


@app.errorhandler(SatelliteNotFound)
def handle_invalid_data_error(e):
    return str(e), 404
