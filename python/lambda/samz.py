from bs4 import BeautifulSoup
import requests
import smtplib


def check_price():
    # get HTML page
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {"user-agent": user_agent}
    req = requests.get(URL, headers=headers)

    # get price
    soup = BeautifulSoup(req.text, "html.parser")
    span = soup.find("span", {"class": "price-tag-fraction"}) # <span id="priceblock_ourprice">...</span>
    price = span.text   # XY,ZW €

    return (price[:5])


URL = "https://articulo.mercadolibre.com.mx/MLM-638492764-antigua-maquina-de-escribir-royal-completa-_JM"
MY_PRICE = 698

actual_price = check_price()
# actual_price = int(check_price())
print(actual_price)
# if actual_price <= MY_PRICE:
#     print('eyop')
# else:
#     print('no le pierden?')
    # send_email(actual_price)