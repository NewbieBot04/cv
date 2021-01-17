import datetime as dt
from notification_manager import NotificationManager
from flight_data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from ui import UserInterface
from travelers_data_manager import TravelerData

ui = UserInterface()
emails = ui.emails
names = ui.names
strip_email = emails[0].strip()
i = 2
for f_name in names:
    split_name = f_name.split()
    traveler_data = TravelerData(f_name=split_name[0].title(), l_name=split_name[1].title(), email=strip_email, index=i)
    i += 1

nxtday_date = dt.datetime.today() + dt.timedelta(days=1)
nxtday = nxtday_date.strftime("%d/%m/%Y")
to_date = "1/3/2021"

data_manager = DataManager()
travel_data = data_manager.getting_data()
new_lst = []
for i in range(len(travel_data["sheet1"])):
    print(i)
    destination_iata_code = travel_data["sheet1"][i]["iata"]
    min_fare = travel_data["sheet1"][i]["lowestPrice"]
    flight_search = FlightSearch(fly_from="DEL", fly_to=destination_iata_code, from_date=nxtday,
                                 to_date=to_date, min_price=min_fare)
    flight_search_data = flight_search.searching()
    flight_data = FlightData(flight_search_data)
    new_lst.append(flight_data.processing())
print(new_lst)

msg_from = ""
msg_to = ""
msg_fair = 0
msg_seats = 0

for i in new_lst:
    if i:
        msg_to = i[1]
        msg_fair = i[2]
        msg_seats = i[3]
    msg = NotificationManager(price=msg_fair, destination=msg_to,
                              from_=nxtday, to_=to_date,
                              available=msg_seats, email=strip_email)
    msg.sending_mail()
