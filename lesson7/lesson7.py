#ДЗ 13

import requests
from bs4 import BeautifulSoup

"""
url_p = /?UniDbQuery.Posted=True&UniDbQuery.From=17.09.2013&UniDbQuery.To=19.05.2023 - 
CBR_URL = "https://cbr.ru/hd_base/KeyRate/"

def get_page(url):
    url = f"https://www.cbr.ru/hd_base/KeyRate/?" \
          f"UniDbQuery.Posted=True&" \
          f"UniDbQuery.From=17.09.2013&" \
          f"UniDbQuery.To={today_human_date()}"
    r = requests.get(url)
    return r.text


def main():
    html = get_page(url)
    soup = BeautifulSoup(html, "html.parser")
    table_data = [i.text for i in soup.find("table", "data").find_all("td")]
    pass

if __name__ == "__main__":
    main()

"""
CBR_URL = "https://cbr.ru/hd_base/KeyRate/"

def get_page(url):
    r = requests.get(url)
    return r.text

def main():
    html = get_page(CBR_URL)
    soup = BeautifulSoup(html, "html.parser")
    table_data = [i.text for i in soup.find("table", "data").find_all("td")]


    pass

if __name__ == "__main__":
    main()
    pass



