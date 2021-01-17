import requests
tequila_app_key = "6kdkZXq6BoCiJWs5xQ-qAiuPUie-nIyS"
tequila_url = "https://api.skypicker.com/flights"


class FlightSearch:
    def __init__(self, fly_from, fly_to, from_date, to_date, min_price):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.from_date = from_date
        self.to_date = to_date
        self.min_price = min_price
        self.parameters = {
            "apikey": tequila_app_key,
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.from_date,
            "date_to": self.to_date,
            "price_to": self.min_price,
            "curr": "INR",
            "vehicle_type ": "aircraft",
            "max_stopovers": 0,
            "partner": "picky"
        }
        self.headers = {
            "Content-Type": "application/json",
            # "Content-Encoding": "gzip"

        }

    def searching(self):
        response = requests.get(url=tequila_url, params=self.parameters, headers=self.headers)
        return response.json()
