# An API Case Study: Sensationalism and Historical Fires

Imagine that our research area is sensationalism and the press: has newspaper coverage of major events in the United States become more or less sensational over time? Narrowing the topic, we might ask whether press coverage of, for example, urban fires has increased or decreased with government reporting on fire-related relief spending.

While we won't be able to explore this question thoroughly, we can begin to approach this research space by collecting historical data on newspaper coverage of fires using an API—in this case, the [Chronicling America Historical Newspaper API](http://chroniclingamerica.loc.gov/about/api/). The Chronicling America API allows access to metadata and text for millions of scanned newspaper pages. In addition, unlike many other APIs, it also does not require an authentication process, allowing us to immediately explore the available data without signing up for an account.

Our initial goal in approaching this research question is to find all newspaper stories in the Chronicling America database that use the term "fire." Typically, use of an API starts with its documentation. On the [Chronicling America API page](http://chroniclingamerica.loc.gov/about/api/), we find two pieces of information critical for getting the data we want from the API: the API's **base URL** and the **path** corresponding to the function we want to perform on the API—in this case, searching the database.

Our base URL is:

	http://chroniclingamerica.loc.gov

All requests we make to the API must begin with this portion of the URL. All APIs have a base URL like this one that is the same across all requests to the API.

Our path is:

	/search/pages/results/

If we combine the base URL and the path together into one URL, we'll have created a request to the Chronicling America API that returns all available data in the database:

	http://chroniclingamerica.loc.gov/search/pages/results/

If you [visit the link above](http://chroniclingamerica.loc.gov/search/pages/results/), you'll see all items available in Chronicling America (12,243,633 at the time of writing), , not just the entries related to our search term, "fire." This request also returns a formatted HTML view, rather than the structured view we want to use to collect data.

According to the Chronicling America documentation, in order to get structured data specifically relating to fire, we need to pass one more kind of data in our request: **query parameters**.

	http://chroniclingamerica.loc.gov/search/pages/results/?format=json&proxtext=fire

The query parameters follow the `?` in the request, and are seperated from one another by the `&` symbol. The first query parameter, `format=json`, changes the returned data from HTML to JSON. The second, `proxtext=fire`, narrows the returned entries to those that include our search term.

If you [follow the above link](http://chroniclingamerica.loc.gov/search/pages/results/?format=json&proxtext=fire) in your browser, you'll see a structured list of the items in the database related to the search term "fire." The format of the returned data is called JSON, and is a structured format that looks like this excerpt from the Chronicling America results:

```json
"city": [
        "Washington"
      ],
      "date": "19220730",
      "title": "The Washington Herald.",
      "end_year": 1939,
```

By making requests to the Chronicling America API, we've accessed information on news stories that contain the search term "fire," and returned data that includes the date of publication and the page the article appears on. If we were to pursue this research question further, a next step might be finding how many stories relating to fire appear on a newspaper's front page over time, or perhaps cleaning the data to reduce the number of false positives. As we have seen, however, exploring an API can be a useful first step in gathering data to tackle a research question.

<div class="alert alert-warning">
Note that in this section, we skipped an important step: finding an appropriate API in the first place. Some resources for researching APIs are available at the end of this lesson.
</div>
