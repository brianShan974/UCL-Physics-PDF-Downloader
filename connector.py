import requests
from bs4 import BeautifulSoup


class Connector:
    def __init__(self):
        self.counter = 0
        self.session = requests.Session()
        self.login_url = "https://moodle.ucl.ac.uk/login/index.php"
        self.post_login_url = "https://moodle.ucl.ac.uk/my/"

    def login(self, username: str, password: str):
        page = self.session.get(self.login_url)
        page_soup = BeautifulSoup(page.text, "lxml")
        login_token = page_soup.find_all("input")[3]["value"]
        values = {
            "username": username,
            "password": password,
            "logintoken": login_token
        }
        self.session.post(
            login_url,
            data=values
        )
        self.post_login_soup = BeautifulSoup(
            self.session.get(self.post_login_url).text,
            "lxml"
        )