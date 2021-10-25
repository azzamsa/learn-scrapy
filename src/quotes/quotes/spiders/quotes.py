import scrapy

from ..items import QoutesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # must be unique

    start_urls = [
        "https://quotes.toscrape.com/",
    ]

    def parse(self, response):
        item = QoutesItem()

        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()

            item["text"] = text
            item["author"] = author
            item["tags"] = tags

            author_page = quote.css(".author + a ::attr(href)").get()
            yield scrapy.Request(
                f"https://quotes.toscrape.com{author_page}",
                callback=self.parse_author,
                cb_kwargs={"item": item},
            )

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            # for learning purpose, 3 page is enough
            page_number = next_page.split("/")[2]
            self.logger.info(f"Current page: {page_number}")
            if int(page_number) < 3:
                yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response, item):
        date = response.css(".author-born-date::text").get()
        location = response.css(".author-born-location::text").get()
        location = location[3:]  # strip `in`

        item["date"] = date
        item["location"] = location

        return item
