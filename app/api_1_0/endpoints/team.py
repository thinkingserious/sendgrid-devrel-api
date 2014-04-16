from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = [
    ("id", "int"),
    ("created_at", "str")
]
req_attr = [
    ("type", "str"),
    ("first_name", "str"),
    ("last_name", "str"),
    ("email", "str"),
    ("phone", "str"),
    ("home_city", "str")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = [
    0,
    "2014-01-01T00:00:00Z"
]
req_sample_data = [
    "Hacker in Residence",
    "Elmer",
    "Thomas",
    "elmer@sendgrid.com",
    "951.801.4624",
    "Riverside"
]
opt_sample_data = []
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
team_items = {}
for index, (attr, type) in enumerate(all_attr):
    team_items[attr] = all_sample_data[index]
team = []
team.append(team_items)

# Build the fields for the Marshal function
team_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        team_fields[attr] = fields.String
    elif type == "int":
        team_fields[attr] = fields.Integer
    elif type == "bool":
        team_fields[attr] = fields.Boolean
team_fields["uri"] = fields.Url('team')

class Team(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Team, self).__init__()

    def get(self, id=None):
        if id == None:
            return {'team': map(lambda t: marshal(t, team_fields), team)}
        team_member = filter(lambda t: t['id'] == id, team)
        if len(team_member) == 0:
            abort(404)
        return marshal(team_member[0], team_fields)

    def patch(self, id):
        team_member = filter(lambda t: t['id'] == id, team)
        if len(team_member) == 0:
            abort(404)
        team_member = team_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                team_member[k] = v
        return marshal(team_member, team_fields)

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        team_member = {}
        team_member["id"] = team[-1]['id'] + 1
        team_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            team_member[attr] = args[attr]
        team.append(team_member)
        return marshal(team_member, team_fields), 201

    def delete(self, id):
        team_member = filter(lambda t: t['id'] == id, team)
        if len(team_member) == 0:
            abort(404)
        team_member = team_member[0]
        team.remove(team_member)
        return 204