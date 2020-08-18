# web-crawler
Web crawler that support both focused and unfocused crawling

### Instructions to Run the Code

Run the FocusedCrawler.py from the command prompt as follows:

1. For unfocused crawling ( that is without keyphrase)
python FocusedCrawler.py <seedurl>

e.g. python FocusedCrawler.py http://en.wikipedia.org/wiki/Karen_Sparck_Jones

1. For Focused crawling (with keyphrase)
python FocusedCrawler.py <seedurl> <keyphrase>

e.g. python FocusedCrawler.py http://en.wikipedia.org/wiki/Karen_Sparck_Jones retrieval

### Requirements for running the code

In order to execute this code python 3 must be installed. Further the following additional libraries have to be installed as well:
* requests
* bs4
