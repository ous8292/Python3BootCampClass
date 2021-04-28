



#Writing CSV Files Example
    #Using lists

from csv import writer
with open("animals.csv", "w") as file:
    csv_writer = writer(file) #calling writer.. passing file in, save that to variable csv_writer
    csv_writer.writerow(["Name", "Age"]) #call write.row.. pass in a list, adds a row to the file for us
    csv_writer.writerow(["Odin", 1])
    csv_writer.writerow(["Kita", 1])