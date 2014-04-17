import os
from configobj import ConfigObj
from simple_salesforce import Salesforce
from flask.ext.restful import Resource

class SF(Resource):
    def __init__(self):
        return

    # Right now this endpoint is being debugged
    # Status: we can get all the data we need from Salesforce to pass to the API
    # Next: convert this to a function and wire up to the team endpoint
    def get(self):
        config = ConfigObj('./app/config.ini')
        sf = Salesforce(
            username=config['SF_USER'],
            password=config['SF_PASS'],
            security_token=config['SF_TOKEN'],
            sandbox=True)
        dict = sf.query("SELECT Username, Title, FirstName, LastName, MobilePhone, Email, City "
                        "FROM User WHERE "
                        "(Title = 'Developer Evangelist' "
                        "OR Title = 'Community Guy' "
                        "OR Title = 'Developer Communications Director') "
                        "AND IsActive = True")
        ret = "Team Size: " + str(dict[u'totalSize']) + " "
        for i in range(dict[u'totalSize']):
            dict2 = dict[u'records'][i]
            # This is unique and in the form of an email, this will be our ID
            ret += "ID: " + dict2[u'Username'] + " "
            ret += "Type: " + dict2[u'Title'] + " "
            ret += "First Name: " + dict2[u'FirstName'] + " "
            ret += "Last Name: " + dict2[u'LastName'] + " "
            # There is also the option to get the SendGrid landline phone + Extension
            # TODO: get rid of the string conversion and make sure this value exists for all team members
            ret += "Phone: " + str(dict2[u'MobilePhone']) + " "
            ret += "Email: " + dict2[u'Email'] + " "
            # TODO: get rid of the string conversion and make sure this value exists for all team members
            ret += "Home City: " + str(dict2[u'City']) + " "
        return ret