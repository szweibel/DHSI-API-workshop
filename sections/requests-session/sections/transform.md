[<<< Previous](parsing.md) | [Next >>>](challenges.md)

# Cleaning and Transforming  Data

After our work in the last section, we currently have a list, and we know that our list has data relating to newspaper titles. However, we don't know what the items in the list actually look like.

Let's use Python's list indexing capability to take a look at the first item in the list.

	>>> news_list[0]

The output should look something like this:

```python
{'url': 'http://chroniclingamerica.loc.gov/lccn/sn85025905.json', 'lccn': 'sn85025905', 'title': 'Chattanooga daily rebel.', 'state': 'Alabama'}
```

The "Chattanooga Daily Rebel"—sounds dangerous!

On first blush this looks like a dictionary...the curly braces are a dead givaway. But let's do our usual process: confirm the type with `type()`.

	>>> type(news_list[0])
	
Yep, it's a dictionary. Now what if we want to extract some part of each of these dictionaries, like the title? Remember that there are thousands of these dictionaries, one for each newspaper.

## Cleaning and Transforming Data

"Cleaning" data can mean many things—removing duplicates, detecting bad entries, and performing sanity checks to make sure the data is what you think it is can all be considered part of data cleaning. Often, too, you'll want to transform data in different ways—perhaps by discarding irrelevant data, putting the data in a different form for input into another tool, or combining the data with another data set.

In the earlier Python session, you learned about for loops—a form of "iteration," a fancy word for doing something over and over. When cleaning and transforming data, you'll frequently want to do the same thing to each entry. We're going to learn about a new way of doing iteration that is similar to the for loop but better adapted to work in the REPL—the list comprehension.

Before we jump into the list comprehension, let's first figure out how we would pull out the title from only one of these dictionaries, without any iteration. Let's first assign a variable to the first dictionary in the list of newspaper entires:

	>>> first_item = news_list[0]
	
then pull out the title:

	>>> title = first['title']
	
Then let's just check to make sure we got what we wanted:

	>>> title
	
We got back the unforgettable `'Chattanooga daily rebel.'`, so we've successfully grabbed the title and just the title.

## Using Iteration to Transform Data

If we were going to use a for loop to pull out all the titles, we might try something like this:

```python
# Create an empty list to put titles in
titles = []

for newspaper in news_list:
	# Extract the title from the dictionary
	title = newspaper['title']

	# Add the title to the output list
	titles.append(title)
```

This is a perfectly valid approach, but one better suited to writing a script than exploring data in a freeform way using the REPL. Let's use the list comprehension to perform essentially the same action. We'll first run the code, then explain it afterward.

	>>> [newspaper['title'] for newspaper in news_list]
	
You should see a list printed out that has only titles, which is what we wanted. That saved a lot of arduous typing, right?

In a sense, the list comprehension is a compressed version of the above for loop. The second item in the comrehension, ` for newspaper` defines a new variable for each run through the loop. The first item, `newspaper['title']` is the action that is performed during each loop—in this case, pulling the title out of the dictionary using the `'title'` key. The last part, `in news_list`, tell the comprehension what to loop over, in this case the list of newspaper entries.

Finally, note that list comprehensions automatically create a list containing the accumulated results.

If you're still confused about the list comprehension, don't worry! It tends to take awhile to understand what it's doing, and the normal for loop syntax is usually easier to comprehend. Feel free to stick with it—for loops can do anything list comprehensions can do, they're just a bit more verbose.

## One More Time Around the List Comprehension

Let's try one more trick with the list comprehension. As you can tell, I'm very taken with the name of the *Chattanooga Daily Rebel*. (Though, apparently it was a [Confederate newspaper during the American Civil War](http://www.timesfreepress.com/news/opinion/columns/story/2013/jul/21/hodges-newspaper-wheels-chattanooga-daily-rebel/113722/)...that part isn't so hot.) I'm curious to know how common the name "rebel is in the Chronicling American list of newspaper titles. Let's find that out with list comprehensions.

We'll use the same list comprehension as above, but we'll add one short clause—an `if` statement—to the end. Here's our new, highly rebellious list comprehension:

	>>> [newspaper['title'] for newspaper in news_list if 'rebel' in newspaper['title']]
	
Here are the results. (They aren't formatted as nicely when they are returned to you, but this is a valid Python list.)

```python
[
    'Chattanooga daily rebel.',
    'The Chattanooga Daily Rebel.',
    'The daily Chattanooga rebel.',
    'The Chattanooga Daily Rebel.',
    'The daily Chattanooga rebel.',
    "Brownlow's Knoxville Whig, and rebel ventilator.",
    "Brownlow 's Knoxville Whig, and rebel ventilator.",
    'The Chattanooga Daily Rebel.',
    'Knoxville tri-weekly Whig and rebel ventilator.'
]
```

There aren't that many newspapers in the data with the word "rebel" in them, but knowing about the *Knoxville tri-weekly Whig and rebel ventilator* makes it all worth it!

[<<< Previous](parsing.md) | [Next >>>](challenges.md)
