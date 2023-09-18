from datetime import datetime, timedelta
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import calendar
import requests
import serial
import time


class Model():

    def __init__(self):
        self.sen_list = []
        self.set_list()
        self.s = serial.Serial('/dev/ttyACM0', 9600)
        pass

    def __del__(self):
        pass

    def datetime_info(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        curr_day = datetime.today()
        day_format = calendar.day_name[curr_day.weekday()]
        day_num = curr_day.strftime("%d")
        month_format = curr_day.strftime("%B")
        year_format = curr_day.strftime("%Y")
        mo_d_y = str(month_format) + " " + str(day_num) + ", " + str(year_format)
        return day_format, mo_d_y, current_time
    
    def weather_info(self):
        api_key = "Insert your API-Key here"
        url = "http://api.weatherapi.com/v1/current.json?"
        city_norm = "Insert your City or Village here"
        parameters = {"q": city_norm, "key": api_key, "aqi": "no"}
        response = requests.get(url, params=parameters)
        weather_data = response.json()
        weather = str(weather_data["current"]["temp_c"])
        info = str(weather_data["current"]["condition"]["text"]) + ", " + weather + " °C"
        url = "http://api.weatherapi.com/v1/forecast.json?"
        tomorrow = datetime.today() + timedelta(days=1)
        date_str = tomorrow.strftime("%Y-%m-%d")
        parameters = {"q": city_norm, "key": api_key, "aqi": "no", "days": "2", "dt": date_str}
        response = requests.get(url, params=parameters)
        weather_data = response.json()
        text_forecast   = weather_data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
        max_temp        = weather_data["forecast"]["forecastday"][0]["day"]["maxtemp_c"] 
        min_temp        = weather_data["forecast"]["forecastday"][0]["day"]["mintemp_c"] 
        rain_forecast   = weather_data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"]

        forecast = "" + str(text_forecast) + ", " + str(rain_forecast) + " mm."
        temp = "" + str(min_temp) + "°C to " + str(max_temp) + " °C"

        return city_norm, info, forecast, temp
    
    def set_list(self):
        self.sen_list.append("Einen wunderschönen min Jung!")
        self.sen_list.append("Grüß Gott!")
        self.sen_list.append("Sei gegrüßt edler Herr!")
        self.sen_list.append("Servus, schick siehste aus!")
        self.sen_list.append("Hallo mein junger Padawan!")
        self.sen_list.append("Moin moin, schönen guten Tag erstmal!")
        self.sen_list.append("Alles Roger in Kambodscha?")
        self.sen_list.append("Good Morning in the Morning!")
        self.sen_list.append("Grüßli Müsli!")
        self.sen_list.append("Hola, lange nicht gesehen, und doch wiedererkannt!")
        self.sen_list.append("Whazuuuuuuuup?")
        self.sen_list.append("Tacho, na wie ist die Lage?")
        self.sen_list.append("Hier Spiegel, wer dort?")
        self.sen_list.append("Ahoi Kapitano, alles in Lot auf'm Boot?")
        self.sen_list.append("It's me, MARIO! Ne Spaß ich bin nur ein Spiegel. Grüß dich!")
        self.sen_list.append("It's me, MARIO! No I'm joking, I'm just a mirror. Whazzuuuup??")

# %%
