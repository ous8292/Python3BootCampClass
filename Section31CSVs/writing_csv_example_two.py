from csv import reader, writer


# will read from one file.. take data uppercase all of it and then write to a new file


with open('fighters.csv') as file:
    csv_reader = reader(file)
    fighers = [csv_reader]
    for row in csv_reader:
        print(row)


with open('uppercase_fighters.csv', 'w') as file:
    csv_writer = writer(file)
