[<<< Previous](fires.md) | [Next >>>](parsing.md)

# Making Requests Using Python

Thus far in these sessions we've done a lot of preparation and learned a lot of concepts. Let's now get our hands dirty and use Python to explore some results from the Chronicling America API. Instead of using the browser to peek at results in JSON, we'll pull these results into our Python environment and step through the results.

In DH Box, click the Command Line tab and log in. Once you're at the prompt (your username and the `$`), type

	python3
	
to open the REPL. The prompt should change to look like this, showing that you are interacting directly with Python:

	>>>
	
## REPL Refresher	

Remember the REPL? We used it at the beginning of the Python session. REPL stands for Read Eval Primt Loop, and the way it works is that you type one line and send it to Python, and Python prints out the result right back at you. Unlike when we write Python scripts, we don't have to use print statements—the result is automatically printed. This makes the REPL great for experimentation, exploration, and testing.

For example, if we type:

	>>> 1
	
we will get the result:

	1
	
We entered `1` and didn't ask for anything to happen, so we get `1` back.

If we do:

	>>> x = 1

and then type just:

	>>> x
	
we will also get `1` back as a result.

Remember that the REPL does four things:

1. Reads in a line of Python that you give it.
2. Evaluates it, meaning simplifying operations, running functions, and so on.
3. Prints the result back to the screen.
4. Loops, meaning it waits again for you to enter a new line.

## Installing requests

Now that we've reviewed how the REPL works, let's use it to request some data from Chonicling America for us to work with. For this, we'll be using the requests library in Python. This library allows you to communicate with the web from inside your Python program.

First, let's make sure requests is installed. Exit the REPL by holding `Control` and hitting `d`. You can also type `exit()` and hit `Enter`.

Once you're back at the "normal" command line (also known as "bash"), enter this command:

	sudo pip3 install requests
	
You will have to enter your login password again for this to work. Once it's finished, re-enter the REPL by typing

	python3
	
and test whether requests was successfully installed by typing

	import requests
	
If you see no output after running this command, requests was successfully imported, meaning it was successfully installed.

## Making our request

Now we're ready to use requests to pull in some data from Chronicling America. We're going to pull in a list of newspaper titles, and our request will look like this:

	http://chroniclingamerica.loc.gov/newspapers.json 
	
This request is described in the [Chronicling America documentation](https://chroniclingamerica.loc.gov/about/api/#linked-data) as "a list of all newspaper titles for which there is digital content." The only way to know what that means in practice is to take a look, so copy that URL out and see what it looks like in your browser. (Or you can just click [here](http://chroniclingamerica.loc.gov/newspapers.json ).

The output should look something like this excerpt:

```json
{
  "newspapers": [
    {
      "lccn": "sn85025905", 
      "url": "http://chroniclingamerica.loc.gov/lccn/sn85025905.json", 
      "state": "Alabama", 
      "title": "Chattanooga daily rebel."
    }, 
    {
      "lccn": "sn82015209", 
      "url": "http://chroniclingamerica.loc.gov/lccn/sn82015209.json", 
      "state": "Alabama", 
      "title": "The Chattanooga Daily Rebel."
    }, 
    {
      "lccn": "sn82014371", 
      "url": "http://chroniclingamerica.loc.gov/lccn/sn82014371.json", 
      "state": "Alabama", 
      "title": "The daily Chattanooga rebel."
    },
```

This output is a little more comprehensible than our search output when we were looking for information on historical fires—there's no complicated pagination. This makes it useful for us to explore on our first run with requests.

Head back to the command line tab in DH Box and enter this line to grab the JSON output and save it to the `all_newspapers` variable.

	>>> all_newspapers = requests.get('https://chroniclingamerica.loc.gov/newspapers.json')

Let's check if that command succeeded. Type

	>>> all_newspapers
	
If you see the following, you've successfully pulled in the data:

	<Response [200]>

Remember that HTTP code `200` means `OK`, or that the request was successfully fulfilled. The most common negative response is `404`, for `Not Found`.

Nice! We've pulled in our data. But what can we do with it?

## Playing with Objects

Let's use our old friend, the `type()` function, to take a look at our `all_newspapers` variable that we created using the requests library.

	>>> type(all_newspapers)
	
You should see something like this:

	<class 'requests.models.Response'>

This means that our `all_newspapers` is a `Response` object as defined in the requests library. But what is a Python object, really? And what do we do with it?

Objects in Python (and other programming languages) are basically containers that can hold data and/or functions inside them. When a function is inside an object, we usually call the function a "method." When data is inside an object, we usually call it an "attribute." The terminology isn't that important, though. What we do need to know is that you can access these "methods" and "attributes" with a `.` (a dot or period).

Try this:

	>>> all_newspapers.status_code
	
You should get this result:

	200
	
Cool, but we already knew that our request was successful. Let's try another:

	>>> all_newspapers.text
	
You should see output with data from the request in (messy) JSON format. That's more like it!

When you encounter an object, how can you learn its methods and atributes so you can use them? There are two main ways. The first, and likely the most practical, is to [read the documentation of the library you're using](http://docs.python-requests.org/en/master/). 

It often happens, though, that the docs for a library you're using are confusing, nonexistent, or inaccurate. In these cases, you can try using the `dir()` function, which will tell you which methods and attributes are available in an object.

	>>> dir(all_newspapers)
	
When using `dir()`, you'll mostly want to ignore the methods and attributes that have underscores around them. They mainly have to do with the internals of the Python language.

## Challenge

Either using the [requests documentation](http://docs.python-requests.org/en/master/) or the `dir()` function, try out some other methods and attributes of the `all_newspapers` variable. Remember that `all_newspapers` is a `Response` object from the requests library.

[<<< Previous](fires.md) | [Next >>>](parsing.md)
