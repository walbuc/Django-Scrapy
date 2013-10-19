#!/usr/bin/env python
# import django env
from django.core.management import setup_environ
import settings
setup_environ(settings)

# import scrapy stuff
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from scrapy.selector import HtmlXPathSelector

import logging, os
import logging.handlers

ROOT_PATH = os.path.dirname(__file__)

from scrapy.conf import settings
settings.overrides['LOG_FILE']=os.path.join(ROOT_PATH, 'log', 'scrapy.log')

logger = logging.getLogger('rstone')

from top.tasks import addAlbum,addArtist

class RstoneTopSpider(CrawlSpider):
    name='rstonetop500'
    allowed_domains = ["www.rollingstone.com"]
    start_urls=[
        'http://www.rollingstone.com/music/lists/500-greatest-albums-of-all-time-20120531',
        'http://www.rollingstone.com/music/lists/100-best-albums-of-the-2000s-20110718',
        'http://www.rollingstone.com/music/lists/100-greatest-guitarists-20111123',
        'http://www.rollingstone.com/music/lists/100-greatest-singers-of-all-time-19691231',
    ]
    rules = (
      Rule(SgmlLinkExtractor(allow='/music/lists/500-greatest-albums-of-all-time-20120531/[0-9a-zA-Z\-]+$'), 'fifth_hungred_greatest_albums', follow=True),
      Rule(SgmlLinkExtractor(allow='/music/lists/100-best-albums-of-the-2000s-20110718/[0-9a-zA-Z\-]+$'), 'hungred_best_albums_of_the_2000', follow=True),
      Rule(SgmlLinkExtractor(allow='/music/lists/100-greatest-guitarists-20111123/[0-9a-zA-Z\-]+$'), 'hungred_greatest_guitarrist', follow=True),
      Rule(SgmlLinkExtractor(allow='/music/lists/100-greatest-singers-of-all-time-19691231/[0-9a-zA-Z\-]+$'), 'hungred_greatest_singers', follow=True),
    )
    def hungred_best_albums_of_the_2000(self,response):
        
        a={
           'ranking':'100 best albums of the 2000s',
        }
        self.common_albums(response,a)
    
    def fifth_hungred_greatest_albums(self,response):
        a={
           'ranking':'500 Greatest Albums of All Time',
        }
        self.common_albums(response,a)
    
    def common_albums(self,response,a):
        x=HtmlXPathSelector(response)
        a['url']=response.url
        a['position']=x.select("//div[@class='listItemDescriptonDiv']/span[@class='ListItemNumber']/text()").extract()[0]
        at=x.select("//div[@class='listItemDescriptonDiv']/h3/text()").extract()[0]
        at=at.split(',')
        at=[i.strip() for i in at]
        at=[i.strip('\'') for i in at]
        a['title']=at[1]
        a['artist']=at[0]
        a['cover']=x.select("//div[@class='listPageContentImage assetContainer imageStandard']/img/@src").extract()[0]
        addAlbum.delay(a)
    
    def hungred_greatest_guitarrist(self,response):
        a={
            'ranking':'100 Greatest Guitarrist of All Time',
            'role':'guitarrist',
        }
        self.common_artist(response,a)
    
    def hungred_greatest_singers(self,response):
        a={
            'ranking':'100 Greatest Singers of All Time',
            'role':'singer',
        }
        self.common_artist(response,a)
    
    def common_artist(self,response,a):
        x=HtmlXPathSelector(response)
        a['url']=response.url
        a['position']=x.select("//div[@class='listItemDescriptonDiv']/span[@class='ListItemNumber']/text()").extract()[0]
        a['artist']=x.select("//div[@class='listItemDescriptonDiv']/h3/text()").extract()[0]
        addArtist.delay(a)