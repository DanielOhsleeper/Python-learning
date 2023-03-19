from VT.backend import Scanner
from VT.backend.Get_report import Report

if __name__ == '__main__':
    g = Report("https://www.virustotal.com/api/v3/urls/")
    print(g.get_status_code())
