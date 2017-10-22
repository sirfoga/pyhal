# !/usr/bin/python
# coding: utf_8

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


""" Use GMail APIs from python """

import os
from email.mime.text import MIMEText

from hal.internet.google.gauthenticator import GoogleApiOAuth


class GMailApiOAuth(GoogleApiOAuth):
    def __init__(self, app_name, client_secrets_file, oauth_path):
        """
        :param app_name: str
            Name of app to display
        :param client_secrets_file: str
            Path to client_secret.json file
        :param oauth_path: str
            Path to gmail.json file
        """

        GoogleApiOAuth.__init__(
            self,
            "https://www.googleapis.com/auth/gmail.send",  # scope
            app_name,
            os.path.join(client_secrets_file),  # app secrets
            os.path.join(oauth_path),  # user credential
        )

    def create_driver(self):
        """
        :return: driver
            GMail API driver
        """

        return super().get_driver("gmail", "v1")


def get_mime_message(subject, text):
    """
    :param subject: str
        Subject of email
    :param text: str
        Email content
    :return: MIMEText
        Email formatted as HTML ready to be sent
    """

    message = MIMEText(
        "<html>" +
        str(text).replace("\n", "<br>") +
        "</html>", "html"
    )
    message["subject"] = str(subject)
    return message


def send_email(sender, msg, driver):
    """
    :param sender: str
        Sender of email
    :param msg: str
        Message to send to me
    :param driver: GMailApiOAuth driver
        GMail authenticator
    :return: void
        Sends email to me with this message
    """

    driver.users().messages().send(
        userId=sender,
        body=msg
    ).execute()  # send message
