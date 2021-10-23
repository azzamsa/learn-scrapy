# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotesPipeline:
    def __init__(self):
        self.connect()
        self.create_table()

    def connect(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS quotes")
        self.curr.execute("""CREATE TABLE quotes(text text,  author text, tag text)""")

    def process_item(self, item, spider):
        self.store(item)
        return item

    def store(self, item):
        self.curr.execute(
            """INSERT INTO quotes values (?,?,?)""",
            (
                item["text"],
                item["author"],
                item["tags"][0],
            ),
        )
        self.conn.commit()
