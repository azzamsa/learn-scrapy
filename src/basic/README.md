# Basic Scraper

This is the simplest working example of Scrapy scraper.

## Getting Started

``` shell
$ # activate the virtualenv
$ vf activate global3 # in this case I am using virtualfish

# install dependencies
$ pip install -r requirements.txt

$ # start crawling
$ scrapy runspider quotes.py -O quotes.json
```

The `quotes.json` will contains exactly 100 quotes. Otherwise, it doesn't work properly.
