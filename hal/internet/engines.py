# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
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


""" Abstract search engines. """


from hal.internet.web import Webpage


class SearchEngineResult(object):
    def __init__(self, title, link, description=""):
        object.__init__(self)

        self.title = title
        self.link = link
        self.description = description

    def __str__(self):
        return self.title


class SearchEngine(object):
    def __init__(self, url, blank_replace="+"):
        """
        :param url: string
            Url of search engine used in all query.
        :param blank_replace:
            Every search engine has to replace blanks in query
        """
        object.__init__(self)

        self.url = str(url)
        self.web_page = Webpage(self.url)
        self.domain = self.web_page.get_domain()
        self.blank_replace = blank_replace

    def parse_query(self, query):
        """
        :param query: string
            Query to search engine.
        :return: string
            Parse given query in order to meet search criteria of search engine.
        """

        return query.strip().replace(" ", self.blank_replace).lower()  # remove trailing blanks, then replace with search engine blanks

    def get_search_page(self, query, using_tor=False):
        """
        :param query: string
            Query to search engine.
        :param using_tor: bool
            Whether use tor or not to fetch web pages
        :return: string
            Get HTML source of search page of given query.
        """

        query_web_page = Webpage(self.url + self.parse_query(query), using_tor=using_tor)
        query_web_page.get_html_source(tor=using_tor)  # get html source
        return query_web_page.source
