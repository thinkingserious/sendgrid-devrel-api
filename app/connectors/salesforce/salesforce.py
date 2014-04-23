import os
from simple_salesforce import Salesforce
from flask.ext.restful import Resource

class SF(Resource):
    def __init__(self):
        self.sf = Salesforce(
            username=os.environ.get('SF_USER'),
            password=os.environ.get('SF_PASS'),
            security_token=os.environ.get('SF_TOKEN'),
            sandbox=True)
        return

    def get_team(self):
        dict = self.sf.query("SELECT Username, Title, FirstName, LastName, MobilePhone, Email, City "
                        "FROM User WHERE "
                        "(Title = 'Developer Evangelist' "
                        "OR Title = 'Community Guy' "
                        "OR Title = 'Developer Communications Director') "
                        "AND IsActive = True")
        team_items = {}
        team = []
        ret = "Team Size: " + str(dict[u'totalSize']) + " "
        for i in range(dict[u'totalSize']):
            dict2 = dict[u'records'][i]
            # This is unique and in the form of an email, this will be our ID
            team_items['ID'] = str(dict2[u'Username'])
            team_items['Type'] = str(dict2[u'Title'])
            team_items['FirstName'] = str(dict2[u'FirstName'])
            team_items['LastName'] = str(dict2[u'LastName'])
            # There is also the option to get the SendGrid landline phone + Extension
            # TODO: get rid of the string conversion and make sure this value exists for all team members
            team_items['Phone'] = str(dict2[u'MobilePhone'])
            team_items['Email'] = str(dict2[u'Email'])
            # TODO: get rid of the string conversion and make sure this value exists for all team members
            team_items['HomeCity'] = str(dict2[u'City'])
            team.append(team_items)
            team_items={}
        return team