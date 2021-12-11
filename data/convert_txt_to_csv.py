#Converts txt file to csv


#Import file
file = open("./may_treat_data.txt","r")
lines = file.readlines()


#Bench test : print first 5 contents of file
# for i in range(0,5):
#     print(lines[i])


#Remove the endlines from all the lines in the file
for i in range(0,len(lines)):
    size_of_line = len(lines[i])
    lines[i] = lines[i][:size_of_line-1]


# #Bench test : print first 5 contents of file
# for i in range(0,5):
#     print(lines[i])

#Convert all of STR1 to lowercase
for i in range(0,len(lines)):
    lines[i] = lines[i].lower()



#Prepare data to write into csv
import csv
fields = ["CUI1", "TS1", "STR1", "CUI2", "TS2", "STR2"]
rows = []

#Stores seen STR1
#Key = STR1
#Val = True/False
ht = {}

#Populate the rows variable; use ht to prevent the storing of duplicates
for line in lines:
    cur_line = line.split("|")
    if cur_line[2] not in ht:
        rows.append(cur_line)
        ht[cur_line[2]] = True

# #Bench Test : print to make sure the rows were split correctly
# for i in range(0,5):
#     print(rows[i])


filename = "unique_may_treat.csv"

#Write to file
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)