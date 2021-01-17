import smtplib


class NotificationManager:
    def __init__(self, available, price, destination, from_, to_, email):
        self.available = available
        self.email = email
        self.price = price
        self.destination = destination
        self.from_date = from_
        self.to_date = to_
        self.my_email = "lazyminds.0499@yahoo.com"
        self.password = "kqgxmzyrluvaxofa"

    def sending_mail(self):
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.email,
                                msg=f"Subject:Hurry ! Low price alert!"
                                    f"\n\nFew seats available {self.available}\n"
                                    f" Only Rs.{self.price} to fly from\n"
                                    f"Delhi to {self.destination},from\n {self.from_date} to {self.to_date}",)
            # print(connection.status)








