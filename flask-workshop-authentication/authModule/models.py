import hashlib
from app import *
from flask import session
import os
# from pyresparser import ResumeParser
from bson import ObjectId


class auth1:
    def __init__(self):
        self.mongo = mongo.db

    def register_user(self,obj):
        result=self.mongo.users.insert(obj)
        return result

    def login_user(self,obj):
        result=list(self.mongo.users.find(obj))
        print(result)
        if len(result)>0:
            return result[0]
        else:
            return False

    