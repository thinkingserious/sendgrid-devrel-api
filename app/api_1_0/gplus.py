from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = []
req_attr = [
    ("followers", "int"),
    ("plusses", "int")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = []
req_sample_data = [
    20000,
    1000
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
gplus_items = {}
for index, (attr, type) in enumerate(all_attr):
    gplus_items[attr] = all_sample_data[index]
gplus = []
gplus.append(gplus_items)

# Build the fields for the Marshal function
gplus_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        gplus_fields[attr] = fields.String
    elif type == "int":
        gplus_fields[attr] = fields.Integer
    elif type == "bool":
        gplus_fields[attr] = fields.Boolean
gplus_fields["uri"] = fields.Url('gplus')

class Gplus(Resource):
    def __init__(self):
        return

    def get(self):
        return {'gplus': map(lambda t: marshal(t, gplus_fields), gplus)}