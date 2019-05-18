[<<< Previous](motivate.md) | [Next >>>](resources.md)

# Objects in Python

Objects in Python (and other programming languages) are basically containers that can hold data and/or functions inside them. When a function is inside an object, we usually call the function a "method." When data is inside an object, we usually call it an "attribute." The terminology isn't that important, though. What we do need to know is that you can access these "methods" and "attributes" with a `.` (a dot or period).

When we added lower case to our weather program, we briefly saw a method contained inside all string objects in Python—`lower()`, which makes the string lower case.

```
>>> loud_greeting = "HELLO!"
>>> loud_greeting.lower()
'hello!'
```

Many, or most, objects in Python have methods that allow you to use them in different ways. As you move into using more advanced libraries, you'll find that understanding what methods are available becomes more important.

## Examining Objects


When you encounter an object, how can you learn its methods and atributes so you can use them? There are two main ways. The first, and likely the most practical, is to read the documentation of the library you're using.

However, you can also use the `dir()` function, which will tell you which methods and attributes are available in an object.

Let's use the REPL for a moment—open it by typing `python` at the command line.

```
>>> s = 'Hello, world!'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
[...]
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

```

The above output shows all the methods and attributes available to Python strings that can be accessed using the dot (`.`) syntax. When using `dir()`, you'll mostly want to ignore the methods and attributes that have underscores around them. They mainly have to do with the internals of the Python language.

## Challenge

1. You can also use `dir()` to see what functions are available from Python libraries that you import. Try importing the random library again and see what you get when you enter `dir(random)`.
2. Try entering other objects based on Python types we've already learned to the `dir()` function. For example, you might try `dir([1, 2, 3])` to see what methods are available when using lists.

[<<< Previous](motivate.md) | [Next >>>](resources.md)
