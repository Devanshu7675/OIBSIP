import requests,json,sys

if len(sys.argv)<2:
    print("Usage: weather_forecast.py location")
    sys.exit()

location = ''.join(sys.argv[1:])
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=2f7ab5edd855d6be8ef45c314254e8e0" % location
response = requests.get(url)
response.raise_for_status()

data = json.loads(response.text)

# print(data)

show = data['weather']
print('Current weather in %s:' % (location))
print(show[0]['main'], "-",show[0]['description'])

temp = data['main']
print('Temperature is:', temp['temp']-273.15, "°C")

humidity = data['main']
print('Humidity is:' , humidity['humidity'],"%")
print()