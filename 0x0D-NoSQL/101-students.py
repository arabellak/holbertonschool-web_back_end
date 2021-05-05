#!/usr/bin/env python3
"""
Returns all students sorted by average score:
"""
import pymongo


def top_students(mongo_collection):
    """
        Return
         - Sorted students
    """
    mongo_collection.find().sort(-1)
