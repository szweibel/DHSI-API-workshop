### What was "print"?

The `print()` statement you used in the last section is an example of a function. We'll talk more about functions later, but for now you can think of them as actions that are performed on a piece of data. The `print()` function operates on the data within the parentheses by printing that data to the screen.

Let's try out another function that will help us to learn more about the kinds of data available to us in Python:


### IDE

An IDE (Integrated Development Environment) is a program that can be used for both writing and running scripts, and they usually come with a number of specialized features. Python comes with its own IDE, but it only runs well on Windows and Linux, not on OSX. More powerful cross-platform IDEs for Python, such as [PyCharm](https://www.jetbrains.com/pycharm/) and [Spyder](https://pythonhosted.org/spyder/) will also allow you to write and run Python programs on your desktop. Check out these tutorials if you're interested in using an IDE to write and execute Python code:

[IDLE tutorial (not recommended for OSX)](https://www.youtube.com/watch?v=lBkcDFRA958)  
[PyCharm Quickstart](https://www.jetbrains.com/help/pycharm/2016.1/quick-start-guide.html)  
[Spyder tutorial](http://datasciencesource.com/python-with-spyder-tutorial/)  




### IPython Notebook

IPython Notebooks are graphical interfaces to Python that run in the browser. To start a notebook, enter 

    $ ipython notebook
	
in your terminal. You should see messages appear in your terminal window, and your browser should open to a list of files. Once IPython is open in the browser, click `New` in the top right and select `Python` under `Notebook` from the dropdown menu.

THe IPython interface consists of cells, which can contain text or Python code. In the first cell (the blank space next to the text that says `In [ ]`, enter the text

	print("Hello world!")
	
then hit `Shift-Enter`. You should see the output `Hello world!` appear below.
