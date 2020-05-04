from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import time

browser = Browser("chrome", executable_path="chromedriver", headless=False)

base_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)
time.sleep(5)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

class_name ="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"
mars_weather = weather_soup.find('div' , class_=classname).text
print("Now printing weather")
print(mars_weather)
