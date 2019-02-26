# -*- coding: utf-8 -*-
import os
import sqlite3
import re
import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiitaScrapyPipeline(object):
    _db = None
    MONTH_LIST = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,\
                  'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    @classmethod
    def get_database(cls):
        cls._db = sqlite3.connect(
            os.path.join(os.getcwd(), 'qiita_scrapy.db')
        )
        cursor = cls._db.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS post(\
            title text not null,\
            url text unique not null,\
            date DATE not null\
            );')
        return cls._db

    def process_item(self, item, spider):

        self.save_post(item)
        return item

    def save_post(self, item):
        if self.find_post(item['url']):
            return

        item['date'] = self.translate(item['date'])

        db = self.get_database()
        db.execute(
            'INSERT INTO post (title, url, date) VALUES (?, ?, ?)', (
                item['title'][0],
                item['url'],
                item['date']
            )
        )
        db.commit()

    def find_post(self, url):
        db = self.get_database()
        cursor  = db.execute(
            'SELECT * FROM post WHERE url=?',
            (url,)
        )
        return cursor.fetchone()

    def translate(self, date):
        m, d, y = re.findall(r"[a-zA-Z]{3}\s\d{2},\s\d{4}", date)[0].split(" ")
        m = self.MONTH_LIST[m]
        d = d.split(",")[0]
        return '{}-{}-{}'.format(y, m, d)
