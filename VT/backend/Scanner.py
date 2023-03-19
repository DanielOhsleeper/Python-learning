import requests
from urllib.parse import quote

class Scanner():
    headers = {
        "accept": "application/json",
        "x-apikey": "af445e54953bcd7ed3748f79ebbf2177c66f0e967c9a5d719b46e222ca72d3ae",
        "content-type": "application/x-www-form-urlencoded"}
    url = "https://www.virustotal.com/api/v3/urls"
    def __init__(self, url):
        self.url = url

    def parse_quote(self):
        url = "https://aronovich.co.il/"
        encoded_url = quote(url, safe="")
        payload = f"url={encoded_url}"
        return payload

    def post(self):
        response = requests.post(Scanner.url, data=Scanner.parse_quote(Scanner), headers=Scanner.headers)
        return response.text



if __name__ == '__main__':
    r = Scanner("https://www.virustotal.com/api/v3/urls/")
    print(r.post())