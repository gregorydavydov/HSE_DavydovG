import requests

class SirotinskyAPI:
    base_url = "https://api.sirotinsky.com"
    log = {
        "username": "HSE_student",
        "password": "123123123"
    }

    def __init__(self):
        self.__get_token()

    def __get_token(self):
        url = f"{self.base_url}/token"
        r = requests.post(url, data=self.log)
        result = r.json()["access token"]
        self.token = result

    def get_name(self, name):
        url = f"{self.base_url}/{self.token}/hello{name}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_org(self, inn):
        url = f"{self.base_url}/{self.token}/efrsb/organisation/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_person(self, inn):
        url = f"{self.base_url}/{self.token}/efrsb/person/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_traider(self, inn):
        url = f"{self.base_url}/{self.token}/efrsb/trader/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_manager(self, inn):
        url = f"{self.base_url}/{self.token}/efrsb/manager/{inn}"
        r = requests.get(url)
        result = r.json()
        return result


def main():
    s_api = SirotinskyAPI()
    user = s_api.get_name("Иванов И.И.")
    org = s_api.get_org("7701272485")
    pass