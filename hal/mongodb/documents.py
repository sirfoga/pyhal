# !/usr/bin/python3
# coding: utf-8

""" Various utilities to deal with MondoDB databases """

from pymongo import MongoClient


class DbBrowser:
    def __init__(self, db_name):
        """
        :param db_name: str
            Name of db
        """

        self.client = MongoClient()
        self.db = self.client[db_name]

    def get_documents_count(self):
        """
        :return: int
            Number of documents in db
        """

        db_collections = [
            self.db[c] for c in self.db.collection_names()
        ]  # list of all collections in database
        return sum([c.count() for c in db_collections])  # sum

    def get_documents_in_collection(self, collection_name, with_id=True):
        """
        :param collection_name: str
            Name of collection
        :param with_id: bool
            True iff each document should also come with its id
        :return: [] of {}
            List of documents in collection in self.db
        """

        documents_iterator = self.db[collection_name].find()
        documents = [
            d for d in documents_iterator
        ]  # list of all documents in collection in database

        if not with_id:
            for doc in documents:
                doc.pop("_id")  # remove id key

        return documents

    def get_documents_in_database(self, with_id=True):
        """
        :param with_id: bool
            True iff each document should also come with its id
        :return: [] of {}
            List of documents in collection in database
        """

        documents = []
        for coll in self.db.collection_names():
            documents += self.get_documents_in_collection(
                coll,
                with_id=with_id
            )

        return documents
