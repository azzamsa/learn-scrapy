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

Some Xpath expression:

- `/foo/bar/baz`: select all `baz` element that are childern of `/foo/bar`.
- `//foo/bar/baz`: select all `baz` element that are childern of `/bar`.
- `/foo/bar/*`: select all element under `/foo/bar`.
- `/foo/bar/baz[1]`: select the first `baz` child of element `/foo/bar`.
- `/foo/bar/baz[last]`: select the first `last` child of element `/foo/bar`.
- `//bar[@id='bar1']`: select all `bar` element which attribute id is `bar1`.
  - other attribute value selector are: `@name`.
- `//*[count(bar)=2]`: select element that has two `bar` children.
- `//*[count(*)=2]`: selecet any element that has two children.
- `//*[name()='bar']`: select any `bar` element. Simmiliar with `//bar`.
- `//*[string-length(name()) = 3]`: select any element with 3 letter character.
  - we can use other comparison here: `<`, `>`.
- `/foo/bar/descendant::*`: select all descendant of `/foo/bar`.
- `//foo/descendant::*`: select all elements which have `foo` among *its ancestors*.
- `//baz/parent::*`: select all parents of `baz` element.
- `/foo/bar/baz/ancestor::*`: select all acestor of `baz`.
- `/foo/bar/following-sibling::*`: select following sibling of `bar`.
- `/foo/bar/preceding-sibling::*`: select preceding sibling of `bar`.
- `/foo/bar/following::*`: select the axis after `bar`.
- `/foo/bar/preceding::*`: select the axis before `bar`.
- `/foo/bar/descendant-or-self::*`: select the context node and the descendant.
- `/foo/bar/ancestor-or-self::*`: select the context node and the ancestor.

Other interesting functions are:

- `//bar[normalize-space(@name)='b1']`: remove leading and trailing spaces before comparison
- `//*[starts-with(name(),'b')]`: select any element *starts* with b.
- `//*[contains(name(),'b')]`: select any element which *contain* c.
- `//bar[position() mod 2 = 0 ]`: select even `bar` elements.

The expression also can be combined using `|`:

- `//foo | //bar`: select all element matching both expression

📝 At this point you realize that using XPath is too verbose. Scrapy selectors
allow you to chain selectors, so most of the time you can just select by class
using CSS and then switch to XPath when needed.

Most of the time, we will be working with relative xpath.
Here are some tips:

- To get the `<p>` element inside `<div>`:

``` python
>>> divs = response.xpath('//div')
>>> for p in divs.xpath('.//p'):  # without the '.', it will get the `<p>` from whole document
    print(p.get())
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


Reference:

- [Official Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Zvon.org XPath 1.0 Tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html#intro)
- [Scrapy Selector Documentation](https://docs.scrapy.org/en/latest/topics/selectors.html)

[scrapy-tutorial]: https://docs.scrapy.org/en/latest/intro/tutorial.html
[css-extension]: https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors
