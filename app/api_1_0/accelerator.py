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
    ("accelerator_url", "str"),
    ("name", "str"),
    ("venue", "int")
]
opt_attr = [
    ("members", "int"),
    ("coupon_code", "str"),
    ("num_visits", "int"),
    ("last_visit_date", "str"),
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
    "http://www.sesamestreetincubator.com",
    "Sesame Street Incubator",
    2
]
opt_sample_data = [
    40,
    "sesame_street_sendgrid",
    4,
    "2014-01-20T00:00:00Z",
    "This is a cool place, but that Oscar is a grouch."
]
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
accelerator_items = {}
for index, (attr, type) in enumerate(all_attr):
    accelerator_items[attr] = all_sample_data[index]
accelerator = []
accelerator.append(accelerator_items)

# Build the fields for the Marshal function
accelerator_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        accelerator_fields[attr] = fields.String
    elif type == "int":
        accelerator_fields[attr] = fields.Integer
    elif type == "bool":
        accelerator_fields[attr] = fields.Boolean
accelerator_fields["uri"] = fields.Url('accelerator')

class Accelerator(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Accelerator, self).__init__()

    def get(self, id=None):
        if id == None:
            return {'accelerator': map(lambda t: marshal(t, accelerator_fields), accelerator)}
        accelerator_member = filter(lambda t: t['id'] == id, accelerator)
        if len(accelerator_member) == 0:
            abort(404)
        return marshal(accelerator_member[0], accelerator_fields)

    def patch(self, id):
        accelerator_member = filter(lambda t: t['id'] == id, accelerator)
        if len(accelerator_member) == 0:
            abort(404)
        accelerator_member = accelerator_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                accelerator_member[k] = v
        return marshal(accelerator_member, accelerator_fields)

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        accelerator_member = {}
        accelerator_member["id"] = accelerator[-1]['id'] + 1
        accelerator_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            accelerator_member[attr] = args[attr]
        accelerator.append(accelerator_member)
        return marshal(accelerator_member, accelerator_fields), 201

    def delete(self, id):
        accelerator_member = filter(lambda t: t['id'] == id, accelerator)
        if len(accelerator_member) == 0:
            abort(404)
        accelerator_member = accelerator_member[0]
        accelerator.remove(accelerator_member)
        return 204