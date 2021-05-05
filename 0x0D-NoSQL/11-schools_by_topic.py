#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
        List of school having a specific topic:
    """
    specTop = mongo_collection.find({'topic': topic})
    return specTop
