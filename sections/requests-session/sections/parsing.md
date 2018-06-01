[<<< Previous](requests.md) | [Next >>>](transform.md)

# Parsing and Exploring Results

## Parsing Our JSON

We have our JSON text in python in the form of `all_newspapers.text`. Let's use another library, the JSON library that comes with Python, to turn the JSON we've requested into a Python dictionary.

First, import the JSON library:

	>>> import json
	
Our next step will be to "load" the data into a dictionary:

	>>> news_dict = json.loads(all_newspapers.text)
	
In the variable name, `dict` is short for "dictionary." 
Let's confirm that our dictionary is what we expect. Try

	>>> type(news_dict)
	
and

	>>> news_dict
	
The former should return `<class 'dict'>`. The latter should print out a representation of the dictionary, which looks a lot like JSON data. That's because JSON and Python dictionaries look pretty much the same as one another.

The process we just performed is called "parsing." This means taking a string or other text representation and transforming it into something more usable by the machine. We've taken JSON, a text representation, and turned it into a Python dictionary, which is easily manipulable by the computer. JSON is intended to be easily parable, so this process wasn't difficult.

## Exploring the Dictionary

Let's use some dictionary-specific approaches to explore the data stored in the dictionary and get it into a more usable form.

We've already tried this:

	>>> news_dict
	
Unfortunately, this results in too much information to get a handle on what's going on with the dictionary.

Remember our earlier lesson on dictionaries in Python? We learned that dictionaries have keys and values. The key is a reference, allowing you to look up values, the same way we look up phone numbers in a phone book by using someone's name. (At least we did before the internet came along.)

Let's use a dictionary-specific method, `.keys()`, to find the keys in our dictionary. (Remember that a "method" is a function that lives inside an object.)

	>>> news_dict.keys()
	
The result should be:

	dict_keys(['newspapers'])

Interesting! Our dictionary only has one key, `newspapers`. That means that all the data we want—the newspaper titles and other information—is contained as the value of this single key.

We might as well pull that data out and assign it to a new variable. First, let's take a quick look at the value associated with the `newspapers` key looks like:

	>>> news_dict['newspapers']
	
OK, it's the data we suspected it was. Let's also check out what type it is:

	>>> type(news_dict['newspapers'])

That's something different—instead of a dictionary, it's `<class 'list'>`. Let's assign it to the variable `news_list`:

	>>> news_list = news_dict['newspapers']

If it's a list, one interesting thing to know would be how long it is. We can do that with the `len()` function:

	>>> len(news_list)
	
That's a lot of newspapers!

## Reflection: An Exploratory Workflow

Stepping back for a second, you may be seeing a workflow developing as we explore using the REPL.

1. Start by pulling in some data, such as through the requests library or (though we haven't discussed this) opening a file.
2. See what the representation of the imported data is by typing in its variable name.
3. Use `type()` to get a general idea of what form the data is currently in.
$. Use a toolbox of functions, methods, and attributes to figure out what can be done with the data from here. These include `len()` to get an idea of how long lists and strings are, `keys()` to see what keys are available in dictionaries, and `dir()` if it's an unfamiliar type and you aren't sure how to proceed. The process of examining what an object in Python can do is called "introspection."
4. Take some action, such as pulling out a specific part of the data, and assign the result to a new variable.
5. Start again from the top with the new variable. Keep going until you have a more concrete idea of what you're working with.

So far, we've found out our newspaper title data consisted of a dictionary with one key/value pair, and we pulled out the value. In the next section, we'll start manipulating that data.

[<<< Previous](requests.md) | [Next >>>](transform.md)
