#ДЗ 13

from datetime import date
import requests
from bs4 import BeautifulSoup
import json

class ParserCBRF:
    def __init__(self):
        self.url = ""
    def __today_date(self):
        today = date.today().strftime("%d.%m.%Y")
        return today
    def __get_page(self):
        url = f"https://cbr.ru/currency_base/daily/?" \
              f"UniDbQuery.Posted=True&" \
              f"UniDbQuery.To={self.__today_date()}"
        r = requests.get(url)
        return r.text
    def __get_info(self):
        html = self.__get_page()
        soup = BeautifulSoup(html, "html.parser")
        table = [i.text for i in soup.find("table", class_="data").find_all("td")]
        self.table = table

    def __table_data(self, table_json ):
        with open(table_json, "w") as table2write:
            json.dump(self.table, table2write)
    def start(self):
        self.__get_info()
        self.__table_data("result.json")

if __name__ == "__main__":
    pars = ParserCBRF()
    pars.start()

