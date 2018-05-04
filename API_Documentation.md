# Documentation and How to Interpret it

Documentation exists to explain what a tool is and how to use it. Too often, whether because documentation is an afterthought, or because the people responsible for making it are better programmers than communicators, technical documentation fails to make itself clear. Paradoxically, it is often necessary to already be familiar with using a tool in order to interpret the instructions about how to use it.  
Let’s take a look at some [documentation for a tool you’ve already been using.](http://www.mit.edu/afs.new/sipb/user/ssen/src/curl-7.11.1/docs/curl.html)

Taking this part as a specific example: 
```bash
curl [options] [URL...]
```

How do we interpret that? It turns out there are some conventions in documentation that are taken for granted but RARELY EXPLAINED. From [Stack Overflow](https://stackoverflow.com/questions/10925478/how-to-read-api-documentation-for-newbs):

>Underlined words are considered literals, and are typed just as they appear.
>Square brackets ( [ ] ) around an argument indicate that the argument is optional.
>Ellipses ... are used to show that the previous argument-prototype may be repeated.
>An argument beginning with a minus sign - is often taken to mean some sort of flag argument even if it appears in a position where a file name could appear.


If you are really interested, [here is the closest thing](http://pubs.opengroup.org/onlinepubs/009695399/basedefs/xbd_chap12.html) to a specification. 

How would the following work? This from the built-in Python API.

input([prompt])
>If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
```python
>>>
>>> s = input('--> ')  
--> Monty Python's Flying Circus
>>> s  
"Monty Python's Flying Circus"
```

Here’s another API example:
```
requests.get(url, params=None, &ast;&ast;kwargs)[source]
Sends a GET request.

Parameters:
url -- URL for the new Request object.
params -- (optional) Dictionary or bytes to be sent in the query string for the Request.
**kwargs -- Optional arguments that request takes.

Returns:
Response object
Return type:
requests.Response
```

Let’s spend some time on this one. url is clear enough as a parameter/argument. How about params=None? And even more obscure, &ast;&ast;kwargs? “Optional arguments that ‘request’ takes.” “Kwargs” means “Keyword Arguments”. 

See if you can find what these optional arguments can be in the documents for the Requests API. Was that clear at all?

Much of the time, documentation feels unmoored: each definition of a function or other aspect of the library is presented without context, failing to ground the reader in the tool. For example, the definition of a function may tell you that it “starts the process” without specifying what the process is. 

Thus, in approaching documentation, it helps to have a little bit of practical familiarity with the tool being described. We recommend that you first seek out small tutorials or, if necessary, stack overflow questions and answers that deal with the fundamentals. Then, you can come to the documentation with some mental framework upon which these abstract and otherwise unanchored definitions might rest. 


