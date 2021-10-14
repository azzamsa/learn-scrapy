## Scrapy shell

``` shell
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

>>> response.css('title::text')
[<Selector xpath='descendant-or-self::title/text()' data='Quotes to Scrape'>]

>>> response.css('title::text').getall()
['Quotes to Scrape']

>>> response.css('title::text').get()
'Quotes to Scrape'

>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
```


## Using XPath

``` shell
>>> response.xpath('//title/text()').get()
'Quotes to Scrape'
```

