import csv

file = open('nypl_items.csv', 'r')
entries = csv.DictReader(file)

dictionary = {}

for row in entries:
    dictionary[row['id']] = row['Title']

while 1:
    id = input("Please enter an ID number: ")
    print(dictionary[id])
