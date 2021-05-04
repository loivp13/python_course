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




# folium instance
mymap = Map(location = [40, 2])


# geopoint instance
locations = [[41,-1],[40,2],[39,5]]
for loc in locations:
    geopoint = Geopoint(latitude=loc[0], longitude= loc[1])
    forecast = geopoint.get_weather()
    popup_content = f"""
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°F <img src='https://clipground.com/images/weather-icon-transparent-png-5.jpg' width = 35>
    <hr style='margin:1px'>
    {forecast[1][0][-8:-6]}h:{round(forecast[1][1])}°F <img src='https://clipground.com/images/weather-icon-transparent-png-5.jpg' width = 35>
    <hr style='margin:1px'>
    {forecast[2][0][-8:-6]}h:{round(forecast[2][1])}°F <img src='https://clipground.com/images/weather-icon-transparent-png-5.jpg' width = 35>
    <hr style='margin:1px'>
    {forecast[3][0][-8:-6]}h:{round(forecast[3][1])}°F <img src='https://clipground.com/images/weather-icon-transparent-png-5.jpg' width = 35>
    <hr style='margin:1px'>
    """

    popup = Popup(popup_content,max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)

mymap.save('map.html')
