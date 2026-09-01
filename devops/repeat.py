import csv
from collections import Counter


def find_duplicates(csv_file, column_name):
    values = []

    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if column_name not in reader.fieldnames:
            print(f"Column '{column_name}' does not exist.")
            return

        for row in reader:
            value = row[column_name].strip()

            if value:
                values.append(value)

    counts = Counter(values)

    print(f"\nRepeated values in column '{column_name}':\n")

    duplicates_found = False

    for value, count in counts.items():
        if count > 1:
            print(f"{value} -> repeated {count} times")
            duplicates_found = True

    if not duplicates_found:
        print("No duplicate values found.")


if __name__ == "__main__":
    find_duplicates(
        csv_file="users.csv",
        column_name="email"
    )