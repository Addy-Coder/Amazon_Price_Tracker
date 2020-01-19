import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
#Make sure that you have enabled sercurity access to your below google account
EMAIL_ADDRESS = 'Provide Email'
EMAIL_PASSWORD = 'Provide Password'

price_compare = sys.argv[1]
sending_email = sys.argv[2]
url = sys.argv[3]

while 1:
    def getPrice(url):
        try:
            # headers = {"User Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
            # html = requests.get(url, headers=headers)

            soup = BeautifulSoup(url,'lxml')
            title = soup.find("span", {"id": "productTitle"}).get_text().replace('\n', '').strip()
            price = float(soup.find("span",{"id":"priceblock_dealprice"}).get_text()[2:].replace(',','').strip())
            # price_int =
            print("---------------------------------")
            print(title)
            print(price)
            print("---------------------------------")
            return price
        except AttributeError:
            title = soup.find("span", {"id": "productTitle"}).get_text().replace('\n', '').strip()
            print("---------------------------------")
            print(title)

            price = float(soup.find("span",{"id":"priceblock_ourprice"}).get_text()[2:].replace(',','').strip())
            print(price)
            print("---------------------------------")
            return price
    def sendMail(url):
        print("Sending mail......")
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = "CHECK OUT THE NEW PRICE"
            body = "Price Droped : "+url

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(EMAIL_ADDRESS, sending_email, msg)
            print("Your Email has been sent successfully to " )


    #url = 'https://www.amazon.in/Gaming-G3-3579-i5-8300H-Windows-Graphics/dp/B07XZFYQ18/ref=sr_1_1_sspa?crid=1UHDM8R5ZWB9W&keywords=lenovo+laptops&qid=1579367794&smid=A14CZOWI0VEHLG&sprefix=lenovpo%2Caps%2C381&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyODFKV1kxU05NU0g3JmVuY3J5cHRlZElkPUEwNjIzMTk4Mk9PSjVDNkQ3WkRHQSZlbmNyeXB0ZWRBZElkPUEwMjA4NjY2MzFKN0xZWFc3OVZaMCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    #url = 'https://www.amazon.in/Skybags-Crew-06-Laptop-Backpack/dp/B07P9JJB2X/ref=sr_1_4_sspa?keywords=skybags&qid=1579411412&sr=8-4-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFYVTY3WkIyUzBHM00mZW5jcnlwdGVkSWQ9QTA3MzU1MDFISk1COEdaWFo2RTAmZW5jcnlwdGVkQWRJZD1BMDI3NTg2ME9aNVZSSDUwUlZUTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    #url = 'https://www.amazon.in/dp/B07TM676N1/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=Z7E0858VT26CM6JM87N3&pf_rd_t=101&pf_rd_p=7d57b3de-af2a-486a-86e4-68512d72663d&pf_rd_i=20669076031'
    #url = 'https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/ref=lp_10559548031_1_1?s=computers&ie=UTF8&qid=1579412452&sr=1-1'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    getPrice(res)

    # price_compare = 1800
    price_current = getPrice(res)
    if price_current<int(price_compare):
        print("*** Price Droped ***")
        sendMail(url)
    time.sleep(60*60)
