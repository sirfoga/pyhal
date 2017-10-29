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

""" Email templates """

from email.mime.text import MIMEText

from hal.internet.email.utils import get_email_content


class EmailTemplate(object):
    """ Default email template """

    def __init__(self,
                 recipient,
                 subject,
                 content_file,
                 footer_file, extra_args=None):
        """
        :param recipient: str
            Name and surname of email recipient
        :param subject: str
            Title of email
        :param content_file: str
            Path to file containing email actual content
        :param footer_file: str
            Path to file containing email footer (ending)
        :param extra_args: {}
            Extra arguments and details about recipient
        """

        object.__init__(self)

        self.recipient = str(recipient).title().strip()
        self.email_subject = subject
        self.content_file = str(content_file)
        self.footer_file = str(footer_file)
        self.data = {} if not extra_args else extra_args

    def get_email_header(self):
        """
        :return: str
            Email header
        """

        return "<h2>Ciao " + str(self.recipient).title() + "!</h2><br>"

    def get_email_footer(self):
        """
        :return: str
            Email text (html formatted)
        """

        return get_email_content(self.footer_file)

    def get_mime_message(self):
        """
        :return: MIMEText
            Email formatted as HTML ready to be sent
        """

        message = MIMEText(
            "<html>" +
            self.get_email_header() +
            get_email_content(self.content_file) +
            self.get_email_footer() +
            "</html>", "html"
        )
        message["subject"] = self.email_subject
        return message