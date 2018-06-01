[<<< Previous](creating-files-and-folders.md) | [Next >>>](pipes.md)

## Creating a cheat sheet

In this section, we'll create a text file that we can use as a cheat sheet. You can use it to keep track of all the awesome commands you're learning. 

Instead of creating an empty file like we did with `touch`, let's try creating a file with some text in it. But first, let's learn a new command: `echo`

```
$ echo "Hello from the command line"
Hello from the command line
```

By default, the echo command just prints out the text we give it. Let's use it to create a file with some text in it:

```
echo "This is my cheat sheet" > cheat-sheet.txt
```

Now let's check the contents of the directory:

```
$ pwd
/Users/jojo/projects
$ ls
cheat-sheet.txt
```

OK, so the file has been created. But what was the `>` in the command we used? On the command line, a `>` is known as a "redirect." It takes the output of a command and puts it in a file. Be careful, since it's possible to overwrite files with the `>` command.

Let's check if there's any text in cheat-sheet.txt.

```
cat cheat-sheet.txt
This is my cheat sheet
```

As you can see, the `cat` command prints the contents of a file to the screen. 

### A note on file naming

Your cheat sheet is titled `cheat-sheet.txt` instead of `cheat sheet.txt` for a reason. Can you guess why?

Try to make a file titled `cheat sheet.txt` and report to the class what happens. 

Now imagine you're attempting to open a very important data file using the command line that is titled `cheat sheet.txt`. 

For your digital best practices, we recommend making sure that file names contain no spaces--you can use creative capitalization, dashes, or underscores instead. 

### Using a text editor

The challenge for this section will be using your DH Box text editor, Brackets, to add some of the commands that we've learned to the newly created cheat sheet. Text editors are programs that allow you to edit plain text files, such as .txt, .py (Python scripts), and .csv (spreadsheet files). Remember not to use programs such as Microsoft Word to edit text files, since they add invisible characters that can cause problems. 

## Challenge

From your programs menu, via Finder or Applications or Launchpad in Mac OSX, via Windows button in Windows, open your Visual Studio Code text editor:

	code cheat-sheet.txt

Type to add the commands we've learned so far to the file. Include descriptions about what each command does. Remember -- this cheat sheet is for you. Write descriptions that make sense to you or take notes about questions.

Save the file.

Once you're done, check the contents of the file on the command line with the `cat` command:

```
$ cat cheat-sheet.txt
My Institute Cheat Sheet

ls
lists files and folders in a directory

cd ~
change directory to home folder

...
```

[<<< Previous](creating-files-and-folders.md) | [Next >>>](pipes.md)

### Example

![Creating a Cheat Sheet](cheat-sheet.gif)
