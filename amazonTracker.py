import requests
from bs4 import BeautifulSoup
import time
import smtplib

URL = "https://www.amazon.com/dp/B086T2TLB7/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B086T2TLB7&pd_rd_w=Oujl3&pf_rd_p=48d372c1-f7e1-4b8b-9d02-4bd86f5158c5&pd_rd_wg=nNtav&pf_rd_r=2MR21YM9MT8CZDFG8T36&pd_rd_r=747c079f-3c29-4809-af73-7f44f1870b07&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTENPMTJVSlFOSE5XJmVuY3J5cHRlZElkPUEwNjg0MzQ5MkxQTUFKMDJDVzZWNCZlbmNyeXB0ZWRBZElkPUEwMzc4NzIwM002N0s1U05DRUlZQSZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15"}
WANTED_PRICE = 24
EMAIL_ADDRESS = "ethan.halfhide@gmail.com"

def trackPrice():
    price = int(getPrice())
    if price > WANTED_PRICE:
        diff = price - WANTED_PRICE
        print(f"It's still {diff} too expensive")
    else:
        print("Cheaper!!")
        sendMail()


def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    with open('test.html', 'w') as f:
        f.write(str(soup))
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    print(title)
    print(price)
    return price

def sendMail():
    subject = "Amazon Price Has Dropped!"
    mailtext = "Subject:"+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttsl()
    server.login(EMAIL_ADDRESS, 'MyFakePassword')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    print("Sent Email")
    pass

if __name__ == "__main__":
    while True:
        trackPrice()
        time.sleep(60)

