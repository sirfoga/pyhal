# !/usr/bin/python3
# coding: utf-8


""" Common classes and entities in Github """

import json

import requests
from bs4 import BeautifulSoup

from internet.utils import add_params_to_url

GITHUB_URL = "https://github.com"
API_URL = "https://api.github.com/"  # Github api url
GITHUB_TOKEN = None
GITHUB_REMOTE = "https://{}:x-oauth-basic@github.com/"


def get_token():
    return GITHUB_TOKEN


def get_clone_url(remote_shortcut, token):
    """
    :param remote_shortcut: str
        Remote relative path of repository to clone
    :param token: str
        Github OAUTH token
    :return: str
        Url to clone
    """

    return GITHUB_REMOTE.format(token) + remote_shortcut


class GithubRawApi(object):
    """ Wrapper for generic Github API """

    _API_URL_TYPE = {
        k: API_URL + k
        for k in [
        "users", "repos", "orgs", "authorizations", "gists", "feeds",
        "search"
    ]
    }  # possible types of Github API

    def __init__(self, url=API_URL, url_params=None,
                 get_api_content_now=False):
        """
        :param url: str
            Url of API content to get
        :param get_api_content_now: bool
            True iff you want to get API content response when building object
        """

        object.__init__(self)

        self.api_url = url
        self.api_content = None

        if url_params:
            self.add_params_to_url(url_params)

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

        if GITHUB_TOKEN is not None:
            self.add_params_to_url({
                "access_token": GITHUB_TOKEN
            })

        api_content_response = requests.get(self.api_url)
        self.api_content = json.loads(
            api_content_response.text
        )  # parse response

    def add_params_to_url(self, params):
        """
        :param params: {}
            List of params to add to url
        :return: void
            Adds params to url
        """

        self.api_url = add_params_to_url(self.api_url, params)


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

    @staticmethod
    def _get_repos(url):
        """
        :return: [] of GithubUserRepository
            List of repositories in given url
        """

        current_page = 1
        there_is_something_left = True
        repos_list = []

        while there_is_something_left:
            api_driver = GithubRawApi(
                url,
                url_params={"page": current_page},
                get_api_content_now=True
            )  # driver to parse API content

            for repo in api_driver.api_content:  # list of raw repository
                repo_name = repo["name"]
                repo_user = repo["owner"]["login"]
                repos_list.append(
                    GithubUserRepository(repo_user, repo_name))

            there_is_something_left = len(api_driver.api_content) > 0
            current_page += 1

        return repos_list

    def get_repos(self):
        """
        :return: [] of GithubUserRepository
            List of public user repositories
        """

        url = self["repos_url"]
        return self._get_repos(url)

    def get_all_repos(self):
        """
        :return: [] of GithubUserRepository
            List of all user repositories (public, orgs and private)
        """

        url = "https://api.github.com/user/repos"
        params = {
            "access_token": GITHUB_TOKEN
        }  # add auth params
        url = add_params_to_url(url, params)
        return self._get_repos(url)

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
