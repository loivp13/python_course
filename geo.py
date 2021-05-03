from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker, Map,Popup


class Geopoint(Marker) :

    def __init__(self, latitude, longitude):
        super().__init__(location =[latitude, longitude])
        self.latitude = latitude
        self.longitude = longitude
    
    def closest_parallel(self):
       return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now
    def get_weather(self):
        weather = Weather(apikey='26631f0f41b95fb9f5ac0df9a8f43c92', lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()
    
    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90, 90), longitude = uniform(-180, 180))


latitude = 40.4
longitude = -3.7

# folium instance
mymap = Map(location = [latitude, longitude])

# geopoint instance
geopoint = Geopoint(latitude=latitude, longitude= longitude)
popup = Popup(str(geopoint.get_weather()))
popup.add_to(geopoint)
geopoint.add_to(mymap)

mymap.save('map.html')