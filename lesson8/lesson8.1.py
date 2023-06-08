from datetime import date
import requests
from bs4 import BeautifulSoup
import re
def today_date():
    today = date.today().strftime("%d.%m.%Y")
    return today

def get_page():
    url = f"https://cbr.ru/currency_base/daily/?" \
          f"UniDbQuery.Posted=True&" \
          f"UniDbQuery.To={today_date()}"
    r = requests.get(url)
    return r.text

def main():
    html = get_page()
    soup = BeautifulSoup(html, "html.parser")
    table = [i.text for i in soup.find("table", "data").find_all("td")]
    print("stop")
    currency_text = table
    currencies = re.findall('[а-яА-ЯёЁ]+', currency_text)
    rate = table[4::5]
    pass

if __name__ == "__main__":
    main()