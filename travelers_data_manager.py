import requests

sheety_url = "https://api.sheety.co/165790edc2c86e0c509997aaac06aa3b/travlerdata/sheet1"
sheety_token = "Bearer 8810nky7988"


class TravelerData:
    def __init__(self, f_name, l_name, email, index):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.index = index
        self.headers = {
            "Authorization": "Bearer 8810nky7988",
            "Content-Type": "application/json"
        }

        self.query = {
            "sheet1": {
                "firstName": self.f_name,
                "lastName": self.l_name,
                "email": self.email

            }

        }
        self.adding_data()

    def adding_data(self):
        response = requests.put(url=f"{sheety_url}/{self.index}", json=self.query, headers=self.headers)
        print(response.text)