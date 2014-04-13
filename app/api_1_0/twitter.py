from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = []
req_attr = [
    ("followers", "int"),
    ("retweets", "int"),
    ("favorites", "int")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = []
req_sample_data = [
    2000,
    1000,
    1000
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
twitter_items = {}
for index, (attr, type) in enumerate(all_attr):
    twitter_items[attr] = all_sample_data[index]
twitter = []
twitter.append(twitter_items)

# Build the fields for the Marshal function
twitter_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        twitter_fields[attr] = fields.String
    elif type == "int":
        twitter_fields[attr] = fields.Integer
    elif type == "bool":
        twitter_fields[attr] = fields.Boolean
twitter_fields["uri"] = fields.Url('twitter')

class Twitter(Resource):
    def __init__(self):
        return

    def get(self):
        return {'twitter': map(lambda t: marshal(t, twitter_fields), twitter)}