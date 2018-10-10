# !/usr/bin/python
# coding: utf_8


"""Authenticate your Google APIs """

import os

import httplib2
from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class GoogleApiOAuth:
    """OAuth Google API"""

    def __init__(self, scope, app_name, app_secrets_path,
                 user_credentials_path):
        """
        :param scope: scope of api
        :param app_name: Name of app to display
        :param app_secrets_path: path to app secrets
        :param user_credentials_path: path to user credentials
        """
        self.scope = str(scope)
        self.app_name = str(app_name)
        self.app_secrets = str(app_secrets_path)
        self.user_credentials = str(user_credentials_path)
        self.store = Storage(user_credentials_path)

    def get_new_user_credentials(self):
        """Gets new credentials

        :returns: New user credentials file upon user prompt
        """
        # OAuth2.0 authorization flow
        flow = client.flow_from_clientsecrets(self.app_secrets, self.scope)
        flow.user_agent = self.app_name
        return tools.run_flow(flow, self.store)

    def get_user_credentials(self):
        """Gets new credentials

        :returns: User credentials created via OAuth
        """
        # create path to user credentials if needed
        if not os.path.exists(os.path.dirname(self.user_credentials)):
            os.makedirs(os.path.dirname(self.user_credentials))

        credentials = self.store.get()  # retrieve credentials
        needs_to_be_updated = not credentials or credentials.invalid
        if needs_to_be_updated:
            self.get_new_user_credentials()  # get new user credentials
            credentials = self.store.get()  # retrieve new credentials

        return credentials

    @staticmethod
    def authenticate(credentials):
        """Authenticates credentials

        :param credentials: authentication code created via OAuth
        :returns: Http authenticated credentials
        """
        http = httplib2.Http()
        credentials.authorize(http)
        return http

    def get_driver(self, name, version):
        """Authenticates and creates new API driver to perform scope stuff

        :param name: Name of driver
        :param version: Version of driver
        :returns: driver
        """
        user_credentials = self.get_user_credentials()  # get credentials
        return discovery.build(
            name, version,
            http=self.authenticate(user_credentials)
        )  # get new driver
