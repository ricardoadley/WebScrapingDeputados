import scrapy


class DeputadosSpider(scrapy.Spider):
    name = "deputados"

    def start_requests(self):
        urls = [
            'https://www.camara.leg.br/deputados/204507'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'zambeli.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')