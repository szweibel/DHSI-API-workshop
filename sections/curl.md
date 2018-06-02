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

``` curl https://curl.haxx.se ```

you will get a web page returned in your terminal window in HTML format. 

If you're familiar with HTML, you will recognize the contents of a fairly conventional homepage. If you're not sure what you're looking at, try following the link [https://curl.haxx.se](https://curl.haxx.se) in another browser window to see how it compares. You'll notice the chunks of text between bracketed tags like `<h1> Everything curl </h1>` are the same things you see visually displayed by the browser.

### -i

All HTTP replies contain a set of response headers that are normally hidden, use curl's `--include` (`-i`) option to display them as well as the rest of the document.

Compare the results of 

``` 
$ curl https://curl.haxx.se
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
<title>curl</title>
<meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
<link rel="stylesheet" type="text/css" href="https://curl.haxx.se/curl.css">
<link rel="shortcut icon" href="https://curl.haxx.se/favicon.ico">
<link rel="icon" href="https://curl.haxx.se/logo/curl-symbol.svg" type="image/svg+xml">
</head>
 ```

to 

``` 
$ curl -i https://curl.haxx.se 
HTTP/1.1 200 OK
Server: Apache
X-Frame-Options: SAMEORIGIN
Last-Modified: Fri, 01 Jun 2018 02:05:05 GMT
ETag: "2024-56d8b03368654"
Cache-Control: max-age=60
Expires: Fri, 01 Jun 2018 02:07:32 GMT
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Type: text/html
Via: 1.1 varnish
Fastly-Debug-Digest: 118da82c63082081cb19f2e7bdaaaaf666ea031755480bfdba9d97b55fc9e57a
Content-Length: 8228
Accept-Ranges: bytes
Date: Fri, 01 Jun 2018 13:16:02 GMT
Via: 1.1 varnish
Age: 19
Connection: keep-alive
X-Served-By: cache-bma7029-BMA, cache-iad2636-IAD
X-Cache: HIT, MISS
X-Cache-Hits: 1, 0
X-Timer: S1527858962.149454,VS0,VE116
Vary: Accept-Encoding
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
<title>curl</title>
<meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
<link rel="stylesheet" type="text/css" href="https://curl.haxx.se/curl.css">
<link rel="shortcut icon" href="https://curl.haxx.se/favicon.ico">
<link rel="icon" href="https://curl.haxx.se/logo/curl-symbol.svg" type="image/svg+xml">
</head>
```

You don't need to know what all these bits of information mean, but you can see that the `-i` flag gives us extra information about the url before launching into the contents requested.

### HEAD

Using the `--head` (`-I`) option will make curl issue a HEAD request. In other words, you will only see the headers associated with the URL.

``` curl -I http://curl.haxx.se ```

curl was made to be flexible and will attempt to retrieve information on anything you give it. Here again, precise typing is important. If you feed curl a slightly wonky url it will do its best to get information, but to get the results you want, you need to be clear about where you send it.

### A note about switches

curl supports over 200 options like `-I` or `-i`. These switches (which indicate how the command should run) come in both short and long forms. Short options follow a single hyphen; long options follow a double hyphen. As you just saw, `--head` and `-I` will return the same results. The command line parser always parses the entire line in curl, so you can put the flags indicating options anywhere in the line.

``` curl -i https://curl.haxx.se ```

will return the same results as 

``` curl https://curl.haxx.se -i ```


### Multiple requests

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

### Some fun curl commands

#### DICT

curl lets you to retrieve definitions from the command line through DICT, the Dictionary Server Protocol, developed in 1997. The Dictionary Server Protocol (DICT) is a TCP transaction based query/response protocol that allows a client to access dictionary definitions from a set of natural language dictionary databases. 

```
curl dict://dict.org/m:curl  
curl dict://dict.org/d:heisenbug:jargon
curl dict://dict.org/d:[word you'd like defined]
```

In the commands above, the `m` stands for "Match" and the `d` stands for "Define." Visit the protocol [here](https://datatracker.ietf.org/doc/rfc2229/?include_text=1).


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
