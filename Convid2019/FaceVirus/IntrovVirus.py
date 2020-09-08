import requests
from urllib3.exceptions import *


def dailyqyery():



    ses=requests.session()

    re=ses.get(url="https://www.pharmaceutical-technology.com/special-focus/covid-19/coronavirus-covid-19-outbreak-latest-information-news-and-updates/",verify=False)
    print(re.text)


dailyqyery()
