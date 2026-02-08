import os
import requests
import datetime

class FlightData:
    def get_flight_prices(self, city, city_code, departure_city):
        tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")

        url = "https://tequila-api.kiwi.com/v2/search"
        headers = {
            "apikey": os.getenv("KIWI_API_KEY")
        }
        params = {
            "fly_from": departure_city,
            "fly_to": city_code,
            "date_from": tomorrow,
            "date_to": six_months
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()["data"][0]["price"]
