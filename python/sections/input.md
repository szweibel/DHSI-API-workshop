[<<< Previous](conditionals.md) | [Next >>>](google.md)

## Input

Python allows you to take input directly from the user using the `input` function. Let's use it to improve our weather application by asking for the weather before displaying the output.

```python
weather = input("What is the weather like today? ")

if weather == "sunny":
    print("Bring your shades")
elif weather == "rainy":
    print("Bring your umbrella")
elif weather == "snowy":
    print("Bring your wooly muffler")
else:
    print("I don't know what you should bring! I'm just a little program...")
```

When you run this program, Python should ask you for some input with the prompt `What is the weather like today?` (The space before the second `"` makes the prompt look more tidy in the console.) It will then return some advice based on the input. Try running it now.

### Storing Responses: Dictionaries

Essentially, what we're doing in our weather app so far is asking for some input, then comparing that input with some stored data to return some output. However, the data is stored in the form of if and elif statements—not the most convenient way to keep track of it, and this approach results in a lot of duplicated elif statements. Let's try storing our weather response data another way—in a dictionary.

A dictionary is similar to a list, in that it stores a group of other data types. In a dictionary, however, each piece of data (called a "value") is paired with an appropriate "key"—a name or number that can be used to look up that value. When placed in dictionary form, our weather responses would look like this:

```python
weather_responses = {
    "sunny" : "Bring your shades",
    "snowy": "Bring your wooly muffler",
    "rainy": "Bring your umbrella",
    }
```

As you can see, a dictionary begins with an opening curly brace (`{`) and ends with a closing curly brace ('`}`). Inside the braces, separated by commas, are key/value pairs—first a key, such as `"sunny"`, then a value, such as `"Bring your shades"`.

Let's improve our program using this dictionary of responses:


```python
weather_responses = {
    "sunny" : "Bring your shades",
    "snowy": "Bring your wooly muffler",
    "rainy": "Bring your umbrella",
    }

weather = input("What is the weather like today? ")

if weather in weather_responses:
    print(weather_responses[weather])
else:
    print("I don't know what you should bring! I'm just a little program...")
```

In the code above, we first define our dictionary, with different states of weather as the keys—the part taht we can look up. When we look up the key, we will be presented with the corresponding value—in this case, the advice about what we should do about the weather.

Looking up a value in a dictionary using a key looks like this:

```python
value = dictionary_variable[key]
```

For our weather example, that might look like this:

```python
weather_advice = weather_responses[weather]
```

Looking up a value in a dictionary is similar to looking up an item in a list using an index number, except instead of the index number, we use the key.

### Challenge

1\. How much of the code above do you understand? Even if you do kind of understand it, do you "grok" it—that is, *really* understand it?

Open up your REPL (type `python` at the `$` prompt). Play around with `input()` a bit until you understand it's behavior really well. Write a two-line program in the REPL or in a script that takes some input and echoes it back to the user.

Alternatively, mess around with dictionaries. Create a small phone book using a dictionary and look up a name in it.

2\. (optional) Read a little about the weird word [grok](grok.md).

[<<< Previous](conditionals.md) | [Next >>>](google.md)
