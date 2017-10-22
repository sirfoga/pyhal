# !/usr/bin/python
# coding: utf_8

# Copyright 2017-2018 Race UP
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


def send_email(sender, msg, oauth):
    """
    :param sender: str
        Sender of email
    :param msg: str
        Message to send to me
    :param oauth: GMailApiOAuth
        GMail authenticator
    :return: void
        Sends email to me with this message
    """

    service = oauth.create_driver()
    service.users().messages().send(
        userId=sender,
        body=msg
    ).execute()  # send message
