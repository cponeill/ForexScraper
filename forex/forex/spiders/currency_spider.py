#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# This is the easiest way to scrape for current currency prices.

import json
import scrapy
from scrapy import Selector

class CurrencySpider(scrapy.Spider):
    """
    Scrape the ECB website for current currency prices.

    Input: ECB website URL.
    Ouput: Symbol & Price information in JSON format.
    """
    name = "forex"
    start_urls = ['http://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html']

    def parse(self, response):
        # set overall xpath value to markets
        markets = response.xpath('//tbody/tr')

        # loop through markets variable, set each path for symbol and price, and output json.
        for market in markets:
            symbol = market.xpath('td[@class="currency"]/a/text()').extract_first()
            price = market.xpath('td[@class="spot number"]/a/span/text()').extract_first()
            yield { 'symbol': symbol, 'price': price }
