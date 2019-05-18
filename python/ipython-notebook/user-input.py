# If you're using Python 3:

name = input("What's your name? ")

# If you're using Python 2:
#
# name = raw_input("What's your name? ")

if len(name) > 12:
    print("Hi %s! Your name is quite long!" % name)
else:
    print("Hi %s! Your name is quite short!" % name)
