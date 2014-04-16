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
    ("name", "str"),
    ("description", "str")
]
opt_attr = [
    ("status", "str"),
    ("project_url", "str")
]
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = [
    0,
    "2014-01-01T00:00:00Z"
]
req_sample_data = [
    0,
    "Dev Rel App",
    "The app that will be created using this API"
]
opt_sample_data = [
    "In Progress",
    "http://docs.sendgrid.apiary.io"
]
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
project_items = {}
for index, (attr, type) in enumerate(all_attr):
    project_items[attr] = all_sample_data[index]
project = []
project.append(project_items)

# Build the fields for the Marshal function
project_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        project_fields[attr] = fields.String
    elif type == "int":
        project_fields[attr] = fields.Integer
    elif type == "bool":
        project_fields[attr] = fields.Boolean
project_fields["uri"] = fields.Url('project')

class Project(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Project, self).__init__()

    def get(self, id=None):
        if id == None:
            return {'project': map(lambda t: marshal(t, project_fields), project)}
        project_member = filter(lambda t: t['id'] == id, project)
        if len(project_member) == 0:
            abort(404)
        return marshal(project_member[0], project_fields)

    def patch(self, id):
        project_member = filter(lambda t: t['id'] == id, project)
        if len(project_member) == 0:
            abort(404)
        project_member = project_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                project_member[k] = v
        return marshal(project_member, project_fields)

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        project_member = {}
        project_member["id"] = project[-1]['id'] + 1
        project_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            project_member[attr] = args[attr]
        project.append(project_member)
        return marshal(project_member, project_fields), 201

    def delete(self, id):
        project_member = filter(lambda t: t['id'] == id, project)
        if len(project_member) == 0:
            abort(404)
        project_member = project_member[0]
        project.remove(project_member)
        return 204