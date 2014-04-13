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
nodejs_items = {}
for index, (attr, type) in enumerate(all_attr):
    nodejs_items[attr] = all_sample_data[index]
nodejs = []
nodejs.append(nodejs_items)

# Build the fields for the Marshal function
nodejs_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        nodejs_fields[attr] = fields.String
    elif type == "int":
        nodejs_fields[attr] = fields.Integer
    elif type == "bool":
        nodejs_fields[attr] = fields.Boolean
nodejs_fields["uri"] = fields.Url('nodejs')

class NodeJS(Resource):
    def __init__(self):
        return

    def get(self):
        return {'nodejs': map(lambda t: marshal(t, nodejs_fields), nodejs)}