from flask import Flask, jsonify, request, abort
from core.functions import get_message, get_location, validate_data
from core.data import satellites_data as satellites
from core.models import Satellite
from core.exceptions import SatelliteNotFound, MissingData
from google.cloud import datastore

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def common_response(data=satellites):
    try:
        validate_data(data)  # Raise exception if information is incomplete
    except MissingData:
        return abort(404, 'Satellite data is incomplete')

    x, y = get_location([satellite.distance for satellite in data])
    return jsonify({
        "position": {
            "x": x,
            "y": y
        },
        "message": get_message([satellite.message for satellite in data])
    })


@app.route('/')
def index():
    return jsonify({'message': 'Online and ready'})


@app.route('/topsecret/', methods=['POST'])
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
    client = datastore.Client()

    with client.transaction():
        data = client.get_multi([
            client.key('Satellite', 'kenobi'),
            client.key('Satellite', 'skywalker'),
            client.key('Satellite', 'sato')
        ])

    data_satellites = []

    for entity in data:
        data_satellites.append(Satellite('', entity['x'], entity['y'], entity['distance'], entity['message']))

    return common_response(data_satellites)


@app.route('/topsecret-split/', methods=['POST'])
def topsecret_post():
    client = datastore.Client()

    for raw_data in request.json['satellites']:
        with client.transaction():
            key = client.key('Satellite', raw_data['name'])
            satellite = client.get(key)
            if satellite is None:
                raise SatelliteNotFound('No satellite found with name "{}"'.format(raw_data['name']))
            else:
                satellite['distance'] = raw_data['distance']
                satellite['message'] = raw_data['message']
                client.put(satellite)

    data = client.get_multi([
        client.key('Satellite', 'kenobi'),
        client.key('Satellite', 'skywalker'),
        client.key('Satellite', 'sato')
    ])

    return common_response(data)


@app.route('/topsecret-split/<string:satellite_name>', methods=['POST'])
def topsecret_split(satellite_name):
    client = datastore.Client()

    with client.transaction():
        key = client.key('Satellite', satellite_name)
        satellite = client.get(key)
        if satellite is None:
            raise SatelliteNotFound('No satellite found with name "{}"'.format(satellite_name))
        else:
            try:
                satellite['distance'] = request.json['distance']
                satellite['message'] = request.json['message']
            except KeyError:
                return abort(422, 'Missing information')
            client.put(satellite)

    return jsonify({'message': 'success'})


@app.route('/topsecret-split/<string:satellite_name>', methods=['DELETE'])
def delete_satellite_data(satellite_name):
    client = datastore.Client()

    with client.transaction():
        key = client.key('Satellite', satellite_name)
        satellite = client.get(key)
        if satellite is None:
            raise SatelliteNotFound('No satellite found with name "{}"'.format(satellite_name))
        else:
            satellite['distance'] = None
            satellite['message'] = None
            client.put(satellite)

    return jsonify({'message': 'data successfully removed'})


@app.errorhandler(SatelliteNotFound)
def handle_invalid_data_error(e):
    return str(e), 404
