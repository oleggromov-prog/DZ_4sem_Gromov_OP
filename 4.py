import csv
with open("products.csv", "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)

    heading = reader.fieldnames

    with open("expensive.csv", "w", encoding = "utf-8") as file_res:
        writer = csv.writer(file_res)

        writer.writerow(heading)

        for st in reader:
            name = st["name"]
            category = st["category"]
            price = st["price"]

            if int(price) > 100:
                writer.writerow([name, category, price])