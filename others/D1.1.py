import csv
import os

count = 0
names = []
file_path = 'C:/Users/ohsle/Downloads/'

def search(count):
    for roots, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith("csv"):
                count += 1
                file_split = file.split(".")
                names.append(file_split[0])
                print(file_split[0])
        print(f"Amount of csv files {count} in {file_path}")
        print(names)


def count_data(file_path):
    rowcount = 0
    for name in names:
        with open(f"{file_path}{name}.csv", "r") as f:
            reader = csv.reader(f)
            for row in f:
                rowcount += 1
        print(f"FileName: {name}, Rows: {rowcount}")
        print(f"FileName: {name}, Columns: {len(row.split(','))}")


search(count)
count_data(file_path)