import requests, json
w_response = requests.get("http://api.airvisual.com/v2/city?city=katowice&state=silesia&country=poland&key=945ef6f0-7f53-4d26-a4e8-736a88e40f3c")
w_json = w_response.json()
print(w_json["data"])