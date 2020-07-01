import requests

location_list = [(42.331429, -83.045753, "Detroit"), (8.3405, 115.0920, "Bali"), (15.8700, 100.9925, "Thailand"), (19.4326, 99.1332, "Mexico"), (3.2028, 73.2207, "Maldives"), (4.6796, 55.4920, "Seychelles"), (30.5595, 22.9375, "South Africa"), (21.6940, 71.7979, "Turks & Caicos"), (13.9094, 60.9789, "St. Lucia"), (40.5532, 14.2222, "Capri")]

def get_weather_data(locations):
    weather_data_container = {}
    for location in locations:
      url = 'https://api.climacell.co/v3/weather/realtime'
      payload = {
      "apikey": "LJZjloQdl5xFnLinzC1I12n7WKEvHG8R", 
      "lat": location[0],
      "lon": location[1],
      "fields":["temp", "precipitation"],
      "unit_system":"us",
  }
      response = requests.get(url, params=payload).json()

      weather_data_container[location[2]] = response["temp"] ["value"]
 
    
    for country, temp, in weather_data_container.items():
      print(f"The temp is {temp} in {country}.")
    return weather_data_container








# class Places:
#   def __init__(self, lat, lon, name):
#   self.lat = lat
#   self.lon = lon
#   self.name = name