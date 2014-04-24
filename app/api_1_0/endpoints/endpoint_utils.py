from flask.ext.restful import fields, reqparse

class EndpointUtils:
    def create_dict_of_keys(self, attr):
        endpoint_fields = {}
        for index, (key, type) in enumerate(attr):
            if type == "str":
                endpoint_fields[key] = fields.String
            elif type == "int":
                endpoint_fields[key] = fields.Integer
            elif type == "bool":
                endpoint_fields[key] = fields.Boolean
        return endpoint_fields

    def create_request_parser(self, req_attr, opt_attr):
        parser = reqparse.RequestParser()
        for index, (attr, type) in enumerate(req_attr + opt_attr):
            if type == "str":
                parser.add_argument(attr, type=str, location='json')
            elif type == "int":
                parser.add_argument(attr, type=int, location='json')
            elif type == "bool":
                parser.add_argument(attr, type=bool, location='json')
        return parser
        pass

    def build_data_container(self, objects, all_attr, endpoint, key):
        object_items = {}
        object = []
        for i in range(len(objects)):
            for index, (attr, type) in enumerate(all_attr):
                if attr == "URL":
                    object_items[attr] = endpoint + objects[i][key]
                else:
                    object_items[attr] = objects[i][attr]
            object.append(object_items)
            object_items = {}
        return object

    def execute_patch(self, args, object):
        for key, value in args.iteritems():
            found_key = False
            if value != None:
                object[key] = value
                found_key = True
        return found_key