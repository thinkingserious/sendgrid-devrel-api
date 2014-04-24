from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
from endpoint_utils import EndpointUtils
from ...connectors.salesforce.salesforce import SF
import datetime

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

class Relationship(Resource, EndpointUtils):
    def __init__(self):
        # Define the automatic, required and optional attributes
        self.auto_attr = [
            ("id", "int"),
            ("created_at", "str")
        ]
        self.req_attr = [
            ("owner", "int"),
            ("first_name", "str"),
            ("email", "str"),
            ("status", "str")
        ]
        self.opt_attr = [
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
        self.all_attr = self.auto_attr + self.req_attr + self.opt_attr
        self.relationship_fields = EndpointUtils.create_dict_of_keys(self, self.all_attr)
        self.reqparse = EndpointUtils.create_request_parser(self, self.req_attr, self.opt_attr)
        self.salesforce = SF()
        result = self.salesforce.put_relationship()
        print result
        # Build sample data JSON object
        relationship_items = {}
        for index, (attr, type) in enumerate(self.all_attr):
            relationship_items[attr] = all_sample_data[index]
        self.relationship = []
        self.relationship.append(relationship_items)
        super(Relationship, self).__init__()

    def get(self, id=None):
        if id == None:
            return { 'relationship': map(lambda t: marshal(t, self.relationship_fields), self.relationship) }
        relationship_member = filter(lambda t: t['id'] == id, self.relationship)
        if len(relationship_member) == 0:
            abort(404)
        return marshal(relationship_member[0], self.relationship_fields)

    def patch(self, id):
        relationship_member = filter(lambda t: t['id'] == id, self.relationship)
        if len(relationship_member) == 0:
            abort(404)
        relationship_member = relationship_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                relationship_member[k] = v
        return '', 204

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        relationship_member = {}
        relationship_member["id"] = self.relationship[-1]['id'] + 1
        relationship_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(self.req_attr + self.opt_attr):
            relationship_member[attr] = args[attr]
        self.relationship.append(relationship_member)
        return marshal(relationship_member, self.relationship_fields), 201

    def delete(self, id):
        relationship_member = filter(lambda t: t['id'] == id, self.relationship)
        if len(relationship_member) == 0:
            abort(404)
        relationship_member = relationship_member[0]
        self.relationship.remove(relationship_member)
        return '', 204