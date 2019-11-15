import scrapy
from ..items import MobiledataItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = [
		'https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=mobiles%7Cin+Mobiles&requestId=49b8f2e3-5bff-4062-bd79-a72772089766&as-searchtext=phones',
	]

	def parse(self, response):
		items = MobiledataItem()
		All_div_phones = response.css('._1UoZlX')
		for phones in All_div_phones:
			names = phones.css('._3wU53n::text').extract()
			specs = phones.css('.tVe95H::text').extract()
			price = phones.css('._2rQ-NK::text').extract()
			name1 = names[0].split('(')
			name = name1[0]
			
			items['Name'] = name
			items['Price'] = price
			items['Specifications'] = specs
			yield items