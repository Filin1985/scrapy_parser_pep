import re

import scrapy

from pep_parse.items import PepParseItem

SEARCH_PATTERN = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for section_link in response.css(
            '#numerical-index tr a[href]'
        ):
            try:
                yield response.follow(section_link, callback=self.parse_pep)
            except AttributeError:
                continue

    def parse_pep(self, response):
        header = response.css('h1.page-title::text').get()
        number, name = re.search(SEARCH_PATTERN, header).groups()
        data = {
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get()
        }
        yield PepParseItem(data)
