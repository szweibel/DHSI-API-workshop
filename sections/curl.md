## Requests with cURL

Now that we're a little familiar with basic commands for navigating our file system, moving files, and exploring datasets, let's see how we can communicate with other computers using the cURL command.

cURL is a command-line application for performing requests using a variety of protocols including HTTP. We're going to look at how to use it when doing HTTP requests.

### HTTP

HTTP is the protocol used to fetch data from web servers. The protocol also allows information to get sent to the servers.

The client, cURL, sends a HTTP request. The request contains a method (like GET, POST, HEAD etc), a number of request headers and sometimes a request body. The HTTP server responds with a status line (indicating if things went well), response headers and most often also a response body. The "body" part is the plain data you requested, like the HTML or the image etc.

If you want to see what's going on, you can use curl's option --verbose (-v as a short option), to display the commands curl is sending to the server.

### URL

The **Uniform Resource Locator** format is how you specify the address of a resource on the internet.

### GET

The most common request/operation made using HTTP is to GET a URL. The URL could itself refer to a web page, an image or a file. The client issues a GET request to the server and receives the document it asked for. If you issue the command line

 curl https://curl.haxx.se

you get a web page returned in your terminal window. The entire HTML document that that URL holds.

All HTTP replies contain a set of response headers that are normally hidden, use curl's --include (-i) option to display them as well as the rest of the document.

### HEAD

Using the --head (-I) option will make curl issue a HEAD request. In other words, you will only see the headers associated with the URL.

You can send requests to multiple URLs in one command, and you can send requests with different HTTP protocols to one URL.

two GETS:

`curl http://url1.example.com http://url2.example.com`

or two POSTS:

`curl --data name=curl http://url1.example.com http://url2.example.com`

Multiple HTTP methods in a single command line

to send a HEAD then a GET:
`curl -I http://example.com --next http://example.com`

or

to send a POST then a GET:

`curl -d score=10 http://example.com/post.cgi --next http://example.com/results.html`

EXAMPLES
To send your password file to the server, where 'password' is the name of the form-field to which /etc/passwd will be the input:

$ curl -F password=@/etc/passwd www.mypasswords.com

To retrieve a web page and display in the terminal

`$ curl http://www.dhbox.org`

To retrieve a web page and display header information

$ curl http://www.tutorialspoint.com -i
To retrieve a web page and save to a file.

$ curl http://www.tutorialspoint.com -0 tutorialspoint.html
To retrieve a web page, or its redirected target

$ curl www.tutorialspoint.com/unix/ 
$ curl www.tutorialspoint.com/unix/ --location
To limit the rate of data transfer to 1 Kilobytes/sec

$ curl http://www.tutorialspoint.com/unix/ --limit-rate 1k -o unix.html
To download via a proxy server

$ curl -x proxy.example.com:3128 http://www.tutorialspoint.com/unix/

### 