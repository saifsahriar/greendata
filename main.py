from flask import Flask, request, jsonify
import requests
import random
import decimal
from flask_cors import CORS ,cross_origin
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv
# import vonage
# dotenv_path = join(dirname(__file__), "../.env")
# load_dotenv(dotenv_path)

# import nexmo

# client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

# if responseData["messages"][0]["status"] == "0":
#     print("Message sent successfully.")
# else:
#     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "Your API key"
CITY = "New York"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY


#function to convert kelvin to celcius
def k2C(N):
  c1 = N - 273
  decimal_value = decimal.Decimal(c1)

  c3 = decimal_value.quantize(decimal.Decimal('0.00'))
  c = float(c3)
  return c


def Weatherget(city):
  url = BASE_URL + "appid=" + API_KEY + "&q=" + city
  response = requests.get(url).json()
  # print(response)

  #getting the temp
  temp_kelvin = response['main']['temp']
  temp_celcius = k2C(temp_kelvin)
  max_temp = k2C(response['main']['temp_max'])
  min_temp = k2C(response['main']['temp_min'])

  #getting pressure and humidity
  pressure = response['main']['pressure']
  humidity = response['main']['humidity']

  #getting weather type
  weathertype = response['weather'][0]['main']
  weatherdesc = response['weather'][0]['description']

  #if rain occurs the give me the rain mm
  if weathertype == "rain":
    rainvol = response['rain']['1h']
  else:
    rainvol = 0

  #getting wind value
  windspeed = response['wind']['speed']
  wind_degree = response['wind']['deg']

  #cloud data
  cloud = response['clouds']['all']

  W = "No Warnings"

  #warnings
  if rainvol >= 100:
    W = "Flood incoming"
  elif rainvol >= 50:
    W = "The heavy rain fall may damage the crops"
  elif windspeed >= 33.33:
    W = "Cyclone incoming"
  elif max_temp >= 39.0:
    W = "There is a heate wave going in the region"
  elif min_temp <= 10.0:
    W = "There is a cold wave going in the region"

  A = {
    "City": city,
    "Temp_in_kelvin": temp_kelvin,
    "Temp_in_Celcius": temp_celcius,
    "Warnings": W,
    "Pressure": pressure,
    "Humidity": humidity,
    "weather_type": weathertype,
    "Weather_Description": weatherdesc,
    "Rain_Volume": rainvol,
    "Wind_Speed": windspeed,
    "Wind_Direction": wind_degree,
    "Clouds": cloud
  }
  return [A, rainvol, temp_celcius, Warning]
  # print(A)


# Weatherget(CITY)

# Url="https://8dca-34-143-181-58.ngrok-free.app/report/?name=Jeet&city=kolkata&ph=8900606201&crop=Rice&pin=0"
# print(requests. get(Url).json())
app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Flask!'


# @app.route('/report/')
# def report(na=None):
#   n = request.args
#   A=n['name']
#   B=n['ph']
#   C=n['city']
#   D=n['pin']
#   E=n['crop']
#   extd=f"/report/?name={A}&ph={B}&city={C}&crop={E}"
#   url= F+extd
#   response = requests. get(url).json()
#   return response
@app.route('/report/')
@cross_origin(supports_credentials=True)
def report(na=None):
  n = request.args
  A = n['name']
  B = n['phone']
  C = n['city']
  D = n['pin']
  E = n['crop']
  Z1 = Weatherget(C)
  Z = Z1[0]
  rain = Z1[1]
  print(rain)
  # Crops = "Rice"
  crop = E
  if crop == "Rice" or "rice" and rain >= 100:
    Re = "The crops might get destroied try to drain the water out of the field."
  if crop == "Rice" or "rice":
    Re = "Suggestions for growing rice under these conditions include using shade cloth to protect plants from direct sunlight, planting early varieties of rice such as Basmati or Jasmine, and applying fertilizers regularly"
  elif crop == "Potato" or "potato" and rain >= 50:
    Re = "The crops might get destroied try to drain the water out of the field."
  elif crop == "Potato" or "potato":
    Re = "Suggestions for growing rice under these conditions include using irrigation to ensure adequate water supply, planting early so as not to be affected by frost or late-season rains, and choosing varieties suited to your climate"
  elif crop == "Wheat" or "wheat":
    Re = "Suggestions for growing rice under these conditions include using irrigation to ensure adequate water supply, planting early so as not to be affected by frost or late-season rains, and choosing varieties suited to your climate"
  D = {"Name": A, "Weather": Z, "Response": Re, "crop": E}
  # client = vonage.Client(key="233854f3", secret="ja80Tjf0NpZCsy56")
  # sms = vonage.Sms(client)# sms = vonage.Sms(client)
  # NEXMO_API_KEY = "****"
  # NEXMO_API_SECRET = "**"
  # TO_NUMBER = B
  # NEXMO_BRAND_NAME = 'Green Data'
  # responseData = sms.send_message(
  #   {
  #       "from": NEXMO_BRAND_NAME,
  #       "to": TO_NUMBER,
  #       "text": f" Hello {A} City: {C} Crop: {E} Warnings: {Z1[3]} Suggestions: {Re}",
  #   }
  # )
  return jsonify(D)


app.run(host='0.0.0.0', port=81)
