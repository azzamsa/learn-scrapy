# Learn Scrapy

My notes on learning Scrapy 🕷.

This is not an exhausting resource for the public to learn.
Use [official Scrapy tutorial][scrapy-tutorial] instead.

## Tutorial

Starting a new project.

``` shell
scrapy startproject tutorial
```

Minimal working example.

``` python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
```

`start_urls` is a shortcut to ` start_requests()` function.

Run the spider using:

``` shell
scrapy crawl quotes
```

### Scrapy Shell

To have a playground for selector, use Scrapy shell:

``` shell
scrapy shell 'http://quotes.toscrape.com/page/1/'
```

``` shell
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

>>> # `::text` is scrapy extension to css selector
>>> response.css('title::text').get()
'Quotes to Scrape'

>>> # you can use regex too
>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
```

### CSS Selector

``` python
>>> response.css('title').getall()
['<title>Quotes to Scrape</title>']

>>> response.css('title::text').getall()
['Quotes to Scrape']
```

`.get()` always returns a single result; if there are several matches, the content of
a first match is returned; if there are no matches, `None` is returned. `.getall()`
returns a list with all results.

To avoid having `None` from `.get()`, use `default=''`

``` python
>>> response.css('img::text').get(default='')
```

Using CSS3 pseudo-elements we can refine the result.
`::text` to select/extract text-only element. Otherwise, we get the tags included.

Use `.attrib` to return attributes for the first matching element.

``` python
>>> response.css('img').attrib['src']
'image1_thumb.jpg'

>>> # or
>>> response.css('img::attr(src)').get()
'image1_thumb.jpg'
```

📝 `.get()` and `.getall()` is the new scrapy method that are equivalent to
`.extract_first()` and `.extract()`. The difference is that the former always
return predictable result, single and list.

### Extensions to CSS Selectors

📝 Take a note that as W3C standards, CSS selectors do not support selecting text
nodes or attribute values. `::text` and `::attr(name)` is [custom Scrapy
(parsel) extension][css-extension] to CSS selectors.  It will not work with
other libraries like `lxml` or `PyQuery`.

- `title::text` selects children text nodes.
- `*::text` selects all descendant text nodes.
- `a::attr(href)` selects the href attribute value.

### XPath Selector

``` python
>>> response.xpath('//title/text()').get()
'Quotes to Scrape'
```

In contrast to Scrapy custom CSS selector such ``::attr(...)`, XPath has the
same built-in feature.

``` python
>>> response.xpath("//a/@href").getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

>>> response.css('a::attr(href)').getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

>>> # if you not prefer both, use python `attrib`
>>> [a.attrib['href'] for a in response.css('a')]
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
```

### Regular Expressions Selector

``` python
>>> response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
['My image 1',
 'My image 2',
 'My image 3',
 'My image 4',
 'My image 5']
```

To get the first matching result, use `.re_first()`.


[scrapy-tutorial]: https://docs.scrapy.org/en/latest/intro/tutorial.html
[css-extension]: https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors
