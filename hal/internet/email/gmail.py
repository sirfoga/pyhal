# !/usr/bin/python
# coding: utf_8


"""Use GMail APIs from python """

import os
from email.mime.text import MIMEText

from hal.internet.services.google.gauthenticator import GoogleApiOAuth


class GMailApiOAuth(GoogleApiOAuth):
    def __init__(self, app_name, client_secrets_file, oauth_path):

        """
        :param app_name: Name of app to display
        :param client_secrets_file: Path to client_secret
        :param oauth_path: Path to gmail
        """
        GoogleApiOAuth.__init__(
            self,
            "https://www.googleapis.com/auth/gmail.send",  # scope
            app_name,
            os.path.join(client_secrets_file),  # app secrets
            os.path.join(oauth_path),  # user credential
        )

    def create_driver(self):
        """Creates GMail driver

        :returns: GMail API driver
        """
        return super().get_driver("gmail", "v1")


def get_mime_message(subject, text):
    """Creates MIME message

    :param subject: Subject of email
    :param text: Email content
    :returns: Email formatted as HTML ready to be sent
    """
    message = MIMEText(
        "<html>" +
        str(text).replace("\n", "<br>") +
        "</html>", "html"
    )
    message["subject"] = str(subject)
    return message


def send_email(sender, msg, driver):
    """Sends email to me with this message

    :param sender: Sender of email
    :param msg: Message to send to me
    :param driver: GMail authenticator
    """
    driver.users().messages().send(
        userId=sender,
        body=msg
    ).execute()  # send message
