import scrapy


class TelegramSpiderSpider(scrapy.Spider):
    name = 'telegram_spider'
    start_urls = []

    for index in range(1, 25):
        start_urls.append('https://www.beautyhaulofficial.com/product/detail/soothing-moisture-aloe-vera-92-soothing-gel-300ml/r/' + str(index))

    def parse(self, response):
        
        for review in response.xpath('//div[@class="review-item"]'):

            yield {
                'name' : review.css('.name::text').get(),
                'date' : review.css('.date::text').get(),
                'comment' : review.css('.text::text').get(),
                'rating' : len(review.css('span.a'))
            }


        # filename = 'review.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
