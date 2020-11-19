#Author: Ajay Dhawan
#Date: Feb 19, 2020
#Goal: To extract all of the tweets from a dummy twitter page


#imports the Apache2 Licensed HTTP library.
#This allows us to access content from web pages
import requests
#BeautifulSoup is used to extract data from web pages
from bs4 import BeautifulSoup
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'

#Here we will requests the data from the fake twitter page
result = requests.get(url)


# We will now store the data from the page in a string
#The data we are storing are the urls from the site
src = result.content
#BeautifulSoup allows us to take the data we have extracted and
#parse the data through the html.parser API
content = BeautifulSoup(src, 'html.parser')

#From the website inspect element we can see that
#the entire tweet in contained in the tweet container
#the author is under the <h2> tag with the class named author
#the tweet is under the tag <p> with the class named content
#the likes and shares are also in the p tag with classes named likes and shares
#the data and time in the <h5> tag with class name date and time

#We will now go through the page and find all attributes with the tag p
#and that have the classes named content
tweetList = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    #While going through each tweets we will only want the content
    #and not the name or id of the attribute which .text will help us get
    #.text only extracts the text from the tag

    #This will be contained in a tweet object
    tweetObj = {
        "author": tweet.find('h2', attrs={"class":"author"}).text,
        "date": tweet.find('h5', attrs={"class":"dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class":"content"}).text,
        "likes": tweet.find('p', attrs={"class":"likes"}).text,
        "shares": tweet.find('p', attrs={"class":"shares"}).text

    }
    tweetList.append(tweetObj)

#Here we create and open a json file in write mode
with open('twitterData.json','w') as outfile:
#The list of objects will then be added to our own json data base
    json.dump(tweetList,outfile,indent=2)
