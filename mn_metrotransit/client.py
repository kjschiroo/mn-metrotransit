import requests
from . import constants


class Client(object):
    '''
    Interface for communication with the metro transit API.
    '''
    def __init__(self, host=constants.DEFAULT_HOST):
        self._host = host

    def get_providers(self):
        url_template = '{host}/NexTrip/Providers?format=json'
        args = {'host': self._host}
        return self._get(url_template.format(**args))

    def get_routes(self):
        url_template = '{host}/NexTrip/Routes?format=json'
        args = {'host': self._host}
        return self._get(url_template.format(**args))

    def get_directions(self, route):
        url_template = '{host}/NexTrip/{route}?format=json'
        args = {'host': self._host, 'route': route}
        return self._get(url_template.format(**args))

    def get_stops(self, route, direction):
        url_template = '{host}/NexTrip/Stops/{route}/{direction}?format=json'
        args = {'host': self._host, 'route': route, 'direction': direction}
        return self._get(url_template.format(**args))

    def get_departures(self, stop):
        url_template = '{host}/NexTrip/{stop}?format=json'
        args = {'host': self._host, 'stop': stop}
        return self._get(url_template.format(**args))

    def get_timepoint_departures(self, route, direction, stop):
        url_template = '{host}/NexTrip/{route}/{direction}/{stop}?format=json'
        args = {
            'host': self._host,
            'route': route,
            'direction': direction,
            'stop': stop
        }
        return self._get(url_template.format(**args))

    def get_vehicle_locations(self, route):
        url_template = '{host}/NexTrip/VehicleLocations/{route}?format=json'
        args = {'host': self._host, 'route': route}
        return self._get(url_template.format(**args))

    def _get(self, url):
        response = requests.get(url)
        return response.json()
