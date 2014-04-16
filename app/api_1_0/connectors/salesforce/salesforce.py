import os
from configobj import ConfigObj
from simple_salesforce import Salesforce
from flask.ext.restful import Resource

class SF(Resource):
    def __init__(self):
        return

    # Right now this endpoint is being debugged, but I've verified it connects and returns
    # the right values
    def get(self):
        config = ConfigObj('./app/config.ini')
        sf = Salesforce(
            username=config['SF_USER'],
            password=config['SF_PASS'],
            security_token=config['SF_TOKEN'],
            sandbox=True)
        dict = sf.query("SELECT Email FROM User WHERE Title = 'Developer Evangelist' AND LastName = 'Thomas'")
        # Debug: print list(dict.keys())
        ret = "Total Size: " + str(dict[u'totalSize'])
        ret += "Is Done? " + str(dict[u'done'])
        dict2 = dict[u'records'][0]
        # Debug: print list(dict2.keys())
        # Debug: print dict2[u'attributes']
        ret += "Email: " + dict2[u'Email']
        dict3 = dict2[u'attributes']
        # Debug: print list(dict3.keys())
        ret += "Type: " + dict3[u'type']
        ret += "URL: " + dict3[u'url']
        return ret