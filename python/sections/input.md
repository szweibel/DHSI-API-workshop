[<<< Previous](conditionals.md) | [Next >>>](google.md)

## Input

**Note:** If you're using Python 2.7, replace all `input()` functions in the code below with `raw_input()`. You can check your version by running `python --version` in the command line.

Python allows you to take input directly from the user using the `input` function. Let's use it to improve our weather application by asking for the weather before displaying the output.

```
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

### Asking repeatedly

What if we want Python to keep asking for input instead of exiting after the first question is answered? For that, we can use something called a while loop.

Remember our for loop? Instead of iterating through a list like the for loop, our while loop will continue to execute as long as a certain condition is true. Here's a very simple while loop that will run forever until you quit it manually.

```
while True:
	print("Oh no! I'm stuck...")
```

In the terminal, you can escape from this endless loop by pressing `Control-c` on your keyboard.

Let's apply the while loop to our weather app:

```
while True:
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

Notice that we had to shift everything over one tab to fit it in the `while` block. Now our program will ask us for input again and again, and give us different answers each time.

Let's add one more feature: an `elif` statement that will break us out of the loop and end the program:

```
while True:
    weather = input("What is the weather like today? ")

    if weather == "sunny":
        print("Bring your shades")
    elif weather == "quit":
        break
    elif weather == "rainy":
        print("Bring your umbrella")
    elif weather == "snowy":
        print("Bring your wooly muffler")
    else:
        print("I don't know what you should bring! I'm just a little program...")
```

The `break` command ends the current loop early, ending the program when "quit" is given as input.

### Challenge

1\. How much of the code above do you understand? Even if you do kind of understand it, do you "grok" it—that is, *really* understand it?

Open up your REPL (type `python` at the `$` prompt). Play around with `input()` a bit until you understand it's behavior really well. Write a two-line program in the REPL or in a script that takes some input and echoes it back to the user.

Alternatively, mess around with `while`. Try using things other than `True` and see if the code in the loop runs. If you can, write a while loop that prints out the numbers from 1 to 10 and stops.

2\. (optional) Read a little about the weird word [grok](grok.md).

[<<< Previous](conditionals.md) | [Next >>>](google.md)
