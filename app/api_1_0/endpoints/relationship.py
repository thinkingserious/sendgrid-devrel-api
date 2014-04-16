from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = [
    ("id", "int"),
    ("created_at", "str")
]
req_attr = [
    ("owner", "int"),
    ("first_name", "str"),
    ("email", "str"),
    ("status", "str")
]
opt_attr = [
    ("volume", "int"),
    ("venue", "int"),
    ("event_date", "str"),
    ("last_name", "str"),
    ("job_title", "str"),
    ("company_name", "str"),
    ("function", "str"),
    ("website", "str"),
    ("phone_number", "str"),
    ("city", "str"),
    ("state", "str"),
    ("country", "str"),
    ("use_case", "str"),
    ("feedback", "str"),
    ("github", "str"),
    ("twitter", "str"),
    ("linkedin", "str"),
    ("gplus", "str"),
    ("facebook", "str"),
    ("notes", "str")
]
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = [
    0,
    "2014-01-01T00:00:00Z"
]
req_sample_data = [
    0,
    "E-Dizzle",
    "elmer.thomas@edizzle.com",
    "dev rel nurture"
]
opt_sample_data = [
    1000000,
    0,
    "2013-12-31",
    "T-Sizzle",
    "Hacker in Residence",
    "SendGrid",
    "Comedian",
    "www.edizzle.com",
    "951-999-9999",
    "Riverside",
    "CA",
    "USA",
    "To help developers deliver the awesome, E-Dizzle style",
    "MOAR Parse API features.",
    "thinkingserious",
    "thinkingserious",
    "thinkingserious",
    "+ElmerThomas",
    "thinkingserious",
    "This guy wears a computer on his face. Might want to keep your distance"
]
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
relationship_items = {}
for index, (attr, type) in enumerate(all_attr):
    relationship_items[attr] = all_sample_data[index]
relationship = []
relationship.append(relationship_items)

# Build the fields for the Marshal function
relationship_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        relationship_fields[attr] = fields.String
    elif type == "int":
        relationship_fields[attr] = fields.Integer
    elif type == "bool":
        relationship_fields[attr] = fields.Boolean
relationship_fields["uri"] = fields.Url('relationship')

class Relationship(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Relationship, self).__init__()

    def get(self, id=None):
        if id == None:
            return { 'relationship': map(lambda t: marshal(t, relationship_fields), relationship) }
        relationship_member = filter(lambda t: t['id'] == id, relationship)
        if len(relationship_member) == 0:
            abort(404)
        return marshal(relationship_member[0], relationship_fields)

    def patch(self, id):
        relationship_member = filter(lambda t: t['id'] == id, relationship)
        if len(relationship_member) == 0:
            abort(404)
        relationship_member = relationship_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                relationship_member[k] = v
        return marshal(relationship_member, relationship_fields)

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        relationship_member = {}
        relationship_member["id"] = relationship[-1]['id'] + 1
        relationship_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            relationship_member[attr] = args[attr]
        relationship.append(relationship_member)
        return marshal(relationship_member, relationship_fields), 201

    def delete(self, id):
        relationship_member = filter(lambda t: t['id'] == id, relationship)
        if len(relationship_member) == 0:
            abort(404)
        relationship_member = relationship_member[0]
        relationship.remove(relationship_member)
        return 204