# Creating functions


def weather_advice(weather):
    if weather == "sunny":
        return "Bring your shades"
    elif weather == "rainy":
        return "Bring your umbrella"
    elif weather == "snowy":
        return "You need snowshoes today"
    else:
        return "I don't know what you should bring! I'm just a little program..."

print(weather_advice('snowy'))
print(weather_advice('hail'))

