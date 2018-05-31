[<<< Previous](repl.md) | [Next >>>](variables.md)

## Types

Types are classifications that let the computer know how a programmer intends to use a piece of data. You can just think of them as, well, types of data.

We've already seen one type in the last section: the integer. In this section, we'll learn four more: the floating point number, the string, the boolean, and the list.

Enter these lines as you see them below:

```
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> type("Hello there!")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type([1, 2, 3])
<class 'list'>
```

Each of these represents a different type:

Float: `1.0`

Floats are numbers with decimals, and are treated a little differently than integers.

String: `"Hello there!"`

Strings are arbitrary sets of characters, such as letters and numbers. You can think of them as a way to store text.

Boolean: `True` and `False`

Boolean is a fancy term for values representing "true" and "false," or "truthiness" and "falsiness."

List: `[1, 2, 3]`

A list is an ordered collection of values. You can put any type in a list: `["rose", "daisy", "buttercup"]` is also a valid list.

Don't worry about trying to actively remember these types. We'll be working with each in turn in the following sections.

## What's the deal with type()?

`type()` is a function. You can think of functions in Python in a few different ways:

1. A way of doing something in Python.
2. A way of saving some code for reuse.
3. A way of taking an input, transforming that input, and returning an output. The input goes in the parentheses `()`.

These are all valid ways of thinking about functions. We'll be learning more about functions in later sections.

[<<< Previous](repl.md) | [Next >>>](variables.md)
