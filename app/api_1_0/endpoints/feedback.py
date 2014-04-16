from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = [
    ("id", "int"),
    ("created_at", "str")
]
req_attr = [
    ("creator", "int"),
    ("source", "str"),
    ("title", "str"),
    ("description", "str")
]
opt_attr = [
    ("jira_url", "str"),
    ("status", "str"),
    ("owner", "str")
]
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = [
    0,
    "2014-01-01T00:00:00Z"
]
req_sample_data = [
    1,
    "Spotify",
    "UI needed for Parse API to return an additional field which posts the entire raw message.",
    "As a user I would like for the Parse API to return an additional field which posts the entire raw message \
    (the full EML content)."
]
opt_sample_data = [
    "https://jira.sendgrid.net/browse/SB-74",
    "Open",
    "Product"
]
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
feedback_items = {}
for index, (attr, type) in enumerate(all_attr):
    feedback_items[attr] = all_sample_data[index]
feedback = []
feedback.append(feedback_items)

# Build the fields for the Marshal function
feedback_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        feedback_fields[attr] = fields.String
    elif type == "int":
        feedback_fields[attr] = fields.Integer
    elif type == "bool":
        feedback_fields[attr] = fields.Boolean
feedback_fields["uri"] = fields.Url('feedback')

class Feedback(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Feedback, self).__init__()

    def get(self, id=None):
        if id == None:
            return { 'feedback': map(lambda t: marshal(t, feedback_fields), feedback) }
        feedback_member = filter(lambda t: t['id'] == id, feedback)
        if len(feedback_member) == 0:
            abort(404)
        return marshal(feedback_member[0], feedback_fields)

    def patch(self, id):
        feedback_member = filter(lambda t: t['id'] == id, feedback)
        if len(feedback_member) == 0:
            abort(404)
        feedback_member = feedback_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                feedback_member[k] = v
        return marshal(feedback_member, feedback_fields)

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        feedback_member = {}
        feedback_member["id"] = feedback[-1]['id'] + 1
        feedback_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            feedback_member[attr] = args[attr]
        feedback.append(feedback_member)
        return marshal(feedback_member, feedback_fields), 201

    def delete(self, id):
        feedback_member = filter(lambda t: t['id'] == id, feedback)
        if len(feedback_member) == 0:
            abort(404)
        feedback_member = feedback_member[0]
        feedback.remove(feedback_member)
        return 204