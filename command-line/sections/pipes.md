[<<< Previous](creating_a_cheat_sheet.md) | [Next >>>](data.md)

## Pipes

So far, you've learned a number of commands and one special symbol, the `>` or redirect. Now we're going to learn another, the `|` or "pipe."

Pipes let you take the output of one command and use it as the input for another.

Let's start with a simple example:

```
$ echo "Hello from the command line" | wc -w
5
```

In this example, we take the output of the `echo` command ("Hello from the command line") and pipe it to the `wc` or word count command, adding a flag `-w` for number of words. The result is the number of words in the text that we entered.

Let's try another. What if we wanted to put the commands in our cheat sheet in alphabetical order?

Use `pwd` and `cd` to make sure you're in the folder with your cheat sheet. Then try:

```
cat cheat-sheet.txt | sort
```

You should see the contents of the cheat sheet file with each line rearranged in alphabetical order. If you wanted to save this output, you could use a `>` to print the output to a file, like this:

```
cat cheat-sheet.txt | sort > new-cheat-sheet.txt
```

[<<< Previous](creating_a_cheat_sheet.md) | [Next >>>](data.md)

### Example

![Pipes example](pipes.gif)




