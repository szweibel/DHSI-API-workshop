[<<< Previous](run.md) | [Next >>>](loops.md)

# Errors in Python

Our usual response when seeing an error on a computer screen is a stress response. Our heart rate elevates and, if we cannot do what we were asking the computer to do, our frustration mounts. This is because many errors when interacting with programs are not useful or informative, and because we often have no capability to fix the program in front of us.

In Python, errors are our friends. This might be hard to accept initially, but the errors you see when running Python scripts generally do a good job of pointing you to what's going wrong in your program. When you see an error in Python, therefore, try not to fall into the stress response you may be used to when interacting with your computer normally.

## Two kinds of errors

In Python, there are two kinds of errors you will encounter frequently. One appears before the program runs, and the other appears during the execution of a program.

**syntax errors** - When you ask Python to run a program or execute a line in the REPL, it will first check to see if the program is valid Python code—that is, that it follows the grammatical or syntactical rules of Python. If it doesn't, before the program even runs, you'll see a syntax error printed out to the screen.

In this below example, the syntax error is a common one—mismatched single and double quotes, which is not allowed in Python. You can replicate the below error by opening the REPL (type `python` in the command line) and entering the line after the `>>>` prompt.
```
>>> print('This string has mismatched quotes. But Python will help us figure out this bug.")
  File "<stdin>", line 1
    print('This string has mismatched quotes. But Python will help us figure out this bug.")
                                                                                           ^
SyntaxError: EOL while scanning string literal
```

Note the carrot (`^`) underneath the mismatched quote, helpfully pointing out where the error lies. Similarly, if this error happened when running a script, Python would tell us the filename and the line number for the line on which the error occurs.

**Traceback errors** - These errors occur during the execution of a Python program when the program finds itself in an untenable state and must stop. Traceback errors are often logical inconsistencies in a program that is valid Python code. A common traceback error is referring to a variable that hasn't been defined, as below.

```
>>> print(not_a_variable)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'not_a_variable' is not defined
```

Traceback errors try to tell you a little about what happened in the program that caused the problem, including the category of error, such as `NameError` or `TypeError`.

## Debugging

Debugging is a fancy word for fixing problems with a program. Here are some common strategies for debugging a program when first learning Python:

- If the error is a syntax error, look at where the carrot is pointing.
- If the error is a syntax error, pay attention to grammatical features such as quotes, parentheses, and indentation.
- If the error is a syntax error, consider reading the program, or the offending line, backward. It's surprising, but this often helps to detect the issue.
- If the error is a traceback error, first look at the line where the error occured, then consider the general category of error. What could have gone wrong?
- If the error is a name error (NameError), check your spelling.
- If the error is a traceback error, try copying the last line of the error and pasting it into Google. You'll often find a quick solution this way.
- If you changed the program and expect a different output, but are getting old output, you may not have saved the file. Go back and make sure the file has been correctly saved.

## Challenge

Try to create as many errors as you can in the next few minutes. After getting your first two syntax errors, try instead to get traceback errors. Some areas to try include mathematical impossibilities and using math operations on types that do not support them.

[<<< Previous](run.md) | [Next >>>](loops.md)
