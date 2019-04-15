import requests

def weather_api(name):
    api = "https://api.openweathermap.org/data/2.5/weather?appid=db704c84db1df1022e65f4274a8c5feb&q="
    city_name = name
    url = api + city_name + "&units=metric"
    return requests.get(url).json() #takes in the url and gets data back in JSON form

def quotes_api():
    
    return requests.get("https://quotes.rest/qod").json()
