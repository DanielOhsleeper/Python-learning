import csv
import datetime

def new_csv(csv_open):
    year_info = {}
    apple_info = "AAPL.csv"
    with open(apple_info, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = datetime.datetime.strptime(row["Date"], "%d-%m-%Y").year
            if year not in year_info:
                year_info[year] = {
                    "Info": {
                        "Avg Price": 0,
                        "Min Price": 0,
                        "Max Price": 0,
                        "Avg Volume": 0,
                    }
                }
                year_info[year]["Info"]["Avg Price"] += float(row["Low"]) + float(row["High"]) / 2
                year_info[year]["Info"]["Min Price"] += float(row["Low"])
                year_info[year]["Info"]["Max Price"] += float(row["High"])
                year_info[year]["Info"]["Max Price"] += float(row["High"])
                year_info[year]["Info"]["Avg Volume"] += int(row["Volume"])

    with open(csv_open, "w", newline="") as w:
        fieldnames = ["Year", "Avg Price", "Min Price", "Max Price", "Avg Volume"]
        writer = csv.DictWriter(w, fieldnames=fieldnames)
        writer.writeheader()
        for year, info in year_info.items():
            writer.writerow({
                                "Year": year,
                                "Avg Price": info["Info"]["Avg Price"],
                                "Min Price": info["Info"]["Min Price"],
                                "Max Price": info["Info"]["Max Price"],
                                "Avg Volume": info["Info"]["Avg Volume"]

            })


new_csv("new_f.csv")

