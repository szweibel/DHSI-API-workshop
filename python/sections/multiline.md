## Multi-line string

Once you have your "Hello world!" program running, replace the text in your `hello.py` file with this:

```
print('''Mary had a little lamb,
Its fleece was white as snow,
And everywhere that Mary went,
The lamb was sure to go.''')
```

Run the program again and you should see the poem as output over four lines. 

### Why use triple quotes?

There are four ways to create strings in Python:

```
'Hello world!'
"Hello world!"
'''Hello world!'''
"""Hello world!"""
```

The first two examples allow you to create single-line strings. The last two allow you to create multi-line strings. Notice that you should not mix and match these opening and closing quotes, as you'll get an error:

```
>>> print("Hello world!')
  File "<stdin>", line 1
    print("Hello world!')
                        ^
SyntaxError: EOL while scanning string literal
```

You've probably already seen similar messages as you've tried the examples so far, but if not...congratulations on your first error! You'll see a lot of errors as you learn Python, and they're actually pretty helpful, so don't be afraid of them. We'll talk more about errors in the next section.

### Differences between the REPL and running scripts

Remember how, in the REPL, we could do things like this?

```
>>> x = 5
>>> x
5
```

In the REPL, the results after Python evaluates your input are automatically printed out for you. This is not the case with longer Python programs. If you want to see the output in the console, you'll need to use the `print()` function. (Notice that IPython cells are actually a beefed up version of the REPL that can take multiple lines, so if you're using the IPython method for running scripts, you can still do stuff like this.)
