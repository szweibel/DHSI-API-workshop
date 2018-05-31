[<<< Previous](types.md) | [Next >>>](run.md)

## Variables

A variable is a symbol that refers to an object, such as a string, integer, or list. If you're not already at the Python prompt, open your terminal and type `python` at the `$`. You're in the right place when you see `>>>`.

Try these commands in order:

```
>>> x = 5
>>> x
5
>>> x + 10
15
>>> y = "hello"
>>> y
'hello'
>>> y + " and goodbye"
'hello and goodbye'
```

As you can see above, the `=` sign lets you assign symbols like `x` and `y` to data.

Variables can be longer words as well:

```
>>> breakfast = ['ham', 'eggs', 'toast']
>>> breakfast
['ham', 'eggs', 'toast']
>>> type(breakfast)
<class 'list'>
```

Variables can have letters, numbers, and underscores, but should start with a letter. 

### Challenge

So I just told you that variables shouldn't start with a number or an underscore. What does that even mean? Will your computer explode if you write `3_flower = "buttercup"`?

Only one way to find out. Try giving weird names to variables and see if you can learn a bit about the rules.

[<<< Previous](types.md) | [Next >>>](run.md)
