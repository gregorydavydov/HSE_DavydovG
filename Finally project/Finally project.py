#Итоговый проект

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

    def __sorted_table(self):
        data_dict = {}
        self.data_dict = data_dict
        for i in range(3, len(self.table), 5):
            currency_name = self.table[i]
            current_rate = self.table[i+1]
            data_dict[currency_name] = {
                "current_rate": current_rate
            }

        sorted_data_dict = dict(sorted(data_dict.items()))
        return sorted_data_dict

    def __table_data(self, table_json):
        with open(table_json, "w", encoding="utf-8") as table2write:
            json.dump(self.data_dict, table2write, ensure_ascii=False)

    def start(self):
        self.__get_info()
        self.__sorted_table()
        self.__table_data("result1.json")



if __name__ == "__main__":
    pars = ParserCBRF()
    pars.start()