# Quotes Scraper

A scraper for [quotes.toscrape.com](http://quotes.toscrape.com).

## Lesson Learned

- Project structure
- `scrapy.Spider`
- Shell
- CSS selector
- Logger
- Feed exports
- Items & Items Pipeline
- Sqlite & Many-to-many database architecture

## Getting Started

``` shell
$ # activate the virtualenv
$ vf activate global3 # in this case I am using virtualfish

# install dependencies
$ pip install -r requirements.txt

# create project skeleton
$ scrapy startproject quotes

$ # start crawling
$ # create database (remove if exists)
$ sqlite3 quotes.db < schema.sql

$ scrapy crawl quotes
```

To see the crawled quotes:

``` sql
SELECT
    q.id,
    q.text,
    q.author,
    GROUP_CONCAT(t.tag,', ') AS tags
FROM
    quotes q
    JOIN quotes_tags qt ON
        q.id = qt.quotes_id
    JOIN tags t ON
        qt.tags_id = t.id
GROUP BY q.id
```
