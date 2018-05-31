# Dictionaries

# Let's make a phone book

phone_book = {'Alice':199933355555,
              'Bob':14446669999,
              'Betty Suarez':18884321111,
              'Wilhelmina Slater':12223334444}


print(phone_book['Alice'])

def look_up_number(name):
    return phone_book[name]

print("Betty's number is",look_up_number('Betty Suarez'))

