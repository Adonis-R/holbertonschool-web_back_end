#!/usr/bin/env python3
'''Write a Python function that changes all topics
of a school document based on the name'''


def update_topics(mongo_collection, name, topics):
    '''update_topics: changes all topics of a school document based on the name'''
    if mongo_collection is None:
        return None
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
