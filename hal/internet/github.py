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


""" Common classes and entities in Github """

import json
import urllib.request

from bs4 import BeautifulSoup

GITHUB_URL_BASE = "https://github.com"
API_TOKEN_FILE = "api_token"
API_TOKEN = open(API_TOKEN_FILE).read().strip()


class GithubRawApi(object):
    """ Wrapper for generic Github API """

    _API_URL_BASE = "https://api.github.com/"  # Github api url

    def __init__(self, url=_API_URL_BASE, get_api_content_now=False):
        """
        :param url: str
            Url of API content to get
        :param get_api_content_now: bool
            True iff you want to get API content response when building object
        """

        object.__init__(self)

        self.api_url = url
        self.api_content = None

        if get_api_content_now:
            self._get_api_content()

    def __getitem__(self, key):
        """
        :param key: str
            Dictionary key to find specific user field
        :return: str
            Dictionary value of given key
        """

        if self.api_content is None:  # update API content
            self._get_api_content()

        try:
            return self.api_content[key]
        except Exception as e:
            print(str(e))
            return None

    def _get_api_content(self):
        """
        :return: void
            Updates class api content by calling Github api and storing result
        """

        api_content_request = urllib.request.Request(self.api_url)
        api_content_request.add_header("Authorization", "token %s" % API_TOKEN)
        api_content_request.add_header("User-Agent", "Github PyAPI")
        api_content_response = urllib.request.urlopen(api_content_request).read()
        self.api_content = json.loads(api_content_response.decode("utf-8"))  # parse response


class GithubApi(GithubRawApi):
    """ Wrapper for generic Github API """

    _API_URL_TYPE = {
        "users": GithubRawApi._API_URL_BASE + "users/",
        "repos": GithubRawApi._API_URL_BASE + "repos/",
        "orgs": GithubRawApi._API_URL_BASE + "orgs/",
        "authorizations": GithubRawApi._API_URL_BASE + "authorizations/",
        "gists": GithubRawApi._API_URL_BASE + "gists/",
        "feeds": GithubRawApi._API_URL_BASE + "feeds/",
        "search": GithubRawApi._API_URL_BASE + "search/"
    }  # possible types of Github API

    def __init__(self, api_type):
        """
        :param api_type: str
            Type of API to build
        """

        super(GithubApi, self).__init__(GithubApi._API_URL_TYPE[api_type])

    @staticmethod
    def get_trending_daily():
        """
        :return: []
            List of GithubUserRepository
        """

        url = "https://github.com/trending?since=daily"
        api_content_request = urllib.request.Request(url)
        api_content_response = urllib.request.urlopen(api_content_request).read().decode("utf-8")  # parse response
        soup = BeautifulSoup(api_content_response, "lxml")  # html parser
        raw_repo_list = soup.find_all("ol", {"class": "repo-list"})[0].find_all("li")
        repos_list = []
        for r in raw_repo_list:
            details = r.find_all("div")[0].a.text.split("/")
            repo_owner = details[0].strip()
            repo_name = details[1].strip()
            repos_list.append(GithubUserRepository(repo_owner, repo_name))
        return repos_list


class GithubUser(GithubApi):
    """ Model of a generic Github user profile """

    def __init__(self, username):
        """
        :param username: str
            Username of user
        """

        super(GithubUser, self).__init__("users")

        self.username = str(username)
        self.api_url += self.username

    def get_repos(self):
        """
        :return: []
            List of GithubUserRepository
        """

        user_repos_url = self["repos_url"]
        api_driver = GithubRawApi(user_repos_url, True)  # driver to parse API content
        repos_list = []
        for r in api_driver.api_content:  # list of raw repository
            repo_name = r["name"]
            repos_list.append(GithubUserRepository(self.username, repo_name))
        return repos_list

    def get_starred_repos(self):
        """
        :return: []
            List of GithubUserRepository
        """

        starred_url = self.api_url + "/starred"
        keep_finding = True  # False when there are no more stars to find
        current_page = 1
        repos_list = []
        while keep_finding:
            api_url = starred_url + "?page=" + str(current_page)  # request starred list url with exact page number
            api_driver = GithubRawApi(api_url, True)  # driver to parse API content
            for s in api_driver.api_content:
                repo_username = s["owner"]["login"]
                repo_name = s["name"]
                repos_list.append(GithubUserRepository(repo_username, repo_name))

            if len(api_driver.api_content) < 1:  # no more repo to find
                keep_finding = False
            current_page += 1  # increase page counter
        return repos_list

    def get_trending_daily_not_starred(self):
        trending_daily = self.get_trending_daily()  # list of repos trending daily
        starred_repos = self.get_starred_repos()  # list of repos starred by user
        repos_list = []
        for r in trending_daily:
            if r not in starred_repos:
                repos_list.append(r)
        return repos_list


class GithubUserRepository(GithubApi):
    """ Model of a generic Github user repository """

    def __init__(self, username, repository_name):
        """
        :param username: str
            Username of user
        :param repository_name: str
            Name of repository
        """

        super(GithubUserRepository, self).__init__("repos")

        self.username = str(username)
        self.repository_name = str(repository_name)
        self.api_url += self.username + "/" + self.repository_name

    def __eq__(self, other):
        return self.username == other.username and self.repository_name == other.repository_name
