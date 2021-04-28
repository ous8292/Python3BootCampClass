

#using reader
# from csv import reader
# with open("fighters.csv") as file:
#     # call reader, pass in the file, gives back a csv.reader object.. then we iterate over it
#     csv_reader = reader(file)
#     # for no headers.. moves us forward once
#     next(csv_reader)
#     #for row in csv_reader:
#         #each row is a list
#         #print(row) #once it iterates over the object it gives us these nice rows
#
#
#     for fighter in csv_reader: #this is an iterator, if you go over it again it exhausts it
#         #each row is a list
#         print(f"{fighter[0]} is from {fighter[1]}") # you have to access data based off of the index (name index 0, country index 1, ect
#
#
#
#prints out a list that we can work with

# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)




#DictReader


from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
    #each row is an orderedDict!!
        #print(row)
        print(row['Name']) #using key value, you can pull names




### Other Delimiters
    # reader accept a delimerter kwarg in case your data isnt seperated by commas
    #
