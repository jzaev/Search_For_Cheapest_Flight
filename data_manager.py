import requests
import pandas as pd
import flight_search

SHEETY_ENDPOINT = "https://api.sheety.co/3d23ea4e18c396d229e076b5fb916d12/flightDeals/prices"
BEARER_KEY = "23094568g2-n0679bn2-06972-0697pogjipo"
SHEET_HEADER = {"Authorization": f"Bearer {BEARER_KEY}"}


def json_to_table(json_data):
    cities, codes, prices = [], [], []
    city_query = flight_search.FlightSearch()
    for row in json_data["prices"]:
        cities.append(row["city"])
        codes.append(city_query.get_destination_code(city_name=row["city"]))
        prices.append(row["lowestPrice"])
    df = pd.DataFrame({"city": cities, "iataCode": codes, "lowestPrice": prices})
    return df


class DataManager:

    def __init__(self):
        respond = requests.get(url=SHEETY_ENDPOINT, headers=SHEET_HEADER)
        self.table = json_to_table(respond.json())
        self.save_data()

    def save_data(self):
        for row in self.table.iterrows():
            json_data = {
                "price": {
                    "iataCode": row[1]["iataCode"]
                }
            }
            respond = requests.put(url=f"{SHEETY_ENDPOINT}/{row[0] + 2}", headers=SHEET_HEADER, json=json_data)
            respond.raise_for_status()
