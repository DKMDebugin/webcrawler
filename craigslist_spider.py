import scrapy, requests, json
from py_w3c.validators.html.validator import HTMLValidator

class CraigsListSpider(scrapy.Spider):
    name = 'CraigsListSpider'
    allowed_domains = ['https://losangeles.craigslist.org/']

    def start_requests(self):
      return [
        scrapy.Request('https://losangeles.craigslist.org/')
        ]

    def parse(self, response):
      with open("page.html", "a") as f:
          f.write(response.text)

      vld = HTMLValidator()
      vld.validate_file("page.html")

      with open("validatePage.json", "a") as f:
          f.write(f"{json.dumps(vld.errors, indent=4)}")
