import requests


class DataManager:
    def __init__(self):
        self.i = 2
        self.city_list = ["ory", "txl", "hnd", "syd", "ist", "kul", "jfk", "sfo", "cpt"]
        self.sheety_url = "https://api.sheety.co/79307bbe3f20c2bb00efab1233f62976/flights/sheet1"
        self.headers = {
                        "Authorization": "Bearer 8810nky7988",
                        "Content-Type": "application/json"
                        }

    def requesting(self):
        for iata in self.city_list:
            data = {
                "sheet1": {
                    "iata": str(iata.upper())
                }
            }
            response = requests.put(url=f"{self.sheety_url}/{self.i}", json=data, headers=self.headers)
            self.i += 1

    def getting_data(self):
        response = requests.get(url=self.sheety_url, headers=self.headers)
        return response.json()




