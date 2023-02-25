# import csv
# import json
# absolute_path = r"C:\Users\ohsle\PycharmProjects\evening-ninjas\lesson12\files\data\AAPL.csv"
#
# with open(absolute_path) as f:
#     reader = csv.DictReader(f)
#     objects = list(reader)
# with open("path.json", "w") as f1:
#     json.dump(objects, f1)
#


student = {"name": "John",
           "age": 30}

print(student.get("name"))