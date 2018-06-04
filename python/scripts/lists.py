# Define some lists

empty_list = []
groceries = ['ham','eggs','cheese']
flowers = ['rose','violet','daisy']
primes = [2,3,5,7,11,13]

print(empty_list)
print(flowers)

# Use a for loop to go through (or "iterate over") lists and do something to each item

for flower in flowers:
    print(flower)

for item in groceries:
    print(item)

for number in primes:
    double_prime = number * 2
    print(double_prime)
