import requests
import os
from dotenv import load_dotenv
load_dotenv()
SERPAPI_ENDPOINT = "https://serpapi.com/search?engine=google_flights"

class FlightSearch:
    def __init__(self):
        self.endpoint = SERPAPI_ENDPOINT
        self.api_key = os.getenv("SERPAPI_API_KEY")

    def search_flight(self, departure_id, arrival_id, outbound_date, return_date):
        parameters = {
        "engine": "google_flights",
        "api_key": self.api_key,
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "type": "1",
        "currency": "USD",
        "hl": "en"
    }
        response = requests.get(url=self.endpoint,params=parameters)
        data = response.json()
        return data
