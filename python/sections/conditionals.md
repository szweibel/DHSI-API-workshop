[<<< Previous](loops.md) | [Next >>>](input.md)

# Conditionals

Conditionals allow programs to change their behavior based on whether some statement is true or false. Let's try this out by writing a script that will give different outputs based on the weather:

```
weather = "sunny"

if weather == "sunny":
    print("Bring your shades")
else:
    print("I don't know what you should bring! I'm just a little program...")
```

In our first line, we set a variable `weather`  to the string "sunny," representing what the weather is like outside. The `if` statement checks whether the variable weather is set to "sunny." If it is, the code in the block beneath is executed, so the text "Bring your shades" will be printed.

The `else` statement handles any inputs that aren't "sunny"—the program merely prints out that it doesn't know what you should bring. Try this script out both with the variable set to "sunny" and the variable set to some other value. 

What if we want our program to handle other kinds of weather, giving different messages for each one? Other cases after the first `if` statement are handled with `elif`:

```
weather = "sunny"

if weather == "sunny":
    print("Bring your shades")
elif weather == "rainy":
    print("Bring your umbrella")
elif weather == "snowy":
    print("Bring your wooly muffler")
else:
    print("I don't know what you should bring! I'm just a little program...")
```

You can add as many `elif` statements as you need, meaning that conditionals in Python have one `if` statement, any number of `elif` statements, and one `else` statement that catches any input not covered by `if` or `elif`. Over the next sections, we'll work on improving this little application, making it able to handle user input directly.

## Challenge

Add two more elif statements to this program to make it better able to handle different kinds of weather.

[<<< Previous](loops.md) | [Next >>>](input.md)
