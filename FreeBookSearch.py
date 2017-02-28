#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
@author Adrià Bonet Vidal
Free book name searcher
'''

import urllib2
from bs4 import BeautifulSoup
  
class Client(object):

    def get_web(self, link):
        file = urllib2.urlopen(link)
        html = file.read()
        file.close()
        return html

    # Search the daily free book name
    def search_book_name(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div", "dotd-title")

        tmp = []
        resultat = []
        for element in elements:
            tmp.append(str(element))
        for element in str(tmp).split('\\t'):
            resultat.append(element)
            if self.identifyElement(element) and element != "":
                return element

    def main(self):
        htmlWeb = self.get_web(
          'https://www.packtpub.com/packt/offers/free-learning/')
        freeBook = self.search_book_name(htmlWeb)
        print freeBook

    # Look if element is a tag
    def identifyElement(self, element):
        return '[' not in element and '<' not in element \
                and '>' not in element and ']' not in element

if __name__ == "__main__":
    clientWeb = Client()
    clientWeb.main()
