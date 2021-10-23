# Quotes Scraper

A scraper for [quotes.toscrape.com](http://quotes.toscrape.com).

## Getting Started

``` shell
$ # activate the virtualenv
$ vf activate global3 # in this case I am using virtualfish

# install dependencies
$ pip install -r requirements.txt

# create project skeleton
$ scrapy startproject quotes

$ # start crawling
$ # -O to overwrite, -o to append
$ scrapy crawl quotes -O quotes.json
```
