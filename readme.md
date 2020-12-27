# fb-preditions Fork Description

This repo contains changes to the original [facebook-scrapper](https://github.com/kevinzg/facebook-scraper).
The changes were made in order to:
* Deal with blocking by facbook.
* Collect all reactions and not only likes.
* Collect more posts from each group.

It was originally made as part of the ai-project [fb-predictions]()
The revised version incorporate the use of ChromeDriver and a cookie that the user has to provide (detials below).

## Install
* Clone this repo:
```
git clone 
```

* Install requirements:
```
pip install -r requirements.txt
```

* Download [ChromeDriver](https://chromedriver.chromium.org/downloads) to the project's directory.

* Collect Cookie: when logged in to facebook, open developer tools >> networks, and copy the cookie into a file named *cookie.txt* inside *reaction* folder.


## Usage
To collect data, run the following script:
```
run.py
```
When asked, provide the name of the facebook goup you with to scrape. 

On rare occasions, the script might pause and ouptput a link. In order to continue, enter the neccessary characters to convince facebook you are not a robot.

Enjoy :)
