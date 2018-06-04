groceries = ['ham','eggs','cheese']
flowers = ['rose','violet','daisy']
primes = [2,3,5,7,11,13]

print(groceries[0]) # prints the first item (counting starts at 0)

print(primes[2:4]) # prints from the third to the fifth item

print(flowers[1:]) # prints from the second item to the end

print(primes[:3]) # prints from the beginning to the fourth item


# Add an item to a list
flowers.append('buttercup')
print(flowers)


# Remove an item to a list
groceries.remove('ham')
print(groceries)
