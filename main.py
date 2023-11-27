import csv
import gspread
from parse_csv import parse_csv_data

MONTH = "november"

file = f"swedbank_{MONTH}.csv"
transactions = []

with open(file, mode="r", encoding="utf8") as csv_f:
    reader = csv.reader(csv_f)
    for row in reader:
        date = row[0]
        name = row[1]
        amount = float(row[2])
        transaction = ((date, name, amount))
        transactions.append(transaction)


if __name__ == "__main__":
    #parse_csv_data(file)
    gc = gspread.service_account()
    sh = gc.open("Finance")
