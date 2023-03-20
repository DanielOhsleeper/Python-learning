import pprint
from VT.backend.VT import VirusTotal
import argparse
if __name__ == '__main__':
    vt = VirusTotal("https://da.co.il/")
    s = vt.scan()
    try:
        res = vt.get_url_analysis()
        pprint.pprint(res)
        pprint.pprint(s)
    except ValueError:
        vt.scan()
    except Exception as e:
        print(e)


