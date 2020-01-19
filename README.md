# Amazon_Price_Tracker
This program uses a Amazon URL and scrapes the website for the title and price. You have to input a expected price, your email id(only works fir Gmail)and the product URL. It will send you an email if the price drops below yout expected value.(Interval 1hr)

Modules Required:
1. smptlib
2. Beautifull Soup
3. Selenium
4. webdriver-manager
5. time
6. sys

NOTE :- 

i. It works with normal products and products which are listed as the deal of the day

ii. If it throws an error saying "'qid' s not recognized", then there is problem with the path

iii. You must edit the script and provide the Email and Password from which you will be notified

LIMITATIONS :-

Although, the program is made to run for eternity, however in real it will throw and error at some point of the time. This is because the Amazon Server by then will have reognized your IP and deny and kind of scraping
