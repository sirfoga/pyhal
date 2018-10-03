# !/usr/bin/python3
# coding: utf-8


""" Markdown r/w models """


class MarkdownItem:
    """Models anything that can be written in Markdown """

    TYPES = ["text", "url", "image", "title"]
    ATTRIBUTES = ["ref", "size"]

    def __init__(self, text, type, attributes=None):
        """
        :param text: str
            Text property to write
        :param type: MarkdownItem.TYPES
            Type of item
        :param attributes: {}
            Extra param, like url, ref ... Each key MUST be in
            MarkdownItem.ATTRIBUTES
        """

        self.text = str(text)
        self.type = type
        self.attributes = attributes

    def to_markdown(self):
        if self.type == "text":
            return self.text
        elif self.type == "url" or self.type == "image":
            return "[" + self.text + "](" + self.attributes["ref"] + ")"
        elif self.type == "title":
            return "#" * int(self.attributes["size"]) + " " + self.text

        raise ValueError("Cannot generate a type `" + self.type + "`")

    def __str__(self):
        return self.to_markdown()


class MarkdownTable:
    """Models and writes a table to .md"""

    def __init__(self, labels, table):
        self.labels = labels
        self.table = table

    @staticmethod
    def _get_row(items):
        items = [
            str(item)
            for item in items
        ]  # convert to strings
        return "|" + "|".join(items) + "|"

    def _get_header(self):
        out = self._get_row(self.labels)
        out += "\n"
        out += self._get_row(["---"] * len(self.labels))  # line below headers
        return out

    def to_markdown(self):
        out = self._get_header()
        out += "\n"

        for row in self.table:
            out += self._get_row(row)
            out += "\n"

        return out

    def __str__(self):
        return self.to_markdown()
