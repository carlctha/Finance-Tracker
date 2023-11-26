import csv
from parse_csv import parse_csv_data


MONTH = "november"

file = f"swedbank_{MONTH}.csv"
print(file)


with open(file, mode="r", encoding="utf8") as csv_f:
    reader = csv.reader(csv_f)
    for row in reader:
        print(row)


if __name__ == "__main__":
    parse_csv_data(file)
