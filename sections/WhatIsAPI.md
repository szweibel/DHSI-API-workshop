[<<< Previous](introduction.md) | [Next >>>](dhbox.md)

## What is an API?

In programming generally, the term API, short for Application Programming Interface, refers to a part of a computer program designed to be used or manipulated by another program, as opposed to an interface designed to be used or manipulated by a human. Computer programs frequently need to communicate amongst themselves or with the underlying operating system, and APIs are one way they do it. In this tutorial, however, we’ll be using the term API to refer specifically to web APIs.

If you’ve heard the term API before, chances are it’s been used not to refer to APIs in general, but instead to a specific kind of API, the web API. A web API allows for information or functionality to be manipulated by other programs via the internet. For example, with Twitter’s web API, you can write a program in a language like Python or Javascript that can perform tasks such as favoriting tweets or collecting tweet metadata.

When using or building APIs, you will encounter these terms frequently:

`HTTP` (Hypertext Transfer Protocol) is the primary means of communicating data on the web. HTTP implements a number of “methods,” which tell which direction data is moving and what should happen to it. The two most common are GET, which pulls data from a server, and POST, which pushes new data to a server.

`URL` (Uniform Resource Locator) - An address for a resource on the web, such
as https://programminghistorian.org/about. A URL consists of a protocol (http://), domain (programminghistorian.org), and optional path (/about). A URL describes the location of a specific resource, such as a web page. When reading about APIs, you may see the terms URL, request, URI, or endpoint used to describe adjacent ideas. This tutorial will prefer the terms URL and request to avoid complication. You can follow a URL or make a GET request in your browser, so you won’t need any special software to make requests in this tutorial.

`JSON` (JavaScript Object Notation) is a text-based data storage format that is designed to be easy to read for both humans and machines. JSON is generally the most common format for returning data through an API, XML being the second most common.

`REST` (REpresentational State Transfer) is a philosophy that describes some best practices for implementing APIs. APIs designed with some or all of these principles in mind are called REST APIs. While the API outlined in this lesson uses some REST principles, there is a great deal of disagreement around this term. For this reason, I do not describe the example APIs here as REST APIs, but instead as web or HTTP APIs.

## An API Case Study: Sensationalism and Historical Fires
Imagine that our research area is sensationalism and the press: has newspaper coverage of major events in the United States become more or less sensational over time? Narrowing the topic, we might ask whether press coverage of, for example, urban fires has increased or decreased with government reporting on fire-related relief spending.

While we won’t be able to explore this question thoroughly, we can begin to approach this research space by collecting historical data on newspaper coverage of fires using an API—in this case, the Chronicling America Historical Newspaper API. The Chronicling America API allows access to metadata and text for millions of scanned newspaper pages. In addition, unlike many other APIs, it also does not require an authentication process, allowing us to immediately explore the available data without signing up for an account.

Our initial goal in approaching this research question is to find all newspaper stories in the Chronicling America database that use the term “fire.” Typically, use of an API starts with its documentation. On the Chronicling America API page, we find two pieces of information critical for getting the data we want from the API: the API’s base URL and the path corresponding to the function we want to perform on the API—in this case, searching the database.

Our base URL is:

`http://chroniclingamerica.loc.gov`


All requests we make to the API must begin with this portion of the URL. All APIs have a base URL like this one that is the same across all requests to the API.
Our path is:
`/search/pages/results/`


If we combine the base URL and the path together into one URL, we’ll have created a request to the Chronicling America API that returns all available data in the database:
`http://chroniclingamerica.loc.gov/search/pages/results/`


If you visit the link above, you’ll see all items available in Chronicling America (12,243,633 at the time of writing), not just the entries related to our search term, “fire.” This request also returns a formatted HTML view, rather than the structured view we want to use to collect data.
According to the Chronicling America documentation, in order to get structured data specifically relating to fire, we need to pass one more kind of data in our request: query parameters.
`http://chroniclingamerica.loc.gov/search/pages/results/?format=json&proxtext=fire`


The query parameters follow the ? in the request, and are seperated from one another by the &symbol. The first query parameter, format=json, changes the returned data from HTML to JSON. The second, proxtext=fire, narrows the returned entries to those that include our search term.
If you follow the above link in your browser, you’ll see a structured list of the items in the database related to the search term “fire.” The format of the returned data is called JSON, and is a structured format that looks like this excerpt from the Chronicling America results:
```javascript
"city": [
        "Washington"
      ],
      "date": "19220730",
      "title": "The Washington Herald.",
      "end_year": 1939,
```

By making requests to the Chronicling America API, we’ve accessed information on news stories that contain the search term “fire,” and returned data that includes the date of publication and the page the article appears on. If we were to pursue this research question further, a next step might be finding how many stories relating to fire appear on a newspaper’s front page over time, or perhaps cleaning the data to reduce the number of false positives. As we have seen, however, exploring an API can be a useful first step in gathering data to tackle a research question.

[<<< Previous](introduction.md) | [Next >>>](dhbox.md)
