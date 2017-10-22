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


""" Some utils methods for a selenium web-driver """


class SeleniumForm:
    """ Great and simple static methods to deal with selenium web-drivers. """

    @staticmethod
    def fill_form_field(browser, field_name, field_value):
        """
        :param browser: web-driver
            Browser to use to submit form.
        :param field_name :string
            Name of field to fill
        :param field_value: string
            Value with which to fill field.
        :return: void
            Fill given field with given value.
        """

        browser.execute_script(
            "document.getElementsByName(\"" + str(
                field_name) + "\")[0].value = \"" + str(field_value) + "\"")

    @staticmethod
    def fill_login_form(browser, username, username_field, user_password,
                        user_password_field):
        """
        :param browser: web-driver
            Browser to use to submit form
        :param username: string
            Username of user to login
        :param username_field: string
            Name of field to fill with username
        :param user_password: string
            Password of user to login
        :param user_password_field: string
            Name of field to fill with user password
        :return: void
            Form filled with given information
        """

        SeleniumForm.fill_form_field(browser, username_field,
                                     username)  # set username
        SeleniumForm.fill_form_field(browser, user_password_field,
                                     user_password)  # set password

    @staticmethod
    def submit_form(browser, button_name):
        """
        :param browser: web-driver
            Browser to use to submit form.
        :param button_name: string
            Name of button to press to submit form
        :return: void
            Submit form.
        """

        browser.execute_script(
            "document.getElementsByName(\"" + button_name + "\")[0].click()"
        )  # click button
