[<<< Previous](errors.md) | [Next >>>](conditionals.md)

# Lists and Loops

## Lists

Remember lists? They look like this:

```python
flowers = ['rose', 'violet', 'buttercup']
```
	
For now, let's just create a list and print it out. Our script will look like this:

```python
flowers = ['rose', 'violet', 'buttercup']
print(flowers)
```

Save this to a new file called `loop.py` and run it with `python loop.py`. You should see the list printed out in the terminal.

So far, we've only learned one function: `type()`. Let's try out another:

```python
flowers = ['rose', 'violet', 'buttercup']
# print(flowers)

list_length = len(flowers)

print(list_length)
```

The `len()` function returns the number of items in a list or the number of characters in a string.

Notice that, if you run the code above, you won't see the `flowers` list printed out. That's because that line has become a comment. If you put a `#` (hash or pound) at the beginning of a line, that line will be ignored.

# List Indexing 

A useful property of a list is the list index. This allows you to pick out an item from within the list by a number starting from zero:

```python
print(flowers[0]) # rose
print(flowers[1]) # violet
```
Note that the first item in the list is item [0]. The second item is item [1]. That's because counting in Python, and in almost all programming languages, starts from 0.

You can print out the last item in a list using negative numbers:

```python
print(flowers[-1]) # buttercup
```

## Loops

What if we want to print out each item in the list separately? For that, we'll need something called a loop:

```python
flowers = ['rose', 'violet', 'buttercup']
# print(flowers)

for flower in flowers:
    print("My favorite flower is the" + flower)
```

What's happening here? This kind of loop is called a "for" loop, and tells Python: "for each item in the list, do something." Let's break it down:

```
for <variable name> in <list name>:
	<do something>
```

Indented code like this is known as a "code block." Python will run the <do something> code in the code block once for each item in the list. You can also refer to \<variable name> in the <do something> block.

You can also perform more complicated operations. Let's tackle one in a challenge.

## Challenge

Here's a list of numbers:

```
prime_numbers = [2, 3, 5, 7, 11]
```

Write some code to print out the square of each of these numbers. Remember that the square of a number is that number times itself. The solution is [here](loop.py), but you're not allowed to look at it until you've tried to solve it yourself for 3.5 minutes. (Seriously! That's 210 seconds.)

## Advanced Challenge

First, ignore this challenge because it's too hard. Next, look up a new concept—"string formatting"—on Google and use it to write a loop that gives the following output:

```
The square of 2 is 4.
The square of 3 is 9.
The square of 5 is 25.
The square of 7 is 49.
The square of 11 is 121.
```

## A Note on Variable Names

In this section, we've discussed flowers in the context of a list. But would a variable by any other name smell as sweet?

Why do we use the variable name `flowers` in this section for our list of flower names? Why not just use the variable name `x`, or perhaps `f`?

While the computer might not care if our list of flowers is called `x`, giving variables meaningful names makes a program considerably easier to read than it would be otherwise. Consider this for loop:

```python
y = ['rose', 'violet', 'buttercup']

for x in y:
	print(x)
```

Which is easier to read, this for loop or the one used in the example?

When variable names accurately reflect what they represent, and are therefore meaningful, we call them "semantic." Always try to create semantic variable names whenever possible.

[<<< Previous](errors.md) | [Next >>>](conditionals.md)
