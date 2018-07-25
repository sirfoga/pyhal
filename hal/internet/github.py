# !/usr/bin/python3
# coding: utf-8

# Copyright 2016-2018 Stefano Fogarollo
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

GITHUB_URL = "https://github.com"
API_URL = "https://api.github.com/"  # Github api url


class GithubRawApi(object):
    """ Wrapper for generic Github API """

    _API_URL_TYPE = {
        k: API_URL + k
        for k in [
        "users", "repos", "orgs", "authorizations", "gists", "feeds",
        "search"
    ]
    }  # possible types of Github API

    def __init__(self, url=API_URL, get_api_content_now=False,
                 token=None):
        """
        :param url: str
            Url of API content to get
        :param get_api_content_now: bool
            True iff you want to get API content response when building object
        :param token: str
            Token to use for API call
        """

        object.__init__(self)

        self.api_url = url
        self.api_content = None
        self.token = token

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
        except:
            return None

    def _get_api_content(self):
        """
        :return: void
            Updates class api content by calling Github api and storing result
        """

        api_content_request = urllib.request.Request(self.api_url)
        if self.token is not None:
            api_content_request.add_header("User-Agent", "Github PyAPI")
            api_content_request.add_header(
                "Authorization", "token %s" % self.token
            )

        api_content_response = urllib.request.urlopen(
            api_content_request).read()
        self.api_content = json.loads(
            api_content_response.decode("utf-8"))  # parse response


class GithubApi(GithubRawApi):
    """ Wrapper for generic Github API """

    def __init__(self, api_type):
        """
        :param api_type: str
            Type of API to build
        """

        super(GithubApi, self).__init__(
            url=GithubRawApi._API_URL_TYPE[api_type],
            get_api_content_now=False
        )

    @staticmethod
    def get_trending_daily(lang=""):
        """
        :param lang: str
            Coding language
        :return: []
            List of GithubUserRepository
        """

        url = "https://github.com/trending/"
        url += str(lang).lower().replace(" ", "") + "?since=daily"
        api_content_request = urllib.request.Request(url)
        api_content_response = urllib.request.urlopen(
            api_content_request).read().decode("utf-8")  # parse response
        soup = BeautifulSoup(api_content_response, "lxml")  # html parser
        raw_repo_list = soup.find(
            "ol", {"class": "repo-list"}
        ).find_all("li")

        repos_list = []
        for repo in raw_repo_list:
            details = repo.find_all("div")[0].a.text.split("/")
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
        self.api_url += "/" + self.username

    def get_email(self):
        """
        :return: str
            Email of user
        """

        api_url = self.api_url + "/events/public"
        api_content = GithubRawApi(
            api_url,
            get_api_content_now=True
        ).api_content

        try:
            for event in api_content:
                if event["type"] == "PushEvent":
                    return event["payload"]["commits"][0]["author"]["email"]
        except:
            return None

    def get_repos(self):
        """
        :return: [] of GithubUserRepository
            List of user repositories
        """

        user_repos_url = self["repos_url"]
        api_driver = GithubRawApi(user_repos_url,
                                  True)  # driver to parse API content
        repos_list = []
        for repo in api_driver.api_content:  # list of raw repository
            repo_name = repo["name"]
            repos_list.append(GithubUserRepository(self.username, repo_name))
        return repos_list

    def get_starred_repos(self):
        """
        :return: [] of GithubUserRepository
            List of starred repositories
        """

        starred_url = self.api_url + "/starred"
        keep_finding = True  # False when there are no more stars to find
        current_page = 1
        repos_list = []
        while keep_finding:
            api_url = starred_url + "?page=" + str(
                current_page)  # request starred list url with page number
            api_driver = GithubRawApi(
                api_url,
                True
            )  # driver to parse API content
            for repo in api_driver:
                repo_username = repo["owner"]["login"]
                repo_name = repo["name"]
                repos_list.append(
                    GithubUserRepository(repo_username, repo_name))

            if len(api_driver.api_content) < 1:  # no more repo to find
                keep_finding = False
            current_page += 1  # increase page counter
        return repos_list

    def get_trending_daily_not_starred(self):
        """
        :return: []
            List of daily-trending repositories which are not starred by user
        """

        trending_daily = self.get_trending_daily()  # repos trending daily
        starred_repos = self.get_starred_repos()  # repos starred by user
        repos_list = []
        for repo in trending_daily:
            if repo not in starred_repos:
                repos_list.append(repo)
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
        self.api_url += "/" + self.username + "/" + self.repository_name

    def __eq__(self, other):
        return self.username == other.username \
               and self.repository_name == other.repository_name
