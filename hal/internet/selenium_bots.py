# -*- coding: utf-8 -*-

""" Some utils methods for a selenium web-driver """


class SeleniumForm:
    """Great and simple static methods to deal with selenium web-drivers"""

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def fill_form_field(browser, field_name, field_value):
        """
        # Arguments
          browser: web-driver
        Browser to use to submit form.
          field_name: string
        Name of field to fill
          field_value: string
        Value with which to fill field.

        # Returns:
          void
          Fill given field with given value.

        """
        browser.execute_script(
            "document.getElementsByName(\"" + str(
                field_name) + "\")[0].value = \"" + str(field_value) + "\"")

    @staticmethod
    def fill_login_form(browser, username, username_field, user_password,
                        user_password_field):
        """
        # Arguments
          browser: web-driver
        Browser to use to submit form
          username: string
        Username of user to login
          username_field: string
        Name of field to fill with username
          user_password: string
        Password of user to login
          user_password_field: string
        Name of field to fill with user password

        # Returns:
          void
          Form filled with given information

        """
        SeleniumForm.fill_form_field(browser, username_field,
                                     username)  # set username
        SeleniumForm.fill_form_field(browser, user_password_field,
                                     user_password)  # set password

    @staticmethod
    def submit_form(browser, button_name):
        """
        # Arguments
          browser: web-driver
        Browser to use to submit form.
          button_name: string
        Name of button to press to submit form

        # Returns:
          void
          Submit form.

        """
        browser.execute_script(
            "document.getElementsByName(\"" + button_name + "\")[0].click()"
        )  # click button
