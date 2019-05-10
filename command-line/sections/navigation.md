[<<< Previous](getting-to-the-command-line.md) | [Next >>>](creating-files-and-folders.md)

## Navigation part 1: who am I and where am I?

#### Prefatory Pro Tip: check your spelling

Command line proficiency highly correlates with correct spelling. Your computer can't guess at what word you may have meant--it'll just give up, and your code won't run. If at first something doesn't work, check your typing! Unlike in human reading, where letters operate simultaneously as atomistic symbols and as complex contingencies (check [Johanna Drucker](https://genius.com/Johanna-drucker-from-a-to-screen-annotated) on the alphabet), in coding, each character has a discrete function. 

### Getting started: know thyself

You see your username to the left of the `$`. Let's try our first command. Type the following and press enter:

```
$ whoami
```

The `whoami` command should print out your username. Congrats, you've executed your first command! This is a basic pattern of use in the command line: type a command and receive output.

Also, why did we say "print," when nothing really printed? This is another conceptual detail that will help us out with the new vocabulary of the command line. To "print" something is to deliver it up on the screen, or otherwise spell it out. So while it's not text that's spitting out on a piece of paper, it's still pretty impressive, no?

### Orienting yourself in the command line: folders

OK, we're going to try another command. But now that we know *who* we are on this computer, let's talk about how to know *where* we are. To understand this, we have to know how a computer's files are organized.

All files on a computer are organized in what's known as a hierarchical filesystem. That means there's a top level, which is also known as a "root" folder on your system. That folder has other folders in it, and those folders have folders in them, and so on. You can draw these relationships in a tree:

```
Users
|
-- mckinniburgh
  |
  -- Applications
  -- Desktop
  -- Documents
```

For shorthand, the root, or highest-level folder is just called `/`. Let's try a command that tells us where we are in the filesystem.

```
$ pwd
```

You should get output like `/home/mckinniburgh`. That means you're in the `mckinniburgh` directory in the `home` folder inside the `/` or root directory. On Windows, your output would instead be something like `C:/Users/mckinniburgh`. The folder you're in is called the working directory, and `pwd` stands for "print working directory."

Remember, the command `pwd` won't actually print anything except on your screen. This command is easier to grasp when we interpret "print" as "display."

And what's a directory? Directories are folders that contain other folders or files, so they're essentially spaces within your overarching filesystem. And "working" essentially means "active" here, so you're asking the computer through the command line, where am I currently active within the filesystem?

While this may not feel particularly important now, one of the key features of the command line is that you can use it to navigate, and create things in different directories or folders. So it's good to know where you stand--and `pwd` will always let you know. 

[<<< Previous](getting-to-the-command-line.md) | [Next >>>](creating-files-and-folders.md)
  
### Example:  

![Navigating the command line](nav.gif)
