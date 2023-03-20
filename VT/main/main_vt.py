import pprint
from VT.backend.VT import VirusTotal
if __name__ == '__main__':
    vt = VirusTotal("https://aronovich.co.il/")
    try:
        res = vt.get_url_analysis("https://aronovich.co.il/")
        pprint.pprint(res)

    except ConnectionError:
        vt.scan()
    except Exception as e:
        print(e)

