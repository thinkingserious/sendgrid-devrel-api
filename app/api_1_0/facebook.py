from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = []
req_attr = [
    ("likes", "int")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = []
req_sample_data = [
    10000
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
facebook_items = {}
for index, (attr, type) in enumerate(all_attr):
    facebook_items[attr] = all_sample_data[index]
facebook = []
facebook.append(facebook_items)

# Build the fields for the Marshal function
facebook_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        facebook_fields[attr] = fields.String
    elif type == "int":
        facebook_fields[attr] = fields.Integer
    elif type == "bool":
        facebook_fields[attr] = fields.Boolean
facebook_fields["uri"] = fields.Url('facebook')

class Facebook(Resource):
    def __init__(self):
        return

    def get(self):
        return {'facebook': map(lambda t: marshal(t, facebook_fields), facebook)}