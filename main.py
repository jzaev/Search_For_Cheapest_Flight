import data_manager
import flight_search

my_cities = data_manager.DataManager()

search_query = flight_search.FlightSearch()

for city in my_cities.table.iterrows():
    res = search_query.searh_flight(fly_to=city["iataCode"],max_price=city["lowestPrice"])
    for data in res["data"]:
        print("=======================================================================")
        print(len(data))
        print(data["price"])
        print(data["route"][0]["local_departure"])
        print(data["route"][0]["airline"])
        print(data["route"][0]["flight_no"])

