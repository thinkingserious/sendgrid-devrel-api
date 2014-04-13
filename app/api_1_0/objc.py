from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = []
req_attr = [
    ("downloads", "int"),
    ("forks", "int"),
    ("watches", "int"),
    ("stars", "int"),
    ("pull_requests", "int"),
    ("closed_issues", "int"),
    ("new_issues", "int"),
    ("traffic", "int"),
    ("contributors", "int")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = []
req_sample_data = [
    1000000,
    5000,
    60000,
    10000,
    500000,
    1000,
    100,
    2000000,
    10
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
objc_items = {}
for index, (attr, type) in enumerate(all_attr):
    objc_items[attr] = all_sample_data[index]
objc = []
objc.append(objc_items)

# Build the fields for the Marshal function
objc_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        objc_fields[attr] = fields.String
    elif type == "int":
        objc_fields[attr] = fields.Integer
    elif type == "bool":
        objc_fields[attr] = fields.Boolean
objc_fields["uri"] = fields.Url('objc')

class ObjC(Resource):
    def __init__(self):
        return

    def get(self):
        return {'objc': map(lambda t: marshal(t, objc_fields), objc)}