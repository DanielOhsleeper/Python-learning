import requests
from urllib.parse import quote
import base64

class VirusTotal():
    headers = {
        "accept": "application/json",
        "x-apikey": "af445e54953bcd7ed3748f79ebbf2177c66f0e967c9a5d719b46e222ca72d3ae",
        "content-type": "application/x-www-form-urlencoded"}
    url = "https://www.virustotal.com/api/v3/urls"
    endpoint = base64.urlsafe_b64encode("http://www.aronovich.co.il/".encode()).decode().strip("=")

    def __init__(self, user_url):
        self.user_url = user_url

    def scan(self):
        encoded_url = quote(self.user_url, safe="")
        payload = f"url={encoded_url}"
        response = requests.post(VirusTotal.url, data=payload, headers=VirusTotal.headers)
        return response.content

    def get_url_analysis(self):
        url_id = base64.urlsafe_b64encode(self.user_url.encode()).decode().strip("=")
        url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
        response = requests.get(url, headers=VirusTotal.headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 404:
            raise ConnectionError("URL Does not exist, please rescan")
        else:
            raise Exception(f"API Call Error, status code {response.status_code}")
