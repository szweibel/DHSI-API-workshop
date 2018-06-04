[<<< Previous](creating_twitterbot.md) | [Next >>>](resources.md)

# Scraping Data Using the Streaming API

1\. If you've followed the steps above, your developer key and token will automatically be used to authenticate to the Twitter Streaming API. If you haven't added your developer key and access token to my_keys.py, follow the instructions under "Getting your API key" above.  
2\. Open the scrape-simple.py file in this repository.  
3\. Scroll to the last line of the file, which looks like this:

    myStream.filter(track=['python'])

The script will search for the word in quotes ('python' above) and return all tweets matching that string. Change the word in quotes to perform a different search. You can also search multiple terms by separating words with commas, like this:

    ['APIs','research','scraping']

4\. Run the script with

	python scrape-simple.py

Python will listen for any tweets matching your search. When it detects a tweet, it will print the text to the screen. Depending on your search, you may need to wait for an appropriate tweet to be posted. If you search for a very common term, the script may have trouble keeping up with the output.  
5\. To collect more sophisticated data in a .csv file (which can be opened in Excel or LibreOffice), first open the scrape-data.py file in this repository. As above scroll to the bottom and change the last line to reflect your desired search criteria.  
6\. To start the listener and begin writing data to a .csv file, run

    python scrape-data.py >> data.csv

in the bash shell. As long as the script continues to run, data will be collected into the .csv file.  

[<<< Previous](creating_twitterbot.md) | [Next >>>](resources.md)
