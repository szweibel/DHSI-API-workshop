[<<< Previous](motivate.md) |  [Next >>>>](resources.md)

## Working with external files

A common task in Python is to pull in and work with data from an external source, such as a spreadsheet or database. In this section, we'll use Python to open and read a `.csv` (plain text spreadsheet) file.

### Reading the .csv

Let's write a short script that will open the `.csv` and read in the lines:

```
import csv

file = open('nypl_items.csv', 'r')
entries = csv.DictReader(file)
```

The `open` function with `r` reads a text file and pulls in its contents. (It can also be used to write to a text file.)

The `csv.DictReader()` function takes a text file in .csv format and parses it. It gives back a list of dictionaries that use the field name (such as "id" and "Title") as the key. The dictionaries look like this:

```
{'Contributor': 'Emmet, Thomas Addis, 1828-1919 | Cabot, George | Lowell, John', 'Place': 'Boston, Mass.', 'id': '794', 'Description': 'Introduces Mr. [Jonathan?] Dwight, of Springfield.', 'Subject': '', 'Digital': 'http://digitalcollections.nypl.org/items/8ea65050-c52d-012f-b37d-58d385a7bc34', 'Title': 'Letter to George Cabot, Beverly [Mass.]', 'Note': '', 'Publisher': '', 'Date': '1785-07-02', 'Genre': '', 'Language': '', 'Resource': 'text'}
```

Let's try printing out only titles:

```
import csv

file = open('nypl_items.csv', 'r')
entries = csv.DictReader(file)

for row in entries:
    print(row['Title'])
```

Like before, you may need to use `Control-c` to cancel the printout.

OK, let's try something a little more involved. What if I want all the entries that are chromolithographs? (I'm not even sure what chromolithographs are, but they sound awesome...) Let's say that this time we also want both the title of the entry and also its URL on the NYPL website, so we can check them out.

```
import csv

file = open('nypl_items.csv', 'r')
entries = csv.DictReader(file)


for row in entries:
    if row['Genre'] == 'Chromolithographs':
        print(row['Title'], row['Digital'])
```

### Challenges

1. Can you figure out a way to find out how many chromolithographs are in the NYPL .csv file? Two ways to do this would be to add the items to a list and then use `len()`, or to create a variable that gets bigger as the program loops. You might want to collaborate with your tablemates on this one.

2. Write a short program that asks the user for the ID number of an entry and returns the title. This is pretty hard, so feel free to take a peek at the [solution](ask_csv.py).

[<<< Previous](motivate.md) |  [Next >>>>](resources.md)
