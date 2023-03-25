import re

import scrapy

from pep_parse.items import PepParseItem

SEARCH_PATTERN = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'
URL_NAME = 'peps.python.org'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [URL_NAME]
    start_urls = [f'https://{url}/' for url in allowed_domains]

    def parse(self, response):
        for section_link in response.css(
            '#numerical-index tr a[href]'
        ):
            yield response.follow(section_link, callback=self.parse_pep)

    def parse_pep(self, response):
        header = response.css('h1.page-title::text').get()
        number, name = re.search(SEARCH_PATTERN, header).groups()
        yield PepParseItem(dict(
            number=number,
            name=name,
            status=response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get()
        ))
