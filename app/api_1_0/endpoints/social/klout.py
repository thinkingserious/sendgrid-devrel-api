from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = []
req_attr = [
    ("score", "int")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = []
req_sample_data = [
    100
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
klout_items = {}
for index, (attr, type) in enumerate(all_attr):
    klout_items[attr] = all_sample_data[index]
klout = []
klout.append(klout_items)

# Build the fields for the Marshal function
klout_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        klout_fields[attr] = fields.String
    elif type == "int":
        klout_fields[attr] = fields.Integer
    elif type == "bool":
        klout_fields[attr] = fields.Boolean
klout_fields["uri"] = fields.Url('klout')

class Klout(Resource):
    def __init__(self):
        return

    def get(self):
        return {'klout': map(lambda t: marshal(t, klout_fields), klout)}