# Requests with cURL

Now that we're a little familiar with basic commands for navigating our file system, moving files, and exploring datasets, let's see how we can communicate with other computers using the cURL command.

[cURL](https://curl.haxx.se/) is a command-line application for performing requests using a variety of protocols including HTTP. We're going to look at how to use it when doing HTTP requests.

## HTTP

HTTP is the protocol used to fetch data from web servers. The protocol also allows information to get sent to the servers.

The client, cURL, sends a HTTP request. The request contains a method (like GET, POST, HEAD etc), a number of request headers and sometimes a request body. The HTTP server responds with a status line (indicating if things went well), response headers and most often also a response body. The "body" part is the plain data you requested, like the HTML or the image, etc.

If you want to see what's going on, you can use curl's option --verbose (-v as a short option), to display the commands curl is sending to the server.

## URL

The **Uniform Resource Locator** format is how you specify the address of a resource on the internet.

The **protocol** is the first part of the URL and describes how your computer will talk to the remote computer. You can think of protocols as agreed-on ways of transferring data. Three commonly-used protocols are HTTP (Hypertext Transfer Protocol), HTTPS (Secure Hypertext Transfer Protocol), and FTP (File Transfer Protocol). The protocol might look like this:

	http://
	
The **domain** is a human-readable address for a website. The domain might look like this:

	dhsi.org
	
The **path** refers to additional locations within a website

	/courses.php
	
The URL can contain additional information. One such type of information, the query parameter, will be discussed later in the week.

## HTTP Methods

HTTP has a number of **methods** that determine which way information is flowing in a request and what is done with the information. The two most important for our purposes are GET and POST. GET requests that information be delivered from the remote server to the local machine. POST instead sends data to the remote server, where it is processed.

## cURL Commands

The most common cURL command is to GET a URL. The URL could itself refer to a web page, an image or a file. The client issues a GET request to the server and receives the information (document, image, etc)  it asked for. If, in your terminal, you you issue the command:

	curl https://curl.haxx.se

you will get a web page returned in your terminal window in HTML format.

All HTTP replies contain a set of response headers that are normally hidden, use curl's `--include` (`-i`) option to display them as well as the rest of the document.

### HEAD

Using the `--head` (`-I`) option will make curl issue a HEAD request. In other words, you will only see the headers associated with the URL.

You can send requests to multiple URLs in one command, and you can send requests with different HTTP protocols to one URL.

two GETs:

	curl http://url1.example.com http://url2.example.com

or two POSTS:

	curl --data name=curl http://url1.example.com http://url2.example.com

Multiple cURL options in a single command:

to send a HEAD then a GET:

	curl -I http://example.com --next http://example.com

or to send a POST then a GET:

	curl -d score=10 http://example.com/post.cgi --next http://example.com/results.html

## Examples

To send your password file to the server, where `<password>` is the name of the form-field to which /etc/password will be the input:

	curl -F password=@/etc/passwd www.mypasswords.com

To retrieve a web page and display in the terminal

	curl http://www.dhbox.org`

To retrieve a web page and display header information

	curl http://www.tutorialspoint.com -i

To retrieve a web page and save to a file.

	curl http://www.tutorialspoint.com -0 tutorialspoint.html

To retrieve a web page, or its redirected target

	curl www.tutorialspoint.com/unix/ 
	curl www.tutorialspoint.com/unix/ --location

To limit the rate of data transfer to 1 Kilobytes/sec

	curl http://www.tutorialspoint.com/unix/ --limit-rate 1k -o unix.html

To download via a proxy server

	curl -x proxy.example.com:3128 http://www.tutorialspoint.com/unix/

### curl party

Type  

`curl parrot.live`

These examples are derived from the [cURL official tutorial](https://curl.haxx.se/docs/httpscripting.html).
