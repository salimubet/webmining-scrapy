import scrapy


class Anoboy2Spider(scrapy.Spider):
    name = 'anoboy2'
    allowed_domains = ['https://anoboy.stream/anime-list/']
    myBaseUrl = "https://anoboy.stream/anime-list/"
    start_urls=[]

   # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,100):
        start_urls.append(myBaseUrl+str(i))
 
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#ada')
 
            # Collecting product name
            product_name = data.css('.OnGoing')

            count = 0 
 
            # Combining the results
            for review in product_name:
                yield{'name': ''.join(product_name[count].xpath('.//text()').extract())                     }
                count = count + 1
    pass
