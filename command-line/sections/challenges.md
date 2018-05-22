
### Further challenges

These challenges are ordered from easiest to hardest. Let [me](https://github.com/smythp) know you've completed them all and I'll give you a bag of candy! And no, it's not cheating if you ask for help.

#### Challenge #1: Create hidden file

Use the `touch` command to create a hidden file. Hidden files have a `.` in front of them, like this:

```
$ ls -A
.gitignore hello.txt
$ ls
hello.txt
```

You can also create hidden folders this way, but you only need to create a file to pass the challenge. 


### Challenge #2: Create an alias

All these commands are great and all, but what if I want to make my own command? For example, maybe I want to make this happen:

```
$ peptalk
Good work
```

To do this, use the `alias` command:

```
$ alias peptalk="echo Good work"
```

To pass this challenge, make your own alias that does something different.

### Challenge #3: Make a permanent alias

So you made an alias, but you realized it goes away when you close and reopen the terminal. (So unfair.) Make your alias permanent.

To do this, you will need to edit the configuration file that your terminal runs when it starts up. On Git Bash, that's going to be called `~/.bashrc`. (That's a `.bashrc` file in your home folder.) On OSX, the file is called `~/.bash_profile`. Just add the command you used to create the alias to the file with your text editor. Close and reopen the terminal to make sure your alias still works.

### Challenge #4: Create your own shell script 

You're having fun with aliases, but are they REAL programs, or just glorified shortcuts?

This challenge is to create a bash script, a REAL program written in bash. To do this, create a text file (I'll call this one `goto-projects.sh`) that begins with this line:

```
#!/bin/bash
```

Under that, write some lines of bash that you want to be executed. How about a program that goes to your projects folder from wherever you are?

```
cd ~/Desktop/projects
echo "Now you're in $(pwd)"
```

Your script should look like this when you're done.

goto-projects.sh:
```
#!/bin/bash

cd ~/Desktop/projects
echo "Now you're in $(pwd)"
```

Now run this command to make your script executable. This gives your computer permission to run it as a program:

```
$ chmod a+x goto-projects.sh
```

Now run your program like this:

```
$ ./goto-projects.sh
```

### Challenge #5: Make your script run from anywhere

Last challenge! So you've made a real program in bash, you're probably feeling pretty proud of yourself. Deservedly so. But you still need to be in a folder with your program, and you still need to use that annoying `./` to run it. Let's make our program accessible from anywhere on the system by moving it to the `/bin` folder.

```
sudo mv goto-projects.sh /bin/goto-projects
```

This moves your script from its current folder to the `/bin` folder and renames it from `goto-projects.sh` to `goto-projects`. Now close your terminal with `exit` and reopen it. Type 

````
$ goto-projects
````

from anywhere and see if that runs your script. If it does, congratulations! You're a force to be reckoned with on the command line.
