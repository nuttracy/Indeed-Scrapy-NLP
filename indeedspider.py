# -*- coding: utf-8 -*-
import scrapy
import urllib

#from indeed_scrapy.items import IndeedScrapyItem


QUERY = 'data+scientist'
LOCATION = '94102'
COUNT = 0

class IndeedspiderSpider(scrapy.Spider):
    name = "indeedspider"
    allowed_domains = ["indeed.com"]
    #print '********************************inclass'  
    
    def start_requests(self):
        last_page_number = 5
        start_urls = ('https://www.indeed.com/jobs?q='+QUERY + '&l=' + LOCATION)
        page_urls = [ start_urls+ "&start=" + str(pageNumber*10-10)
                     for pageNumber in range(1, last_page_number + 1)]    
            
        for url in page_urls:
            #print '********parse******************************'
            #print url
            yield scrapy.Request(url=url, callback=self.parse_listing_results_page)

    def parse_listing_results_page(self, response):
        #//a[contains(@data-tn-element,"jobTitle")]/@href
        print '*************parse_listing*****************'
        
        for href in response.xpath('//a[contains(@data-tn-element,"jobTitle")]/@href').extract():
            url = response.urljoin(href)
            print '******************************'
            print url
            global COUNT
            COUNT += 1
            filename = "OutFiles/Web_" + str(COUNT)+".txt"
            urllib.urlretrieve(url, filename)
            

