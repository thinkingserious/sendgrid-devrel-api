from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = []
req_attr = [
    ("id", "int"),
    ("questions_answered", "int"),
    ("upvotes", "int")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = []
req_sample_data = [
    0,
    100,
    10
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
quora_items = {}
for index, (attr, type) in enumerate(all_attr):
    quora_items[attr] = all_sample_data[index]
quora = []
quora.append(quora_items)

# Build the fields for the Marshal function
quora_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        quora_fields[attr] = fields.String
    elif type == "int":
        quora_fields[attr] = fields.Integer
    elif type == "bool":
        quora_fields[attr] = fields.Boolean
quora_fields["uri"] = fields.Url('quora')

class Quora(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Quora, self).__init__()

    def get(self, id=None):
        if id == None:
            return {'quora': map(lambda t: marshal(t, quora_fields), quora)}
        quora_member = filter(lambda t: t['id'] == id, quora)
        if len(quora_member) == 0:
            abort(404)
        return marshal(quora_member[0], quora_fields)
