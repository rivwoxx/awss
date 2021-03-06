from bs4 import BeautifulSoup
import requests
import smtplib
import json

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

def lambda_handler(event, context):
    URL = "https://articulo.mercadolibre.com.mx/MLM-681420534-pantalla-display-touch-xiaomi-redmi-note-5a-prime-nuevo-_JM"
    MY_PRICE = 698

    actual_price = int(check_price())
    return{
        'statusCode': 200,
        'body' : json.dumps('Hello from lambda!')
    }