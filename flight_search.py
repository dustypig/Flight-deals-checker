import os
import requests

class FlightSearch:
    def search_flights(self, city):
        url = "https://tequila-api.kiwi.com/locations/query"
        headers = {
            "apikey": os.getenv("KIWI_API_KEY")
        }
        params = {
            "term": city
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()["locations"][0]["code"]
