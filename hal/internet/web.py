# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" deal with webpages """

import robotparser
import time
import urllib2
import urlparse
import webbrowser

from BeautifulSoup import BeautifulSoup
from selenium import webdriver


class Webpage(object):
    """ representation of URL (web page)
    """

    def __init__(self, raw_url):
        object.__init__(self)

        self.url = self.parse_url(raw_url)
        self.get_domain()
        self.source = ""
        self.links = ""

    def run(self):
        """
        :return: get html source, links..
        """

        try:
            self.get_html_source()
        except:
            raise ValueError("Cannot get HTML source of \"" + self.url + "\"")

        try:
            self.get_links(1, 1000)  # default recall and timeout
        except:
            raise ValueError("Cannot get URL links inside of \"" + self.url + "\"")

    def parse_url(self, raw_url):
        """
        :param raw_url: url to parse
        :return: parses correctly url
        """

        parsed = raw_url

        if not raw_url.startswith('http://') and not raw_url.startswith('https://'):  # if url is like www.yahoo.com
            parsed = 'http://' + parsed
        elif raw_url.startswith('https://'):
            parsed = parsed[8:]
            parsed = 'http://' + parsed

        index_hash = parsed.rfind('#')  # remove trailing #
        index_slash = parsed.rfind('/')
        if index_hash > index_slash:
            parsed = parsed[0: index_hash]

        return parsed

    def get_domain(self):
        """
        :return: extract domain from given url
        """

        parsed_url = urlparse.urlparse(self.url)
        self.domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)

    def allow_spider(self, spider):
        """
        :param spider: name of bot
        :return: look robots.txt for approval
        """

        domain = self.domain  # look for robots.txt in domain
        parser = robotparser.RobotFileParser()
        parser.set_url(domain + 'robots.txt')
        parser.read()

        return parser.can_fetch(spider, self.url)

    def get_html_source(self, tor=False):
        """
        :return: BeautifulSoup to parse
        """

        if tor:
            self.source = open_tor(self.url, 1)  # 1 time only
        else:
            try:
                req = urllib2.Request(self.url)
                req.add_header('User-Agent', 'I am a human')
                response = urllib2.urlopen(req)
                self.source = response.read()
            except:
                raise ValueError('error while parsing ' + self.url)

    def get_links(self, recall, timeout):
        """
        :param recall: max time to attempt to fetch url
        :param timeout: max time (s) to wait for web_page response
        :return: array of out_links
        """

        for attempt in xrange(0, recall):
            try:  # setting timeout
                soup = BeautifulSoup(self.source)  # parse source
                out_links = []

                for tag in soup.findAll(['a', 'link'], href=True):
                    tag['href'] = urlparse.urljoin(self.url, tag['href'])
                    out_links.append(tag['href'])

                self.links = sorted(out_links)  # sort array
            except:
                time.sleep(timeout)  # time to wait for another attempt


def open_browser(url, times):
    """
    :param url: url to open
    :param times: how many times
    :return: open given url
    """

    if times >= 0:
        for travel in range(0, times):
            webbrowser.open(url)
    else:
        raise ValueError('\'times\' field cannot be negative')


def open_tor(url, times):
    """
    :param url: url to open (inside TOR network)
    :param times: how many times
    :return: open given url with tor browser (anonymously): Tor browser must be running
    """

    if times >= 0:
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks','127.0.0.1')
        profile.set_preference('network.proxy.socks_port', 9150)

        browser = webdriver.Firefox(profile)
        source = ""
        for travel in range(0, times):
            browser.get(url)
            source = browser.page_source

        return source
    else:
        raise ValueError('\'times\' field cannot be negative')
