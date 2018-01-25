import mn_metrotransit as mn_transit


def test_get_providers_completes():
    client = mn_transit.Client()
    client.get_providers()


def test_get_routes_completes():
    client = mn_transit.Client()
    client.get_routes()


def test_get_directions_completes():
    client = mn_transit.Client()
    client.get_directions(route=0)


def test_get_stops_completes():
    client = mn_transit.Client()
    client.get_stops(route=5, direction=4)


def test_get_departures_completes():
    client = mn_transit.Client()
    client.get_departures(stop=11167)


def test_get_timepoint_departures():
    client = mn_transit.Client()
    client.get_timepoint_departures(route=5, direction=4, stop='7SOL')


def test_get_vehicle_locations_completes():
    client = mn_transit.Client()
    client.get_vehicle_locations(route=5)
