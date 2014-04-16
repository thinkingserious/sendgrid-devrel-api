from simple_salesforce import Salesforce
from collections import OrderedDict
sf = Salesforce(username='elmer.thomas@sendgrid.com.devrel', password='1zXPBGAP3u', security_token='qXbCaPfQmgLAUFy2wN0WS1e5N', sandbox=True)
dict = sf.query("SELECT Email FROM User WHERE Title = 'Developer Evangelist' AND LastName = 'Thomas'")
# Debug: print list(dict.keys())
print "Total Size:\t" + str(dict[u'totalSize'])
print "Is Done?\t" + str(dict[u'done'])
dict2 = dict[u'records'][0]
# Debug: print list(dict2.keys())
# Debug: print dict2[u'attributes']
print "Email:\t\t" + dict2[u'Email']
dict3 = dict2[u'attributes']
# Debug: print list(dict3.keys())
print "Type:\t\t" + dict3[u'type']
print "URL:\t\t" + dict3[u'url']