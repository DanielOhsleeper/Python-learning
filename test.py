import csv
path = r"C:\Users\ohsle\Downloads\tatauranga-umanga-maori-statistics-on-maori-businesses-2021-csv-english.csv"

with open(path, 'r') as f:
    csv_reader = csv.DictReader(f)

    with open("csv_file.csv", 'w') as n_file:
        fieldnames = []
        for line in csv_reader:
            # csv_writer.writerow(line)
            # print(line)
            fields = []
            for k, v in line.items():
                if k not in fieldnames:
                    fieldnames.append(k)
            csv_writer = csv.DictWriter(n_file, fieldnames=fieldnames, delimiter='\t')
            csv_writer.writeheader()
            for line in csv_reader:
                csv_writer.writerow(line)



