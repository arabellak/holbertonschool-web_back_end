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
    mongo_collection.aggregate([
        {'$project': {'name': '$name', 'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}
    ])
