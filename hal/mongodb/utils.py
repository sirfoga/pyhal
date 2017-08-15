# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
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

""" Various utilities to deal with MondoDB databases """

from pymongo import MongoClient


def get_documents_count(db_name):
    """
    :param db_name: str
        Name of db
    :return: int
        Number of documents in db
    """

    mongo_client = MongoClient()  # mongodb client
    db = mongo_client[db_name]  # db to scan
    db_collections = [
        db[c] for c in db.collection_names()
        ]  # list of all collections in database
    return sum([c.count() for c in db_collections])  # sum


def get_documents_in_collection(db_name, collection_name, with_id=True):
    """
    :param db_name: str
        Name of db
    :param collection_name: str
        Name of collection
    :param with_id: bool
        True iff each document should also come with its id
    :return: [] of {}
        List of documents in collection in database
    """

    mongo_client = MongoClient()  # mongodb client
    db = mongo_client[db_name]  # db to scan
    documents_iterator = db[collection_name].find()
    documents = [
        d for d in documents_iterator
        ]  # list of all documents in collection in database
    if not with_id:  # remove id key
        for d in documents:
            d.pop("_id")

    return documents


def get_documents_in_database(db_name, with_id=True):
    """
    :param db_name: str
        Name of db
    :param with_id: bool
        True iff each document should also come with its id
    :return: [] of {}
        List of documents in collection in database
    """

    documents = []
    mongo_client = MongoClient()  # mongodb client
    db = mongo_client[db_name]  # db to scan
    for c in db.collection_names():
        documents += get_documents_in_collection(db_name, c, with_id=with_id)
    return documents
