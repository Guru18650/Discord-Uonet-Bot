import discord, os, requests, json
from dotenv import load_dotenv

load_dotenv()

def GetWeatherEmbed():
    w_response = requests.get(os.getenv("W_URL")+"appid="+os.getenv("W_KEY")+"&q="+os.getenv("W_CITY")+"&lang="+os.getenv("W_LANGUAGE")+"&units="+os.getenv("W_UNITS"))
    w_json = w_response.json()
    w_parse = w_json["main"]
    w_temperature = w_parse["temp"]
    w_pressure = w_parse["pressure"]
    w_humidity = w_parse["humidity"]
    w_description2 = w_json["weather"]
    w_description = w_description2[0]["description"]
    embed=discord.Embed(title="Pogoda", description="19.09.2022 - "+w_description)
    embed.add_field(name="Temperatura", value=str(w_temperature)+"°C", inline=True)
    embed.add_field(name="Ciśnienie", value=str(w_pressure)+"HPa", inline=True)
    embed.add_field(name="Wilgotność", value=str(w_humidity)+"%", inline=True)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed