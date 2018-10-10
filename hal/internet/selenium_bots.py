# -*- coding: utf-8 -*-

"""Some utils methods for a selenium web-driver """


class SeleniumForm:
    """Methods to deal with selenium web-drivers"""

    def __init__(self, browser):
        """
        :param browser: selenium browser to user
        """
        self.browser = browser

    def fill_form_field(self, field_name, field_value):
        """Fills given field with given value

        :param field_name: name of field to fill
        :param field_value: value with which to fill field
        """
        self.browser.execute_script(
            "document.getElementsByName(\"" + str(
                field_name) + "\")[0].value = \"" + str(field_value) + "\"")

    def fill_login_form(self, username, username_field, user_password,
                        user_password_field):
        """Fills form with login info

        :param username: user login
        :param username_field: name of field to fill with username
        :param user_password: login password
        :param user_password_field: name of field to fill with user password
        """
        self.fill_form_field(username_field, username)  # set username
        self.fill_form_field(user_password_field, user_password)  # set password

    def submit_form(self, button_name):
        """Submits form

        :param button_name: name of button to press to submit form
        """
        self.browser.execute_script(
            "document.getElementsByName(\"" + button_name + "\")[0].click()"
        )  # click button
