from flask.ext.restful import Resource, reqparse, fields, marshal, abort
from ...connectors.salesforce.salesforce import SF
import datetime

# Define the automatic, required and optional attributes
auto_attr = [
    ("ID", "str")
]
req_attr = [
    ("Type", "str"),
    ("FirstName", "str"),
    ("LastName", "str"),
    ("Email", "str"),
    ("Phone", "str"),
    ("HomeCity", "str"),
    ("URL", "str")
]
opt_attr = []
all_attr = auto_attr + req_attr + opt_attr

# Build the fields for the Marshal function
team_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        team_fields[attr] = fields.String
    elif type == "int":
        team_fields[attr] = fields.Integer
    elif type == "bool":
        team_fields[attr] = fields.Boolean

sf = SF()
r = sf.get_team()
team_items = {}
team = []
for i in range(len(r)):
    for index, (attr, type) in enumerate(all_attr):
        if attr == "URL":
            team_items[attr] = "/api/v1.0/team/" + r[i]["ID"]
        else:
            team_items[attr] = r[i][attr]
    team.append(team_items)
    team_items = {}

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
        # Return a single team member
        team_member = filter(lambda t: t['ID'] == id, team)
        if len(team_member) == 0:
            abort(404, error="404", message="endpoint {} doesn't exist".format(id))
        return marshal(team_member[0], team_fields)

    def patch(self, id):
        team_member = filter(lambda t: t['ID'] == id, team)
        if len(team_member) == 0:
            abort(404, error="404", message="endpoint {} doesn't exist".format(id))
        team_member = team_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                team_member[k] = v
        return '', 204
