import scrapy


class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['jawapos.com']
    start_urls = ['https://www.jawapos.com/berita-hari-ini/']

    def parse(self, response):
        data = response.css('.post-list__container')
 
        # Collecting title
        title = data.css('.post-list__title')

        # Collecting price
        cat = data.css('.post-list__cat')     
        c=0

        time = data.css('.post-list__time')

        # Combining the results
        for review in title:
            yield{'title': ''.join(review.xpath('.//text()').extract()),
                  'cat': ''.join(cat[c].xpath(".//text()").extract()),
                  'time': ''.join(time[c].xpath("./text()").extract())
                     }
            c=c+1
