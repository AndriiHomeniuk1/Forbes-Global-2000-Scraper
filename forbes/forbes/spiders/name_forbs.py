import scrapy
from scrapy.http import Response


class NameForbsSpider(scrapy.Spider):
    name = "name_forbs"
    allowed_domains = ["forbes.com"]
    start_urls = ["https://www.forbes.com/lists/global2000/?sh=27736c1f5ac0"]

    def parse(self, response: Response, **kwargs):
        for pagination in response.css(".table-row-group"):
            for company in pagination.css(".table-row"):
                yield {
                    "rank": company.css(".rank::text").get(),
                    "name": company.css(".organizationName::text").get(),
                    "url_name": company.css(".table-row::attr(href)").get()
                }
