import requests
import datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "XyEXu-MkOSlgnsIvc_VAn8XHbnlq8t18"

SEARCH_API = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def searh_flight(self, fly_to, max_price, fly_from="TLV"):
        date_from = datetime.datetime.now().strftime("%d/%m/%Y")
        date_to = (datetime.datetime.now()+datetime.timedelta(days=10)).strftime("%d/%m/%Y")
        query = {"fly_from": fly_from,
                 "fly_to": fly_to,
                 "dateFrom": date_from,
                 "dateTo": date_to,
                 "one_per_date": 1,
                 "price_to": max_price,
                 "curr": "USD",
                 "max_stopovers": 0,
                 }
        location_endpoint = SEARCH_API
        headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()
        return results
