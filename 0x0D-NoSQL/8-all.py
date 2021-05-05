#!/usr/bin/env python3
"""
Lists all documents in a collection
"""
from pymongo import MongoClient
import pprint

def list_all(mongo_collection):
    """
    Return
     - If no document, empty list
    """
    if mongo_collection.count() <= 0:
        return []
    else:
        return mongo_collection.find()
