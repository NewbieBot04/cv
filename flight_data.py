class FlightData:
    def __init__(self, data):
        self.data = data

    def processing(self):
        try:
            from_ = self.data["data"][1]["cityFrom"]
            to_destination = self.data["data"][2]["cityTo"]
            fair = self.data["data"][5]["price"]
            availability = self.data["data"][7]["availability"]["seats"]
            return from_, to_destination, fair, availability
        except IndexError:
            return False






