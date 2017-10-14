#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json
import scrapy
from scrapy import Selector

class CurrencySpider(scrapy.Spider):

    name = "forex"
    start_urls = ['http://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html']

    def parse(self, response):
        markets = response.xpath('//tbody/tr')
        for market in markets:
            symbol = market.xpath('td[@class="currency"]/a/text()').extract_first()
            price = market.xpath('td[@class="spot number"]/a/span/text()').extract_first()
            yield { 'symbol': symbol, 'price': price }
