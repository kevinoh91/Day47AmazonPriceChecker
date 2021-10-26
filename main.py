from bs4 import BeautifulSoup
import requests
import smtplib

user = "kyoh.python@gmail.com"
password = ""

product_page = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(product_page, headers=headers)
website = response.text

soup = BeautifulSoup(website, "html.parser")
price = float(soup.find(name="span", class_="a-size-base a-color-price").text.split("$")[1])
product = soup.find(id="productTitle").get_text().strip()
price_target = input("Input price target: $")

if price <= price_target:
    message = f"{product} is currently selling for ${price}. Buy now: {product_page}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user, to_addrs=user, msg=f"Subject: Price Alert!\n\n{message}")
