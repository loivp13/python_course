from folium import Map
from geo import Geopoint

latitude = 40.09
longitude = -3.47


antipode_latitude = latitude * (-1)

if longitude <= 0:
    antipode_longitude = longitude + (180)
else:
    antipode_longitude = longitude - (180)

location = [antipode_latitude, antipode_longitude]
myMap = Map(location)
myMap.save(str('antipode.html'))

mypoint = Geopoint(41.2, 4.1)
mypoint2 = Geopoint(41.3, 24.1)

print(antipode_latitude)
print(antipode_longitude)
print(mypoint.closest_parallel())
print(mypoint2.closest_parallel())