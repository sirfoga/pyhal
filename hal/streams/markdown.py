# -*- coding: utf-8 -*-

"""Markdown r/w models """


class MarkdownItem:
    """Models anything that can be written in Markdown"""

    TYPES = ["text", "url", "image", "title"]
    ATTRIBUTES = ["ref", "size"]

    def __init__(self, text, type, attributes=None):
        """
        :param text: Text property to write
        :param type: Type of item
        :param attributes: Extra param, like url, ref ... Each key MUST be in
            MarkdownItem.ATTRIBUTES
        """
        self.text = str(text)
        self.type = type
        self.attributes = attributes

    def to_markdown(self):
        """Converts to markdown
        :returns: item in markdown format
        """
        if self.type == "text":
            return self.text
        elif self.type == "url" or self.type == "image":
            return "[" + self.text + "](" + self.attributes["ref"] + ")"
        elif self.type == "title":
            return "#" * int(self.attributes["size"]) + " " + self.text

    def __str__(self):
        return self.to_markdown()


class MarkdownTable:
    """Models and writes a table to .md"""

    def __init__(self, labels, table):
        """
        :param labels: Column names
        :param table: table data
        """
        self.labels = labels
        self.table = table

    @staticmethod
    def _get_row(items):
        """

        :param items: array
        :returns: markdown-formatted array
        """
        items = [
            str(item)
            for item in items
        ]  # convert to strings
        return "|" + "|".join(items) + "|"

    def _get_header(self):
        """Gets header of table

        :returns: markdown-formatted header"""
        out = self._get_row(self.labels)
        out += "\n"
        out += self._get_row(["---"] * len(self.labels))  # line below headers
        return out

    def to_markdown(self):
        """Converts to markdown
        :returns: item in markdown format
        """
        out = self._get_header()
        out += "\n"

        for row in self.table:
            out += self._get_row(row)
            out += "\n"

        return out

    def __str__(self):
        return self.to_markdown()
