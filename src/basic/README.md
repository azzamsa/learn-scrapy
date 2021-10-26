# Basic Scraper

This is the simplest working example of a Scrapy scraper.

## Getting Started

``` shell
$ # activate the virtualenv
$ vf activate global3 # in this case I am using virtualfish

# install dependencies
$ pip install -r requirements.txt

$ # start crawling
$ scrapy runspider quotes.py -O quotes.json
```

The `quotes.json` will contain exactly 100 quotes. Otherwise, it doesn't work properly.

## Logs

Instead of putting the output into git, compare your log output to the log below.
To see if yours are correct.

Some important lines are:
- `Stored json feed (100 items)`. Check whether your crawled items are the same.
- `request_method_count/GET`.

 <details>
  <summary>quotes.py</summary>
  
  ```python
2021-10-26 07:03:32 [scrapy.extensions.feedexport] INFO: Stored json feed (100 items) in: quotes.json
2021-10-26 07:03:32 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 2652,
 'downloader/request_count': 10,
 'downloader/request_method_count/GET': 10,
 'downloader/response_bytes': 23065,
 'downloader/response_count': 10,
 'downloader/response_status_count/200': 10,
 'elapsed_time_seconds': 5.565168,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2021, 10, 26, 0, 3, 32, 194542),
 'httpcompression/response_bytes': 108561,
 'httpcompression/response_count': 10,
 'item_scraped_count': 100,
 'log_count/DEBUG': 110,
 'log_count/INFO': 11,
 'request_depth_max': 9,
 'response_received_count': 10,
 ```
  
</details> 
