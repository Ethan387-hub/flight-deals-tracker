import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
load_dotenv()
USERNAME = os.getenv("SHEETY_USERNAME")
PASSWORD = os.getenv("SHEETY_PASSWORD")
auth = HTTPBasicAuth(USERNAME,PASSWORD)
SHEETY_URL = os.getenv("SHEETY_URL")


class DataManager:
    def __init__(self):
        self.username = USERNAME
        self.password = PASSWORD
        self.end_point = SHEETY_URL
        self.auth = auth
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=self.end_point,auth=self.auth)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_price(self,destination_id,new_price):
        update_endpoint = f"{self.end_point}/{destination_id}"
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(url=update_endpoint,auth=self.auth,json=new_data)
        response.raise_for_status()
        return response.json()

