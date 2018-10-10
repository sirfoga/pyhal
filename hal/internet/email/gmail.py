# !/usr/bin/python
# coding: utf_8


"""Use GMail APIs from python """

import os
from email.mime.text import MIMEText

from hal.internet.services.google.gauthenticator import GoogleApiOAuth


class GMailApiOAuth(GoogleApiOAuth):
    def __init__(self, app_name, client_secrets_file, oauth_path):
        """
        :param app_name: str
        :param Name: of app to display
        :param client_secrets_file: str
        :param Path: to client_secret
        :param oauth_path: str
        :param Path: to gmail
        """
        GoogleApiOAuth.__init__(
            self,
            "https://www.googleapis.com/auth/gmail.send",  # scope
            app_name,
            os.path.join(client_secrets_file),  # app secrets
            os.path.join(oauth_path),  # user credential
        )

    def create_driver(self):
        """:returns: driver
            GMail API driver

        """
        return super().get_driver("gmail", "v1")


def get_mime_message(subject, text):
    """
    :param subject: str
    :param Subject: of email
    :param text: str
    :param Email: content
    :returns: MIMEText
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
    :param Sender: of email
    :param msg: str
    :param Message: to send to me
    :param driver: GMailApiOAuth driver
    :param GMail: authenticator
      Sends email to me with this message
    """
    driver.users().messages().send(
        userId=sender,
        body=msg
    ).execute()  # send message
