[<<< Previous](navigation.md) | [Next >>>](creating_a_cheat_sheet.md)  

## Creating files and folders

### Creating a file

So far, we've only performed commands that give us information. Let's use a command that creates something on the computer. 

First, make sure you're in the home directory:

```
$ pwd
/Users/mckinniburgh
```

Let's move to the Desktop folder with `cd`:

```
cd Desktop
```

Once you've made sure you're in the Desktop folder with `pwd`, let's try a new command:

```
touch foo.txt
```

If the command succeeds, you won't see any output. Now move the terminal window and look at your "real" desktop, the graphical one. See any differences? If the command was successful and you were in the right place, you should see an empty text file called "foo.txt" on the desktop. Pretty cool, right?

#### Handy tip: up arrow

Let's say you liked that "foo.txt" file so much you'd like another! In the terminal window, press the "up arrow" on your keyboard. You'll notice this populates the line with the command that you just wrote. You can hit "Enter" to create another "foo.txt," or you could use your left/right arrows to change the file name to "foot.txt" to create something different. 

As we start to write more complicated and longer commands in our terminal, the "up arrow" is a great shortcut so you don't have to spend lots of time typing. 

### Creating folders

We've probably already got all sorts of files on our computer, so let's create a project folder on our Desktop so that we can keep all our work in one place. For what it's worth too, there's nothing really that special about "Desktop," except it's easy to confirm your work by using a GUI. 

First, let's check to make sure we're still in the Desktop folder with `pwd`:

```
$ pwd
/Users/mckinniburgh/Desktop
```

Once you've double-checked you're in Desktop, we'll use this command to make a folder called "projects":

```
mkdir projects
```

So, you can navigate using the GUI to confirm this folder now exists, but what if you don't want to slow down to do this? What if you just want to check from your command line window? Go ahead and use the command `ls`, which will "list" the contents of the directory you're in. Once you confirm that the projects folder was created successfully, `cd` into it. 

```
$ cd projects
$ pwd
/Users/mckinniburgh/Desktop/projects
```

OK, now you've got a projects folder that you can use throughout DHSI. It should be visible on your graphical desktop, just like the `foo.txt` file we created earlier. 

[<<< Previous](navigation.md) - [Next >>>](creating_a_cheat_sheet.md)

### Example

![Creating files and folders](make-file-folder.gif)
