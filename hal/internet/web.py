# -*- coding: utf-8 -*-

"""Deal with web-pages """

import random
import re
import time
import urllib.request
import webbrowser
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

USER_AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 ("
    "KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 ("
    "KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 ("
    "KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 ("
    "KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 ("
    "KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 ("
    "KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 ("
    "KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 ("
    "KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 ("
    "KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 ("
    "KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,"
    "like Gecko) Chrome/9.1.0.0 Safari/540.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 ("
    "KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14",
    "Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, "
    "like Gecko) Chrome/9.0.587.0 Safari/534.12",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 ("
    "KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 ("
    "KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 ("
    "KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) "
    "Chrome/14.0.792.0 Safari/535.1",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) "
    "Chrome/15.0.872.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, "
    "like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, "
    "like Gecko) Chrome/17.0.963.66 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 ("
    "KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, "
    "like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) "
    "Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, "
    "like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, "
    "like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/34.0.1847.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/37.0.2062.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 ("
    "KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/51.0.2704.103 Safari/537.36 "
]
URL_VALID_REGEX = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:" +
    r"(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)" +
    r"+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE
)
HEADERS = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept": "text/html,application/xhtml+xml,application/xml,"
              "application/pdf;q=0.9,*/*;q=0.8 "
}


def is_url(candidate):
    """Checks if string is url

    :param candidate: url to check for url
    :returns: True iff candidate is a valid url

    """
    return re.match(URL_VALID_REGEX, candidate)


class Webpage:
    """Representation of Web page at URL"""

    def __init__(self, url):
        """
        :param url: Url of webpage
        """
        self.url = self.parse_url(url)
        self.domain = self.get_domain()

        self.source = None
        self.soup = None

    @staticmethod
    def parse_url(url):
        """Parses correctly url

        :param url: url to parse
        """
        parsed = url

        if not url.startswith("http://") and not url.startswith(
                "https://"):  # if url is like www.yahoo.com
            parsed = "http://" + parsed
        elif url.startswith("https://"):
            parsed = parsed[8:]
            parsed = "http://" + parsed

        index_hash = parsed.rfind("#")  # remove trailing #
        index_slash = parsed.rfind("/")
        if index_hash > index_slash:
            parsed = parsed[0: index_hash]

        return parsed

    def get_scheme(self):
        """Gets scheme of url
        :returns: get scheme (HTTP, HTTPS, FTP ..) from given url
        """

        return urllib.request.urlparse(self.url).scheme

    def get_hostname(self):
        """Gets hostname of url
        :returns: extract hostname from given url
        """

        return urllib.request.urlparse(self.url).hostname

    def get_domain(self):
        """Gets domain of url
        :returns: get domain from given url
        """

        return "{uri.scheme}://{uri.netloc}/".format(
            uri=urllib.request.urlparse(self.url))

    def get_html_source(self):
        """Gets source page of url
        :returns: HTML source
        """
        req = urllib.request.Request(self.url)
        req.add_header("user-agent", random.choice(USER_AGENTS))
        req_text = urllib.request.urlopen(req).read()
        self.source = str(req_text)
        self.soup = BeautifulSoup(self.source, "lxml")
        return self.source

    def get_links(self, recall, timeout):
        """Gets links in page

        :param recall: max times to attempt to fetch url
        :param timeout: max times
        :returns: array of out_links
        """
        for _ in range(recall):
            try:  # setting timeout
                soup = BeautifulSoup(self.source)  # parse source
                out_links = []

                for tag in soup.findAll(["a", "link"], href=True):
                    tag["href"] = urljoin(self.url, tag["href"])
                    out_links.append(tag["href"])

                return sorted(out_links)  # sort array
            except:
                time.sleep(timeout)  # times to wait for another attempt

    def open_in_browser(self, n_times):
        """Opens page in browser

        :param n_times: Times to open page in browser
        """
        for _ in range(n_times):
            webbrowser.open(self.url)


def download_url(url, local_file):
    """Downloads link to local file

    :param url: Url to download
    :param local_file: Save url as this path
    """
    downloader = urllib.request.URLopener()
    downloader.retrieve(url, local_file)


def download_to_file(url, local_file, headers=HEADERS, cookies=None,
                     chunk_size=1024):
    """Download link to local file

    :param url: PDF url to download
    :param local_file: Save url as this path
    :param headers: Headers to fetch url (Default value = HEADERS)
    :param cookies: Cookies to fetch url (Default value = None)
    :param chunk_size: int (Default value = 1024)
    """
    if not cookies:
        cookies = {}

    req = requests.get(url, headers=headers, cookies=cookies, stream=True)
    with open(local_file, "wb") as local_download:
        for chunk in req.iter_content(chunk_size):
            if chunk:
                local_download.write(chunk)


def get_tor_session():
    """Finds TOR session

    :returns: TOR session
    """
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {
        "http": "socks5://127.0.0.1:9050",
        "https": "socks5://127.0.0.1:9050"
    }
    return session


def renew_connection(password):
    """Renews TOR session

    :param password: new password
    """
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)
