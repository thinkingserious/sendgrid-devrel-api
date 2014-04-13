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
    ("event_name", "str"),
    ("event_short_description", "str"),
    ("event_long_description", "str"),
    ("who_is_attending", "str"),
    ("start_date", "str"),
    ("end_date", "str"),
    ("venue", "int"),
    ("event_type", "str"),
    ("sendgrid_api_uses", "int"),
    ("number_of_attendees", "int"),
    ("participation", "str"),
    ("audience_type", "str"),
    ("education_focused", "bool"),
    ("should_we_attend", "bool"),
    ("registration_link", "str"),
    ("comments", "str")
]
opt_attr = [
    ("start_time", "str"),
    ("end_time", "str"),
    ("twitter", "str"),
    ("hash_tag", "str")
]
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = [
    0,
    "2014-01-01T00:00:00Z"
]
req_sample_data = [
    0,
    "McHack",
    "Find out who can make the best McBurger.",
    "Find out who can make the best McBurger. Given some burgers, cheese and condiments, let\'s see what you can do \
    in 24 hours.",
    "0, 1, 5",
    "2014-04-01",
    "2014-04-05",
    0,
    "other, cookathon",
    0,
    100,
    "demo sendgrid api, serve as mentor, other, cook",
    "evenly split between technical and non-technical",
    True,
    True,
    "www.mchack.com",
    "This was the most delicious hackathon ever. We should try to attend one for Burger King too."
]
opt_sample_data = [
    "6:00pm",
    "6:00pm",
    "mchack",
    "burgerandfries"
]
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
event_items = {}
for index, (attr, type) in enumerate(all_attr):
    event_items[attr] = all_sample_data[index]
event = []
event.append(event_items)

# Build the fields for the Marshal function
event_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        event_fields[attr] = fields.String
    elif type == "int":
        event_fields[attr] = fields.Integer
    elif type == "bool":
        event_fields[attr] = fields.Boolean
event_fields["uri"] = fields.Url('event')

class Event(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Event, self).__init__()

    def get(self, id=None):
        if id == None:
            return { 'event': map(lambda t: marshal(t, event_fields), event) }
        event_member = filter(lambda t: t['id'] == id, event)
        if len(event_member) == 0:
            abort(404)
        return marshal(event_member[0], event_fields)

    def patch(self, id):
        event_member = filter(lambda t: t['id'] == id, event)
        if len(event_member) == 0:
            abort(404)
        event_member = event_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                event_member[k] = v
        return marshal(event_member, event_fields)

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        event_member = {}
        event_member["id"] = event[-1]['id'] + 1
        event_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            event_member[attr] = args[attr]
        event.append(event_member)
        return marshal(event_member, event_fields), 201

    def delete(self, id):
        event_member = filter(lambda t: t['id'] == id, event)
        if len(event_member) == 0:
            abort(404)
        event_member = event_member[0]
        event.remove(event_member)
        return 204