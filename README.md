# Great circle distance calculator

```shell
$ gcdist start end
```
will display the great-circle distance in kilometres between the two places.  For example:

```shell
$ python gcdist.py "albany, west australia" "hobart"
Albany, City Of Albany, Western Australia, Australia: lat=-35.0247822, lon=117.883608
Hobart, City of Hobart, Tasmania, 7000, Australia: lat=-42.8825088, lon=147.3281233
2675.6 km
```

Place geolocation is done using OpenStreetMap's Nominatum service.  The display name of the looked up place is displayed as a check that the name is not aliased.  

Uses a spherical world model so probably good to 1% accuracy.
