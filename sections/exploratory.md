# Self Directed Exploration: THe New York Times API

In this session, you will use some of the tools you have learned (cURL, your browser, Python, research) to explore an API on your own. This session will require patience, persistence, and willingness to try different approaches until you get the results you're looking for.

## Task One: Research

Take a look at the [set of New York Times APIs](https://developer.nytimes.com/), which include APIs for the Times archive, books, and "semantic"—knowledge-based—search. Pick one and do a little research on it, including glancing at its documentation and trying a Google search about it. What do you think it does? What kind of data might it return? Though you don't know what the API does yet in concrete terms, try to think of a question you might answer using it. This question might be related to your research, or it might not.

## Task Two: Request a Key

Create a new API key for your chosen API.

1. Go to [his page](https://developer.nytimes.com/signup).
2. Enter your name and email address.
3. Enter a website. If you have a personal home page, enter that. Otherwise, enter the home page of your employer or university.
4. From the dropdown, select the name of the API you're interested in, i.e. the Books API.
5. Complete the CAPTCHA and click `Create API Key`.
6. Check your email and copy your key into a text file for reference, making sure not to include any whitespace or additional characters.

## Task Three: How does it work?

As this is a self-directed exercise, you will now attempt to figure out how the New YOrk Times API works. In particular, you're looking for this information:

1. The "base URL"—the part of any request that is consistent across all requests to the API. You may find this mentioned explicitly or your may infer it from API examples.
2. The authentication process—that is, how you use your API key to identify yourself to the service. In some cases, this is passed as part of the heading. In other cases, it may be given as part of the request path, or as a query parameter (the part of the URL after the `?`).
3. The form of the particular request you wish to make. Pick a particular request type (some of the Times APIs have only one request type, others have many). Is it GET request or a POST request? What parts of the request do you, the API user, need to change?

## Task Four: Experiment

This is the tricky part. Try to craft a working request that extracts information (at this point, any information) from the service. If your chosen request is a GET request, you can try it out by entering the created URL in the address bar of your browser.

If you're getting a `Page Not Found` or `404` message, you may not have the base URL correct.

If you are getting a message about an invalid API key, double check the key you were given. You may want to play with the formatting—try the key with quotes around it and without, for example.

You've completed this step when you've made the API return some useful information to you.

## Task Five: Explore

You may not get to this step during the session—don't worry if that's the case!

Using Python and the requests library, try to write a function that makes a request of the API. For example, if the API request looks like this:

	http://developer.movieapi.com?genre=<genre>&year=<year>
	
you might create a function that looks liek this:

```python
import requests

def search_movies(genre, year):
	request = 'http://developer.movieapi.com?genre=%s&year=%s' % (genre, year)

	requests.get(request)
	
search_movies('horror', '1987')
```







