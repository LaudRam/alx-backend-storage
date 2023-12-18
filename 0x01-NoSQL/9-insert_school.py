#!/usr/bin/env python3
''' Inserts a new document in a collection '''
import pymongo


def insert_school(mongo_collection, **kwargs):
    ''' insert into school '''
    return mongo_collection.insert_one(kwargs).inserted_id
