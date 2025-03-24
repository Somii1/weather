import requests
# API atslēga un URL
api_key = '4befee2e32534a6691c81340252103'  # Aizstāj ar savu API atslēgu
city = input("Enter city name: ")
url = f'http://api.weatherapi.com/v1/forecast.json?key=4befee2e32534a6691c81340252103&q={city}&days=10&aqi=yes&alerts=non'
# Veikt GET pieprasījumu
response = requests.get(url)
# Pārbaudīt atbildes statusu
if response.status_code == 200:
    print("Dati iegūti veiksmīgi!")
    data = response.json() 
    print(data)
   # temperature = data['current']['temp_c']
    
    #print(temperature)
    #umidity = data['main']['humidity']
    #weather_description = data['weather'][0]['description']
   # print(f"Temperatūra: {temperature}°C")
    #print(f"Mitrums: {humidity}%")
    #print(f"Laikapstākļi: {weather_description}") # Atgriezt datus JSON formātā
def main():

# Iegūst laika apstākļu datus
    #weather_data = 'get_weather_data'()
    print(data["location"]["name"])
# Izdrukā datus
    #print_weather(weather_data) 
if __name__ == "__main__":
 main()
