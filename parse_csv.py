import csv


def parse_csv_data(file):
    file = file
    parsed_data = []

    with open(file, mode="r", encoding="utf8") as csv_f:
        reader = csv.reader(csv_f)
        next(reader)

        for row in reader:
            data = [row[6], row[9], row[10]]
            parsed_data.append(data)

    with open(file, mode="w", newline="") as csv_f:
        writer = csv.writer(csv_f)

        writer.writerow(["Transaktionsdag", "Beskrivning", "Belopp"])

        writer.writerows(parsed_data)
