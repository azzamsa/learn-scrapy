import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # must be unique

    start_urls = [
        "https://quotes.toscrape.com/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            # `foo.bar` the dot operator to access the class
            # `::text` to extract the text only
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                # `div.tags`, `tags` is a class
                # `a.tag`, `tag` is a class
                # a space denotes a children element
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            # for learning purpose, 3 page is enough
            page_number = next_page.split("/")[2]
            print(page_number)
            if int(page_number) < 3:
                yield response.follow(next_page, callback=self.parse)
