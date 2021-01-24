import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        
        for country in countries:
            name = country.xpath(".//td[1]/a/text()").get()
            gdp_debt = country.xpath(".//td[2]/text()").get()
            population = country.xpath(".//td[3]/text()").get()

            yield {
                "name": name,
                "gdp_debt": gdp_debt,
                "population": population
            }
