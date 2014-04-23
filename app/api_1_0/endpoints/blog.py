from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal
import datetime

# Define the automatic, required and optional attributes
auto_attr = [
    ("id", "int"),
    ("created_at", "str")
]
req_attr = [
    ("author", "int"),
    ("blog_url", "str"),
    ("title", "str")
]
opt_attr = [
    ("content_type", "str"),
    ("status", "str"),
    ("date_published", "str"),
    ("start_date", "str"),
    ("end_date", "str"),
    ("unique_views", "int"),
    ("views", "int"),
    ("conversions", "int")
]
all_attr = auto_attr + req_attr + opt_attr

# Define sample data
auto_sample_data = [
    0,
    "2014-01-01T00:00:00Z"
]
req_sample_data = [
    0,
    "http://www.sendgrid.com/blog/the-best-blog-post-eva",
    "The Best Blog Post Eva!!!"
]
opt_sample_data = [
    "Technical",
    "Published",
    "2014-01-01T00:00:00Z",
    "2014-01-01T00:00:00Z",
    "2014-01-01T00:00:00Z",
    1000000,
    5000000,
    100000
]
all_sample_data = auto_sample_data + req_sample_data + opt_sample_data

# Build sample data JSON object
blog_items = {}
for index, (attr, type) in enumerate(all_attr):
    blog_items[attr] = all_sample_data[index]
blog = []
blog.append(blog_items)

# Build the fields for the Marshal function
blog_fields = {}
for index, (attr, type) in enumerate(all_attr):
    if type == "str":
        blog_fields[attr] = fields.String
    elif type == "int":
        blog_fields[attr] = fields.Integer
    elif type == "bool":
        blog_fields[attr] = fields.Boolean
blog_fields["uri"] = fields.Url('blog')

class Blog(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                self.reqparse.add_argument(attr, type=str, location='json')
            elif type == "int":
                self.reqparse.add_argument(attr, type=int, location='json')
            elif type == "bool":
                self.reqparse.add_argument(attr, type=bool, location='json')
        super(Blog, self).__init__()

    def get(self, id=None):
        if id == None:
            return {'blog': map(lambda t: marshal(t, blog_fields), blog)}
        blog_member = filter(lambda t: t['id'] == id, blog)
        if len(blog_member) == 0:
            abort(404)
        return marshal(blog_member[0], blog_fields)

    def patch(self, id):
        blog_member = filter(lambda t: t['id'] == id, blog)
        if len(blog_member) == 0:
            abort(404)
        blog_member = blog_member[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                blog_member[k] = v
        return '', 204

    def put(self):
        args = self.reqparse.parse_args()
        # Build the response object
        blog_member = {}
        blog_member["id"] = blog[-1]['id'] + 1
        blog_member["created_at"] = datetime.datetime.now()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            blog_member[attr] = args[attr]
        blog.append(blog_member)
        return marshal(blog_member, blog_fields), 201

    def delete(self, id):
        blog_member = filter(lambda t: t['id'] == id, blog)
        if len(blog_member) == 0:
            abort(404)
        blog_member = blog_member[0]
        blog.remove(blog_member)
        return '', 204