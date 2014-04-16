from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = []
req_attr = [
    ("id", "int"),
    ("reputation", "int")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = []
req_sample_data = [
    0,
    100
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
stackoverflow_items = {}
for index, (attr, type) in enumerate(all_attr):
    stackoverflow_items[attr] = all_sample_data[index]
stackoverflow = []
stackoverflow.append(stackoverflow_items)

# Build the fields for the Marshal function
stackoverflow_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        stackoverflow_fields[attr] = fields.String
    elif type == "int":
        stackoverflow_fields[attr] = fields.Integer
    elif type == "bool":
        stackoverflow_fields[attr] = fields.Boolean
stackoverflow_fields["uri"] = fields.Url('stackoverflow')

class StackOverflow(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(StackOverflow, self).__init__()

    def get(self, id=None):
        if id == None:
            return {'stackoverflow': map(lambda t: marshal(t, stackoverflow_fields), stackoverflow)}
        stackoverflow_member = filter(lambda t: t['id'] == id, stackoverflow)
        if len(stackoverflow_member) == 0:
            abort(404)
        return marshal(stackoverflow_member[0], stackoverflow_fields)
