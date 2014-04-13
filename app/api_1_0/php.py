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
php_items = {}
for index, (attr, type) in enumerate(all_attr):
    php_items[attr] = all_sample_data[index]
php = []
php.append(php_items)

# Build the fields for the Marshal function
php_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        php_fields[attr] = fields.String
    elif type == "int":
        php_fields[attr] = fields.Integer
    elif type == "bool":
        php_fields[attr] = fields.Boolean
php_fields["uri"] = fields.Url('php')

class PHP(Resource):
    def __init__(self):
        return

    def get(self):
        return {'php': map(lambda t: marshal(t, php_fields), php)}