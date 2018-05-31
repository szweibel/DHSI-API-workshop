[<<< Previous](getting-to-the-command-line.md) | [Next >>>](creating-files-and-folders.md)

## Navigation part 1: who am I and where am I?

#### Prefatory Pro Tip

Go slow at first, and check your spelling!

One of the biggest things you can do to make sure your code runs correctly and you can use the command line successfully is to make sure you check your spelling! Keep this in mind today, this week, and your whole life. If at first something doesn't work, check your typing! Unlike in human reading, where letters operate simultaneously as atomistic symbols and as complex contingencies (check [Johanna Drucker](https://genius.com/Johanna-drucker-from-a-to-screen-annotated) on the alphabet), in coding, each character has a discrete function. 

### Getting started: know thyself

You may also see your username to the left of the `$`. Let's try our first command. Type the following and press enter:

```
$ whoami
```

The `whoami` command should print out your username. Congrats, you've executed your first command! This is a basic pattern of use in the command line: type a command and receive output.

### Orienting yourself in the command line: folders

OK, we're going to try another command. But first, let's make sure we understand some things about how a computer's filesystem works.

A computer's files are organized in what's known as a hierarchical filesystem. That means there's a top level or "root" folder on your system. That folder has other folders in it, and those folders have folders in them, and so on. You can draw these relationships in a tree:

```
Users
|
-- jojokarlin
  |
  -- Applications
  -- Desktop
  -- Documents
```

In DH Box, because we're working inside a virtual computer, we won't see many of the default folders you'd recognize on your own computer. The root or highest-level folder is just called `/`. Let's try a command that tells us where we are in the filesystem:

```
$ pwd
```

You should get output like `/home/jojokarlin`. That means you're in the `jojokarlin` directory in the `home` folder inside the `/` or root directory. On Windows, your output would instead be something like `C:/Users/jojokarlin`. The folder you're in is called the working directory, and `pwd` stands for "print working directory."

The command `pwd` won't actually print anything except on your screen. This command is easier to grasp when we interpret "print" as "display."

Before we can get very far, we need to put some folders into our DH Box.

[<<< Previous](getting-to-the-command-line.md) | [Next >>>](creating-files-and-folders.md)
  
### Example:  

![Navigating the command line](nav.gif)
