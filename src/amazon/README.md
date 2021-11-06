# Amazon Scraper

A scraper for [amazon.com](https://amazon.com).

## Lesson Learned

- CSS selector


## Getting Started

``` shell
$ # take a look at a previous projects

$ # start crawling
$ scrapy crawl amazon_spider -O amazon.json
```


## Logs

<details>
  <summary>amazon spider (with default user-agents)</summary>

```python
2021-11-06 13:53:52 [scrapy.extensions.feedexport] INFO: Stored json feed (48 items) in: amazon.json


2021-11-06 13:53:52 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 735,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 100450,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/301': 1,
 'elapsed_time_seconds': 3.058293,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2021, 11, 6, 6, 53, 52, 428490),
 'httpcompression/response_bytes': 710037,
 'httpcompression/response_count': 1,
 'item_scraped_count': 48,
 'log_count/DEBUG': 51,
 'log_count/INFO': 11,
 'memusage/max': 57421824,
 'memusage/startup': 57421824,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2021, 11, 6, 6, 53, 49, 370197)}
2021-11-06 13:53:52 [scrapy.core.engine] INFO: Spider closed (finished)
```

</details>

<details>
  <summary>amazon spider (with google bot user-agents)</summary>

```python
2021-11-06 14:11:22 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'amazon',
 'EDITOR': 'emacs',
 'NEWSPIDER_MODULE': 'amazon.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['amazon.spiders'],
 'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; '
               '+http://www.google.com/bot.html)'}

2021-11-06 14:11:25 [scrapy.extensions.feedexport] INFO: Stored json feed (48 items) in: amazon.json

2021-11-06 14:11:25 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 849,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 100087,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/301': 1,
 'elapsed_time_seconds': 2.922486,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2021, 11, 6, 7, 11, 25, 619503),
 'httpcompression/response_bytes': 708893,
 'httpcompression/response_count': 1,
 'item_scraped_count': 48,
 'log_count/DEBUG': 51,
 'log_count/INFO': 11,
 'memusage/max': 57565184,
 'memusage/startup': 57565184,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2021, 11, 6, 7, 11, 22, 697017)}
2021-11-06 14:11:25 [scrapy.core.engine] INFO: Spider closed (finished)
```

</details>
