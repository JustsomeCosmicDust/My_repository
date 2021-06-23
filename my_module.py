import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?id=1259229&appid=472ba573bab13d4a9007536bc276a744')


with open('MyPune.txt', 'w') as f:
    f.write(r.text)