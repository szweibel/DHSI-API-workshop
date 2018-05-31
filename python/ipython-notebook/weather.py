# Let's combine some of what we've learned

while True:
    # Use "raw_input" instead of "input" in Python 2
    weather = input("What's the weather today? ")
    if weather == "cloudy" or weather == "overcase":
        print("You don't need a hat")
    elif weather == "sunny" or weather == "warm":
        print("Wear shades")
    elif weather == "rainy" or weather == "wet":
        print("Bring an umbrella")
    elif weather == "snowy" or weather == "cold":
        print("Wear your wooly muffler")
    else:
        print("I don't know what you should do today...")
