from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

notification_manager = NotificationManager()
data_manager = DataManager()
data = FlightSearch()

flight_deals = [] #STORES FLIGHT OBJECTS FOUND

destinations = data_manager.get_destination_data()

for destination in destinations:
    city = destination['city']
    destination_code = destination['iataCode']
    target_price = destination['lowestPrice']
    id = destination['id']





    data_list = (data.search_flight(
        "NBO",
        destination_code,
        "2026-11-15",
        "2026-11-22"
    ))
    best_flights = data_list.get('best_flights',[])
    if best_flights:

        cheapest_flight = min(best_flights,key=lambda flight: flight['price'])
        flight_segments = cheapest_flight['flights']
        departure_airport = flight_segments[0]['departure_airport']['id']
        destination_airport = flight_segments[-1]['arrival_airport']['id']
        departure_time = flight_segments[0]['departure_airport']['time'].split()[0]
        current_price = cheapest_flight['price']

        if current_price < target_price:
            print("flight deal found")
            flight_data = FlightData(price=current_price,origin_airport=departure_airport,destination_airport=destination_airport,out_date=departure_time,return_date="not decided")
            flight_deals.append(flight_data)
            for flight in flight_deals:
                data_manager.update_destination_price(destination_id=id,new_price=current_price)
                message = (
                    f"From: {flight.origin_airport}\n"
                    f"To: {flight.destination_airport}\n"
                    f"Departure: {flight.out_date}\n"
                    f"Return: {flight.return_date}\n"
                    f"Price: {flight.price}"
                )
                notification_manager.send_email(message=message)
                print("Email sent")

    else:
        print("No flights are currently available")




