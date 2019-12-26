import requests
from bs4 import BeautifulSoup
import time

URL = input("Enter URL: ")

website = input("Enter only Flipkart or Amazon: ")

#price = 0

#URL = 'https://www.flipkart.com/acer-nitro-5-core-i5-9th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-an515-54-52fn-gaming-laptop/p/itmc72dcee51a8d5?pid=COMFHNY8Z7C9DGU6&lid=LSTCOMFHNY8Z7C9DGU6JLJSNJ&marketplace=FLIPKART&srno=s_1_3&otracker=AS_Query_OrganicAutoSuggest_4_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_5_na_na_na&fm=SEARCH&iid=75866374-1267-4942-a6e4-7b948be457e2.COMFHNY8Z7C9DGU6.SEARCH&ppt=sp&ppn=sp&ssid=2telojzya80000001577156739739&qH=6a476f61ea33f248'
def track_price(URL, website):
    #URL = "https://www.amazon.in/dp/B07DJ8K2KT?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=EZCJCBFBZJ971RAWSWRA"

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    #extracted = soup.find(id="priceblock_dealprice").get_text()

    if website.lower() == "flipkart":
        print("wait")
    elif website.lower() == "amazon":
        price = int(soup.find(id="priceblock_dealprice").get_text()[2:8].replace(',', ''))
        print(price)
    else:
        print("Nikal Bosdk")

    while True:
        if price <= 52000:
            print("Bhai, Kharid le")
        else:
            print("mat le bhai, abhi mehenga hi hai")
        #print(time.clock())


#def compare(price):
#    if price <= 52000:
#        print("Bhai, Kharid le")
#    else:
#        print("mat le bhai, abhi mehenga hi hai")

track_price(URL, website)
#compare(price)