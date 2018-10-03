# !/usr/bin/python
# coding: utf_8


""" Use GMail APIs from python """

import os
from email.mime.text import MIMEText

from internet.services.google import GoogleApiOAuth


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
