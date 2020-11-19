# web_scraper
Python Web Scraper


I took on this personal project in order to learn more about real-world applications of coding (i.e how to extract information that is contained on the web and save it in a json format that can be used to manipulate and save large amounts of data. This project was a small scale example of how python can extract data and save it into a JSON format. 

The first part of my project was to access the url: (ethans fake twitter site) and extract all of the information from the web page (“Scrape the website”).

This was done by using pythons’ request, beautifulsoup and JSON library. Each individual tweet was added into a python dictionary with the key information such as author, date, tweet text, likes and shares. Then I proceeded to create a write JSON file where I archived all of the tweets into a JSON list. By doing this, I was able to create my own "data base" where the tweets could be searched through for information and or manipulated. 

The second part of my project dealt with using the JSON data that was created in the first part.

With my first demonstration, I found all the tweets that Jimmy Fallon used the key words “Obama” and “thank you”. The results showed that Jimmy Fallon had mentioned Obama 35 times and thank you notes 29 times. This demonstration was a proof of concept of how data can be taken from the web and phrased in such manner where the keyword information can be located.

The second demonstration isolated all the dates that Jimmy Fallon had tweeted and creating a separate repository named Dates.json in order to log which days Jimmy Fallon had tweeted.
