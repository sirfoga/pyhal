# !/usr/bin/python
# coding: utf_8


""" Authenticate your Google APIs """

import os

import httplib2
from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class GoogleApiOAuth(object):
    def __init__(self, scope, app_name, app_secrets_path,
                 user_credentials_path):
        """
        :param scope: string
            scope of api
        :param app_name: str
            Name of app to display
        :param app_secrets_path: string
            path to app secrets
        :param user_credentials_path: string
            path to user credentials
        """

        object.__init__(self)

        self.scope = str(scope)
        self.app_name = str(app_name)
        self.app_secrets = str(app_secrets_path)
        self.user_credentials = str(user_credentials_path)
        self.store = Storage(user_credentials_path)

    def get_new_user_credentials(self):
        """
        :return: credentials
            New user credentials file upon user prompt
        """

        flow = client.flow_from_clientsecrets(self.app_secrets,
                                              self.scope)  # perform OAuth2.0 authorization flow.
        flow.user_agent = self.app_name
        return tools.run_flow(flow, self.store)

    def get_user_credentials(self):
        """
        :return: string
            User credentials created via OAuth
        """

        if not os.path.exists(os.path.dirname(
                self.user_credentials)):  # create path to user credentials if needed
            os.makedirs(os.path.dirname(self.user_credentials))

        credentials = self.store.get()  # retrieve credentials
        if not credentials or credentials.invalid:  # user credentials are to be updated
            self.get_new_user_credentials()  # get new user credentials
            credentials = self.store.get()  # retrieve new credentials

        return credentials

    @staticmethod
    def authenticate(credentials):
        """
        :param credentials: string
            User authentication code created via OAuth
        :return: http
            Http authenticated credentials
        """

        http = httplib2.Http()
        credentials.authorize(http)
        return http

    def get_driver(self, name, version):
        """
        :param name: string
            Name of driver
        :param version: string
            Version of driver
        :return: api driver
            Authenticates and creates new API driver to perform scope stuff
        """

        user_credentials = self.get_user_credentials()  # get credentials
        return discovery.build(name, version, http=self.authenticate(
            user_credentials))  # get sheets driver
