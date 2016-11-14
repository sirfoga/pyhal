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


""" Deal with webpages. """


import time
import random
import urllib.request
import webbrowser
import socks
import socket
import requests  # fetch source via tor
from bs4 import BeautifulSoup


CHROME_USER_AGENT = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14",
    "Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
]


class Webpage(object):
    """ representation of URL (web page)"""

    def __init__(self, url, using_tor=False):
        """
        :param url: string
            Url of webpage
        :param using_tor: bool
            Whether using tor or not to fetch source page
        """

        object.__init__(self)

        self.url = self.parse_url(url)
        self.domain = self.get_domain()
        self.using_tor = using_tor
        self.source = self.get_html_source(self.using_tor)
        self.soup = BeautifulSoup(self.source, "lxml")

    @staticmethod
    def parse_url(raw_url):
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

    def get_scheme(self):
        """
        :return: get scheme (HTTP, HTTPS, FTP ..) from given url
        """

        return urllib.request.urlparse(self.url).scheme

    def get_hostname(self):
        """
        :return: extract hostname from given url
        """

        return urllib.request.urlparse(self.url).hostname

    def get_domain(self):
        """
        :return: get domain from given url
        """

        return "{uri.scheme}://{uri.netloc}/".format(uri=urllib.request.urlparse(self.url))

    def allow_spider(self, spider):
        """
        :param spider: name of bot
        :return: look robots.txt for approval
        """

        domain = self.domain  # look for robots.txt in domain
        parser = urllib.request.robotparser.RobotFileParser()
        parser.set_url(domain + 'robots.txt')
        parser.read()

        return parser.can_fetch(spider, self.url)

    def get_html_source(self, tor=False):
        """
        :return: BeautifulSoup to parse
        """

        if tor:
            print("To be able to fetch HTML source pages via Tor the following command is required:")
            print("apt-get install tor && tor &")
            socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
            socket.socket = socks.socksocket
            r = requests.get(self.url).text
        else:
            q = urllib.request.Request(self.url)
            q.add_header("user-agent", random.choice(CHROME_USER_AGENT))
            r = urllib.request.urlopen(q).read()

        return str(r)

    def get_links(self, recall, timeout):
        """
        :param recall: max time to attempt to fetch url
        :param timeout: max time (s) to wait for web_page response
        :return: array of out_links
        """

        for attempt in range(recall):
            try:  # setting timeout
                soup = BeautifulSoup(self.source)  # parse source
                out_links = []

                for tag in soup.findAll(['a', 'link'], href=True):
                    tag['href'] = urllib.request.urlparse.urljoin(self.url, tag['href'])
                    out_links.append(tag['href'])

                return sorted(out_links)  # sort array
            except:
                time.sleep(timeout)  # time to wait for another attempt

    def open_in_browser(self, times):
        """
        :param times: int
            Times to open webpage in browser
        :return: void
            Open a wendrive and go to webpage
        """

        for t in range(times):
            webbrowser.open(self.url)
