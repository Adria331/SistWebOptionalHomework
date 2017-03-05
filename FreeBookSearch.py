#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
@author Adrià Bonet Vidal
Daily free book of Packt notifier
'''

import urllib2
from bs4 import BeautifulSoup
import subprocess

class Client(object):

    def get_web(self, link):
        file = urllib2.urlopen(link)
        html = file.read()
        file.close()
        return html

    # Search the daily free book name of Packt free learning Website
    def search_book_name(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div", "dotd-title")
        bookName = elements[0].find_all("h2")[0].text.strip()
        return bookName

    # Shows a system message with the name of the book 
    #(You can use cron to show it when you want)
    def sendMessage(self, book):
    	subprocess.Popen(['notify-send', "The free book of the day is: " + book])

    def main(self):
        htmlWeb = self.get_web(
          'https://www.packtpub.com/packt/offers/free-learning/')
        freeBook = self.search_book_name(htmlWeb)

        print freeBook
        self.sendMessage(str(freeBook))


if __name__ == "__main__":
    clientWeb = Client()
clientWeb.main()