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
csharp_items = {}
for index, (attr, type) in enumerate(all_attr):
    csharp_items[attr] = all_sample_data[index]
csharp = []
csharp.append(csharp_items)

# Build the fields for the Marshal function
csharp_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        csharp_fields[attr] = fields.String
    elif type == "int":
        csharp_fields[attr] = fields.Integer
    elif type == "bool":
        csharp_fields[attr] = fields.Boolean
csharp_fields["uri"] = fields.Url('csharp')

class Csharp(Resource):
    def __init__(self):
        return

    def get(self):
        return {'csharp': map(lambda t: marshal(t, csharp_fields), csharp)}