[<<< Previous](getting-to-the-command-line.md) | [Next >>>](creating-files-and-folders.md)

## Navigation

#### Prefatory Pro Tip

Go slow at first, and check your spelling!

One of the biggest things you can do to make sure your code runs correctly and you can use the command line successfully is to make sure you check your spelling! Keep this in mind today, this week, and your whole life. If at first something doesn't work, your spelling will be the first thing you check. Unlike in human reading, where letters operate simultaneously as atomistic symbols and as complex contingencies (check Johanna Drucker on the alphabet), in coding, each character has a discrete function. 

### Getting started: know thyself

You may also see your username to the left of the `$`. Let's try our first command. Type the following and press enter:

```
$ whoami
```

The `whoami` command should print out your username. Congrats, you've executed your first command! This is a basic pattern of use in the command line: type a command and receive output.

### Orienting yourself in the command line: folders

OK, we're going to try another command. But first, let's make sure we understand some things about how your computer's filesystem works.

Your computer's files are organized in what's known as a hierarchical filesystem. That means there's a top level or "root" folder on your system. That folder has other folders in it, and those folders have folders in them, and so on. You can draw these relationships in a tree:

```
Users
|
-- jojokarlin
  |
  -- Applications
  -- Desktop
  -- Documents
```

The root or highest-level folder on OSX is just called `/`. We won't need to go in there, though, since that's mostly just files for the operating system. On Windows, the root directory is usually called `C:` ([More on why C is default on Windows](http://www.todayifoundout.com/index.php/2015/04/c-drive-default-windows-based-computers-2/).).

OK, let's try a command that tells us where we are in the filesystem:

```
$ pwd
```

You should get output like `/Users/jojo`. That means you're in the `jojo` directory in the `Users` folder inside the `/` or root directory. On Windows, your output would instead be `C:/Users/jojo`. The folder you're in is called the working directory, and `pwd` stands for "print working directory."

The command `pwd` won't actually print anything except on your screen. This command is easier to grasp when we interpret "print" as "display."

OK, we know where we are. But what if we want to know what files and folders are in the `jojo` directory, a.k.a. the working directory? Try entering:

```
$ ls
```

You should see a number of folders, probably including `Documents`, `Desktop`, and so on. You may also see some files. These are the contents of the current working directory. 

I wonder what's in the Desktop folder? Let's try navigating to it with the following command:

```
$ cd Desktop
```

(Make sure the "D" in "Desktop" is capitalized. ) If the command was successful, you won't see any output. This is normal—often, the command line will succeed silently. 

So how do we know it worked? That's right, let's use our `pwd` command again. We should get:

```
$ pwd
/Users/jojo/Desktop
```

Now try `ls` again to see what's on your desktop. These three commands—`pwd`, `ls`, and `cd`—are the most commonly used in the terminal. Between them, you can orient yourself and move around. 
 

Before we move on, let's take a minute to navigate through our computer's file system using the command line.

# Challenge

Use the three commands you've just learned—`pwd`, `ls` and `cd`—eight (8) times each. Go poking around your Photos folder, or see what's so special about that root `/` directory. When you're done, come back to the home folder with 

```
cd ~
```

(That's a tilde, on the top left of your keyboard.) One more command you might find useful is 

```
cd ..
```

which will move you one directory up in the filesystem. That's a `cd` with two periods after it.

### Compare with the GUI

It's important to note that this is the same old information you can get by pointing and clicking displayed to you in a different way. 

Go ahead and use pointing and clicking to navigate to your working directory--you can get there a few ways, but try starting from "My Computer" and clicking down from there. You'll notice that the folder names should match the ones that the command line spits out for you, since it's the same information! We're just using a different mode of navigation around your computer to see it.

[<<< Previous](getting-to-the-command-line.md) | [Next >>>](creating-files-and-folders.md)
  
### Example:  

![Navigating the command line](nav.gif)
