import scrapy
from scrapy import Selector, Request
from ..items import dangdangbook


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["category.dangdang.com/"]
    start_urls = ["http://category.dangdang.com/cp01.47.03.00.00.00.html"]

    def parse(self, response):
        sel = Selector(response)
        listitems = sel.css('#search_nature_rg >ul >li')
        for listitem in listitems:
            book = dangdangbook()
            book['title'] = listitem.css('p.name > a::attr(title)').extract_first()
            book['price'] = listitem.css('p.price > span.search_now_price::text').extract_first()
            book['discribe'] = listitem.css('p.detail::text').extract_first()
            book['author'] = listitem.css('p.search_book_author > span:nth-child(1) > a:nth-child(1)::attr(title)').extract_first()
            yield book

        href_list = sel.css('#12810 > div:nth-child(3) > div.con.paginating.clearfix > div > ul > li > a::attr(href)')
        for href in href_list:
            url = response.urljoin(href.extract())
            print(url)
            yield Request(url=url)
