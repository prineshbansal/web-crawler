# web-crawler
Web crawler that supports both focused and unfocused crawling

## Instructions to Run the Code

Run the FocusedCrawler.py from the command prompt as follows:

* For unfocused crawling (crawling without keyphrase)
```
python FocusedCrawler.py <seedurl>
```
Eg:
```
python FocusedCrawler.py http://en.wikipedia.org/wiki/Karen_Sparck_Jones
```

* For focused crawling (crawling with keyphrase)
```
python FocusedCrawler.py <seedurl> <keyphrase>
```
Eg:
```
python FocusedCrawler.py http://en.wikipedia.org/wiki/Karen_Sparck_Jones retrieval
```

## Requirements for running the code

In order to execute this code python 3 must be installed. Further the following additional libraries have to be installed as well:
* requests
* bs4
