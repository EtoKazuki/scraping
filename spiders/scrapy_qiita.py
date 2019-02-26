# -*- coding: utf-8 -*-
import scrapy
from ..items import Post

class ScrapyQiitaSpider(scrapy.Spider):
    name = 'scrapy_qiita'
    allowed_domains = ['qiita.com']
    start_urls = ['https://qiita.com/search?q=python']
    PAGE_COUNT = 0

    def parse(self, response):
        for post in response.css('.searchResult'):
            yield Post(
            # emタグがあるとうまく文字列を取得できないから下の書き方. string()を使う
                title=post.css('h1').xpath('string()').extract(),
                url=post.css('.searchResult_itemTitle a::attr(href)').extract_first().strip(),
                date = post.css('.searchResult_header::text').extract_first()
            )

        older_post_link = response.css('.js-next-page-link::attr(href)').extract_first()
        if older_post_link is None or self.PAGE_COUNT == 10:
            return

        self.PAGE_COUNT += 1

        older_post_link = response.urljoin(older_post_link)
        yield scrapy.Request(older_post_link, callback=self.parse)
