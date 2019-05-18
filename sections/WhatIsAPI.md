[<<< Previous](introduction.md) | [Next >>>](dhbox.md)

## What is an API?

We get information through computers in many ways. Perhaps you navigated to this particular page by using a mouse or a touchpad to open a web browser, and then clicked a link. While pointing and clicking is a perfectly fine way of asking your computer to do things, it can sometimes be inefficient if there's a lot you'd like to do. For instance, if you wanted to obtain data from multiple web pages, you could copy and paste, and put that in a spreadsheet. However--there's an easier way! 

Enter computer programming, a practice in which a user writes specific code that instructs the computer to execute a particular function. Writing out your instructions, or writing a script, is more powerful--meaning, you can DO more. And in programming generally, the term API, short for Application Programming Interface, refers to a part of a computer program designed to be used or manipulated by another program. The **Interface** part of this term is key, because APIs can provide a simpler interface for you to request something from the computer. For instance, instead of asking someone to make a sandwich by sequentially instructing them to get bread and pimento cheese, if this person is an API (stick with me here), you can say, "make a sandwich!"

While not all APIs are web-based, these types are increasingly popular for data-driven work, and they're what we'll focus on in this course. A web API allows for information (like data) or functionality (what the application can do) to be manipulated by other programs via the internet. And, you'll be the one selecting and writing those other programs. For example, with Twitter’s web API, you can write a program, in a language like Python or Javascript, that can perform tasks such as favoriting tweets or collecting tweet metadata. Of course, you can do these things by pointing and clicking, but using APIs lets you work at greater speed and scale.

Before we get going, here's some vocabulary that will help us establish some common terms and concepts. Since APIs make frequent use of URLs and data storage formats, these terms primarily address those things.

When using or building APIs, you will encounter these terms frequently:

`HTTP` (Hypertext Transfer Protocol) is the primary means of communicating data on the web. You've seen this acronym in the beginning of every URL (see next definition!) in your search box. HTTP implements a number of “methods,” which tell which direction data is moving and what should happen to it. The two most common are GET, which pulls data from a server, and POST, which pushes new data to a server.

`URL` (Uniform Resource Locator) - An address for a resource on the web, such
as https://programminghistorian.org/about. A URL consists of a protocol (http://), domain (programminghistorian.org), and optional path (/about). A URL describes the location of a specific resource, such as a web page. When reading about APIs, you may see the terms URL, request, URI, or endpoint used to describe adjacent ideas. This course will use the terms URL and request. You can follow a URL or make a GET request in your browser, so there's no need for any specialized software to make requests for now.

`JSON` (JavaScript Object Notation) is a text-based data storage format that is designed to be easy to read for both humans and machines. JSON is generally the most common format for returning data through an API, XML being the second most common.

`REST` (REpresentational State Transfer) is a philosophy that describes some best practices for implementing APIs. APIs designed with some or all of these principles in mind are called REST APIs. While the API outlined in this lesson uses some REST principles, there is a great deal of disagreement around this term. For this reason, we avoid describing example APIs here as REST APIs, but instead use the term web or HTTP APIs.

[<<< Previous](introduction.md) | [Next >>>](../command-line/README.md)
