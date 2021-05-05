#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
        Return
         - New _id
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc
