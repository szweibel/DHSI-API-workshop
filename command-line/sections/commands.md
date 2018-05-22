## Commands

`pwd` - show the current (or "working") directory. Stands for "print working directory"

`ls` - show the files and folders in the working directory. I think of it as standing for "list stuff," but it's probably just short for "list."

`cd` - move to a directory, i.e. `cd Desktop` will move to the "Desktop" folder. Some special cases:

- `cd ..` - go to the directory above
- `cd ~` go to your "home" directory, i.e. /Users/<yourname>
- `cd` (by itself) also goes to the home directory
- `cd -` go to the last directory you were in before the current
- `cd ../..` travel two directories up
- `cd Documents/thesis-drafts` move two directories, from the home folder to "thesis-drafts," skipping "Documents"

`touch <filename>` - Create an empty text file named <filename> in your current directory.

`echo "Hello from the command line"` - Print out any text you give it, in this case "Hello from the command line"

`cat <filename>` - Print the contents of a file to the screen, in this case the contents of `<filename>`

`>` - Redirects printed output to a text file, as in `echo "this is some text" > hello.txt`

`rev` - Reverses the text you give it, i.e. `echo "Hello there" | rev` 

`|` - Pipe symbol. Takes output from one command and uses it as input for another command.

`less <filename>` - Print out the contents of a file in a paginated form. Use `<Control-v>` and `<Alt-v>` (or `<Command-v` and `<Option-v>`) to move up and down. Press `q` to quit.

`head <filename>` - Print the first section of a file

`tail <filename>` - Print the last section of a file

`wc -l` - Takes input and returns the number of lines in that input, as in `cat <filename> | wc -l`

`uniq` - Remove duplicate lines from input, as in `cat <filename> | uniq`. To show the duplicate files, use `uniq -d`.

`mv` - Move or rename a file. For example, `mv file1 file2` will rename `file` to `file2`. You can also specify another destination, so that `mv file1 ~` will move file1 to the home folder without renaming it.

Also check out [other useful commands](other-commands.md)
