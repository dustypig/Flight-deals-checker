from data_manager import DataManager
from flight_data import FlightData

DEPARTURE_CITY = "London"
DEPARTURE_CITY_IATA = "LON"

def check_flights():
    manager = DataManager()
    data = manager.get_sheets()
    alerts = []

    for row in data:
        price = FlightData().get_flight_prices(
            row["city"],
            row["iataCode"],
            DEPARTURE_CITY_IATA
        )

        if price < row["lowestPrice"]:
            alerts.append(
                f"✈️ **Low Price Alert**\n"
                f"{DEPARTURE_CITY} → {row['city']}\n"
                f"💰 {price}$"
            )

    return alerts
