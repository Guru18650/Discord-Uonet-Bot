import discord, os, requests, json
from dotenv import load_dotenv
from datetime import date

load_dotenv()

weekdays = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

def GetAQI(aqi):
    if(aqi<=50):
        return "Dobra"
    if(aqi<=100):
        return "Umiarkowana"
    if(aqi<=150):
        return "Niedobra"
    if(aqi<=200):
        return "Zła"
    if(aqi<=300):
        return "Bardzo zła"
    if(aqi<=500):
        return "Tragiczna, zagrożenie!"
def GetNewDayEmbed():
    w_response = requests.get(os.getenv("W_URL")+"appid="+os.getenv("W_KEY")+"&q="+os.getenv("W_CITY")+"&lang="+os.getenv("W_LANGUAGE")+"&units="+os.getenv("W_UNITS"))
    w_json = w_response.json()
    w_parse = w_json["main"]
    w_temperature = w_parse["temp"]
    w_pressure = w_parse["pressure"]
    w_humidity = w_parse["humidity"]
    w_description2 = w_json["weather"]
    w_description = w_description2[0]["description"]
    embed=discord.Embed(title=weekdays[date.today().weekday()] + " - " + str(date.today()), description=w_description)
    embed.add_field(name="Temperatura", value=str(w_temperature)+"°C", inline=True)
    embed.add_field(name="Ciśnienie", value=str(w_pressure)+"HPa", inline=True)
    embed.add_field(name="Wilgotność", value=str(w_humidity)+"%", inline=True)
    embed.add_field(name="Ubierz dzisiaj kurtke i czapke, kiedyś mi podziękujesz", value="Powodzenia na lekcjach i miłego dnia!", inline=False)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed

def GetWeatherEmbed():
    w_response = requests.get(os.getenv("W_URL")+"appid="+os.getenv("W_KEY")+"&q="+os.getenv("W_CITY")+"&lang="+os.getenv("W_LANGUAGE")+"&units="+os.getenv("W_UNITS"))
    w_aq_response = requests.get(os.getenv("AQ_URL")+os.getenv("AQ_KEY"))
    w_json = w_response.json()
    w_parse = w_json["main"]
    w_temperature = w_parse["temp"]
    w_pressure = w_parse["pressure"]
    w_humidity = w_parse["humidity"]
    w_description2 = w_json["weather"]
    w_description = w_description2[0]["description"]
    embed=discord.Embed(title=weekdays[date.today().weekday()] + " - " + str(date.today()), description=w_description)
    embed.add_field(name="Temperatura", value=str(w_temperature)+"°C", inline=True)
    embed.add_field(name="Ciśnienie", value=str(w_pressure)+"HPa", inline=True)
    embed.add_field(name="Wilgotność", value=str(w_humidity)+"%", inline=True)
    embed.add_field(name="Jakość powietrza", value=str(w_aq_response.json()["data"]["current"]["pollution"]["aqius"])+"AQI; "+GetAQI(w_aq_response.json()["data"]["current"]["pollution"]["aqius"]), inline=True)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed