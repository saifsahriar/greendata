
![Logo](https://user-images.githubusercontent.com/77581157/236961390-9b0e5c0e-13d5-43e5-b14c-0bd6ca1dd214.png)



# Green Data

A brief description of what this project does and who it's for


## Problem Statement
Develop an app to analyse the data from the weather and use a predictive algorithm to draw a pattern of weather scenarios at any given area and send it as a text message to a list of mobile numbers within the vicinity of that area.

## Documentation
We have made a weather forecast and warning app and website that shows weather data and Warns on any forcasted warnings and also we have made our own AI model that suggests precautions and recommendations for crops based on the weather data.

Our AI is running on the collab file [link](https://colab.research.google.com/drive/1_poiJnmHmg8IPm7AsL1cFJNi3vjAZkgj?usp=sharing)

Our Flask Server and Load balancer is running on Replit [link](https://replit.com/@JeetGhosh3/Weather)

And we push messages and Warnings through Twillo by scanning weather data of every city and pusing sms to all numbers associated to that city or location.
## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## API Reference

#### Get all items

```http
  GET https://weather.jeetghosh3.repl.co/report/?name=Jeet&city=kolkata&phone=900000&pin=700000&crop=Rice
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**. Your name |
| `city` | `string` | **Required**. Your city |
| `phone` | `string` | **Required**. Your phone number |
| `pin` | `string` | **Required**. Your pin |
| `Crop` | `string` | **Required**. The Crop name |



#### Get the json data example
`{
"Name": "Jeet",
"Response": "Suggestions for growing rice under these conditions include using shade cloth to protect plants from direct sunlight, planting early varieties of rice such as Basmati or Jasmine, and applying fertilizers regularly",
"Weather": {
"City": "kolkata",
"Clouds": 20,
"Humidity": 74,
"Pressure": 1003,
"Rain_Volume": 0,
"Temp_in_Celcius": 31.12,
"Temp_in_kelvin": 304.12,
"Warnings": "No Warnings",
"Weather_Description": "haze",
"Wind_Direction": 180,
"Wind_Speed": 1.54,
"weather_type": "Haze"
},
"crop": "Rice"
}`


## Running Guide

Click on the [link](https://saifsahriar.github.io/greendata/) and enter the data and then wait for few seconds to let the app call the api and get the data.

It will redirect you to a next page thet will show all the data.

Also, You can navigate using the manu bar
    
## Tech Stack

**Client:** HTML, CSS, Java Script

**Server:** Python, Flask

**APP** Java, XML

**AI Model** Custom trained LLM


## Screenshots

![Screenshot_20230509_042132](https://user-images.githubusercontent.com/77581157/236961431-470899c8-88e6-4906-96ea-e37e0efc47d2.jpg)
![Screenshot_20230509_042115](https://user-images.githubusercontent.com/77581157/236961427-551552e6-6ec2-444c-84f7-5c5c2728c58f.jpg)


## Features

- Weather Details
- Free API
- Disaster warnings
- AI made suggestion and Recommendation


## Demo

https://user-images.githubusercontent.com/77581157/236961546-9810f392-904d-48b6-8a0a-fc4e7178c935.mp4



