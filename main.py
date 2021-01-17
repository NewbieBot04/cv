from bs4 import BeautifulSoup
import requests
import smtplib

email = "lazyminds.0499@gmail.com"
password = "8810nky@#0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
           }
url = "https://www.amazon.in/AmazonBasics-Full-Size-Ergonomic-Wireless-Scrolling/dp/B078HFRNSP/ref=sr_1_22_sspa?dchild" \
      "=1&keywords=mouse&qid=1610741989&sr=8-22-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQ0ZFRlJER0M2MDY0JmVuY3J5c" \
      "HRlZElkPUEwMzk1NzA1N0tNQkgwNFZMMUtZJmVuY3J5cHRlZEFkSWQ9QTA5Nzc2NzYxQjA5VjlRVjY1Q1hGJndpZGdldE5hbWU9c3BfYnRmJmFj" \
      "dGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

response = requests.get(url=url, headers=headers)
site_data = response.text

soup = BeautifulSoup(site_data, "lxml")
price_tag = soup.find(name="span", id="priceblock_ourprice")
price = price_tag.string
strip_price = price.split()
actual_price = strip_price[1].replace(",", "")
name_tag = soup.find(name="span", id="productTitle")
product_name = name_tag.string


if float(actual_price) < 1500:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="lazyminds.0499@yahoo.com", msg=f"Subject:Amazon price Alert"
                                                                                  f"\n\n{product_name}"
                                                                                  f" available at price "
                                                                                  f"{actual_price} \n {url}"
                        )
    connection.close()
