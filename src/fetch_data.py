import os
from dotenv import load_dotenv
import json
import requests
import time
from datetime import timedelta, date


load_dotenv()
API_key = os.getenv("API_key")

url = "https://api.nasa.gov/neo/rest/v1/feed"

all_asteroids=[]

start_date = date(2025,7,1)
end_date = date(2026,7,1)
current = start_date

while current<end_date:
    weekend = current + timedelta(days=7)
    params = {
        "start_date" : current ,
        "end_date" : weekend ,
        "api_key" : API_key
    }
    response=requests.get(url,params=params)

    if response.status_code == 200:
        data=response.json()
        for date in data["near_earth_objects"]:
            for asteroid in data["near_earth_objects"][date]:
                extracts ={
                    "id" : asteroid["id"],
                    "name" : asteroid["name"],
                    "absolute_magnitude" : asteroid["absolute_magnitude_h"],
                    "velocity" : asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"],
                    "diameter_min" : asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                    "diameter_max" : asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    "miss_distance_au" : asteroid["close_approach_data"][0]["miss_distance"]["astronomical"],
                    "is_hazardous" : asteroid["is_potentially_hazardous_asteroid"]
                }
                all_asteroids.append(extracts)
        
        print("SUCCESS")
    elif response.status_code == 429:
        print("Rate limit hit")
    elif response.status_code == 500:
        print("Server down")
    else:
        print(f"Unexpected Error {response.status_code}")
    time.sleep(1)
    current=current + timedelta(days=7)
print(f"Total asteroids collected: {len(all_asteroids)}")

with open(r"d:\Downloads\My code\NASA-Asteroid-Classifier\data\raw_data.json","w") as fp:
    json.dump(all_asteroids,fp,indent=2)