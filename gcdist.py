# curl "https://nominatim.openstreetmap.org/search?q=south+pole&format=json?limit=1"
import requests
import sys
from math import sqrt, sin, cos, atan2, pi

def lookup(placename):

    url = "https://nominatim.openstreetmap.org/search?q=south+pole&format=json?limit=1"
    params = dict(limit=1, format="json", q=placename.replace(" ", "+"))
    # defining a params dict for the parameters to be sent to the API

    r = requests.get(url=url, params=params)

    # extracting data in json format
    data = r.json()[0]

    lat = float(data['lat'])
    lon = float(data['lon'])
    print(f"{data['display_name']}: lat={lat}, lon={lon}")
    return lat * pi/180, lon * pi/180

φ1, λ1 = lookup(sys.argv[1])  # lat, lon
φ2, λ2 = lookup(sys.argv[2])  # lat, lon

R = 6371.009 # mean Earth radius

# https://en.wikipedia.org/wiki/Great-circle_distance
# lambda = lon
# phi = lat
# melb - syd is 877.8 according to google

Δλ = abs(λ1 - λ2)

Δσ = atan2(
        sqrt(
        (cos(φ2) * sin(Δλ))**2 +
        (cos(φ1) * sin(φ2) - sin(φ1) * cos(φ2) * cos(Δλ))**2
        ),
        (sin(φ1) * sin(φ2) + cos(φ1) * cos(φ2) * cos(Δλ))
    )

d = Δσ * R
print(f"{d:.1f} km")


