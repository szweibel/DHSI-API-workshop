[<<< Previous](pipes.md) | [Next >>>](grep.md)

## Exploring text data

So far the only text file we've been working with is our cheat sheet. Now, this is where the command line can be a very powerful tool: let's try working with a large text file, one that would be too large to work with by hand.

Let's download the data we're going to work with:

[Download nypl_items.csv](http://smythp.com/hosted/nypl_items.csv)

Once the file is downloaded, move it from your Downloads folder to the `projects` folder on your desktop. (Either navigate to your Downloads folder from the command line and type `mv nypl_items.csv ~/Desktop/projects/` to move the file "nypl_items.csv" from the current directory to your projects directory on your Desktop, or drag and drop in the GUI).

Our data set is a list of public domain items from the New York Public Library. It's in .csv format, which is a plain text spreadsheet format. CSV stands for "comma separated values," and each field in the spreadsheet is separated with a comma. It's all still plain text, though, so we can manipulate the data using the command line.

### Interlude for Jojo's favorite command line feature: tab completion.

When you are navigating in the command line, typing folder and file names can seem to go against the promise of easier communication with your computer. Enter `tab` completion, stage right. So far, I've been asking you to type everything carefully, paying close attention to your spelling. The way tab completion works is that it fills in—*correctly*—the remaining characters of a file you begin typing. It only works from the point that a file name is distinct -- so if you have intro-to-command-line1.txt and intro-to-commandline2.txt, it will only go as far as it can. This trick can help immensely as it will only work if the file already exists.

### Viewing data in the command line

Try using `cat` to look at the data. You'll find it all goes by too fast to get any sense of it. (You can do Control-C to cancel the output if it's taking too long.) 

Instead, let's use another tool to get the data one page at a time:

```
$ less nypl_items.csv
[...]
```

This gives you a paginated view of the data. You can use `Control-v` and `Alt-v`to move down or up one page. (On Macs, use `<Command-v>` and `<Option-v>`.) Once you're done, hit `q` to return to the command line. 

Let's try two more commands for viewing the contents of a file:

```
$ head nypl_items.csv
[...]
$ tail nypl_items.csv
[...]
```

These commands print out the first and last sections of the file respectively.

### Note: Clearing Text

If all the text remaining in your terminal window is starting to overwhelm you, you have some options. Try `clear` or type `command` + `k` to clear the scrollback. In Mac OSX terminal, `command` + `l` will clear the output from your most recent command.

### Cleaning the data

We didn't tell you this before, but there are duplicate lines in our data! Two, to be exact. Before we try removing them, let's see how many entries are in our .csv file:

```
$ cat nypl_items.csv | wc -l
100001
```

This tells us there are 100,001 lines in our file. The `wc` tool stands for "word count," but it can also count characters and lines in a file. We tell `wc` to count lines by using the `-l` flag. If we wanted to count characters, we could use `wc -m`.

To find and remove duplicate lines, we can use the `uniq` command. Let's try it out:

```
$ cat nypl_items.csv | uniq | wc -l
99999
```

OK, the count went down by two because the `uniq` command removed the duplicate lines. But which lines were duplicated?

```
$ $ cat nypl_items.csv | uniq -d
[...]
```

The `uniq` command with the `-d` flag prints out the lines that have duplicates. 

### Challenge

Use the commands you've learned so far to create a new version of the `nypl_items.txt` file. (Hint: redirects are your friend.)

[<<< Previous](pipes.md) | [Next >>>](grep.md)

![exploring data](data.gif)

