from flask.ext.restful import Resource, marshal, abort
from endpoint_utils import EndpointUtils
from ...connectors.salesforce.salesforce import SF

# Documentation for this endpoint: http://docs.sendgrid.apiary.io
class Team(Resource, EndpointUtils):
    def __init__(self):
        # Define the automatically generated, required and optional attributes
        self.auto_attr = [
            ("ID", "str")
        ]
        self.req_attr = [
            ("URL", "str"),
            ("Type", "str"),
            ("FirstName", "str"),
            ("LastName", "str"),
            ("Email", "str"),
            ("Phone", "str"),
            ("HomeCity", "str")
        ]
        self.opt_attr = []
        self.all_attr = self.auto_attr + self.req_attr + self.opt_attr
        self.team_fields = EndpointUtils.create_dict_of_keys(self, self.all_attr)
        self.reqparse = EndpointUtils.create_request_parser(self, self.req_attr, self.opt_attr)
        self.salesforce = SF()
        team_members = self.salesforce.get_team()
        self.team = EndpointUtils.build_data_container(self, team_members, self.all_attr, "/api/v1.0/team/", "ID")
        super(Team, self).__init__()

    def get(self, id=None):
        if id == None:
            return {'team': map(lambda t: marshal(t, self.team_fields), self.team)}
        # Return a single team member
        team_member = filter(lambda t: t['ID'] == id, self.team)
        if len(team_member) == 0:
            abort(404, error="404", message="Endpoint {} doesn't exist".format(id))
        return marshal(team_member[0], self.team_fields)

    def patch(self, id):
        team_member = filter(lambda t: t['ID'] == id, self.team)
        if len(team_member) == 0:
            abort(404, error="404", message="Endpoint {} doesn't exist".format(id))
        team_member = team_member[0]
        args = self.reqparse.parse_args()
        found_key = EndpointUtils.execute_patch(self, args, team_member)
        if found_key:
            return '', 204
        else:
            abort(400, error="400", message="Key {} not found".format(id))