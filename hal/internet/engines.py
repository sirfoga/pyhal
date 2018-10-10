# -*- coding: utf-8 -*-

"""Abstract search engines """

from hal.internet.web import Webpage


class SearchEngineResult:
    """Result of general search engine"""

    def __init__(self, title, link, description=""):
        """
        :param title: title of result
        :param link: search query url
        :param description: description of result
        """
        self.title = title
        self.link = link
        self.description = description

    def __str__(self):
        return self.title


class SearchEngine:
    """Internet general search engine"""

    def __init__(self, url, blank_replace="+"):
        """
        :param url: string
            Url of search engine used in all query.
        :param blank_replace:
            Every search engine has to replace blanks in query
        """
        self.url = str(url)
        self.web_page = Webpage(self.url)
        self.domain = self.web_page.get_domain()
        self.blank_replace = blank_replace

    def parse_query(self, query):
        """Parses given query in order to meet search criteria of search engine

        :param query: Query to search engine
        :returns: query of search engine (well-formatted)
        """
        return query.strip().replace(
            " ",
            self.blank_replace
        ).lower()  # remove trailing blanks, replace with search engine blanks

    def get_search_page(self, query):
        """Gets HTML source

        :param query: query to search engine
        :returns: HTML source of search page of given query
        """
        query_web_page = Webpage(self.url + self.parse_query(query))
        query_web_page.get_html_source()  # get html source
        return query_web_page.source
