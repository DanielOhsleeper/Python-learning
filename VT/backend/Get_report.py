import requests
import base64

class Report():
    headers = {
        "accept": "application/json",
        "x-apikey": "af445e54953bcd7ed3748f79ebbf2177c66f0e967c9a5d719b46e222ca72d3ae"
    }
    def __init__(self, url):
        self.url = url

    endpoint = base64.urlsafe_b64encode("http://www.aronovich.co.il/".encode()).decode().strip("=")

    def get(self, endpoint):
        url = f"https://www.virustotal.com/api/v3/urls/{endpoint}"
        response = requests.get(url, headers=Report.headers)
        return response

    def get_status_code(self):
        response = Report.get(Report, Report.endpoint)
        return response.status_code



if __name__ == '__main__':
    g = Report("https://www.virustotal.com/api/v3/urls/")
    print(g.get(Report.endpoint))



