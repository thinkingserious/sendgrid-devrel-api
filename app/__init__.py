from flask import Flask
from flask.ext.restful import Api

from api_1_0.endpoints.team import Team
from api_1_0.endpoints.relationship import Relationship
from api_1_0.endpoints.event import Event
from api_1_0.endpoints.feedback import Feedback
from api_1_0.endpoints.project import Project
from api_1_0.endpoints.blog import Blog
from api_1_0.endpoints.accelerator import Accelerator

from api_1_0.endpoints.social.twitter import Twitter
from api_1_0.endpoints.social.stackoverflow import StackOverflow
from api_1_0.endpoints.social.quora import Quora
from api_1_0.endpoints.social.facebook import Facebook

from api_1_0.endpoints.social.gplus import Gplus
from api_1_0.endpoints.social.klout import Klout
from api_1_0.endpoints.opensource.docs import Docs
from api_1_0.endpoints.opensource.csharp import Csharp
from api_1_0.endpoints.opensource.java import Java
from api_1_0.endpoints.opensource.nodejs import NodeJS
from api_1_0.endpoints.opensource.objc import ObjC
from api_1_0.endpoints.opensource.perl import Perl
from api_1_0.endpoints.opensource.php import PHP
from api_1_0.endpoints.opensource.python import Python

from api_1_0.connectors.salesforce.salesforce import SF

app = Flask(__name__)
api = Api(app)
app.config.from_envvar('SENDGRIDDEVRELAPI_SETTINGS')

# Register the endpoints
api.add_resource(Team, '/team/<int:id>', '/team')
api.add_resource(Relationship, '/relationship/<int:id>', '/relationship')
api.add_resource(Event, '/event/<int:id>', '/event')
api.add_resource(Feedback, '/feedback/<int:id>', '/feedback')
api.add_resource(Project, '/project/<int:id>', '/project')
api.add_resource(Blog, '/blog/<int:id>', '/blog')
api.add_resource(Accelerator, '/accelerator/<int:id>', '/accelerator')
# Social related endpoints
api.add_resource(Twitter, '/social/twitter')
api.add_resource(StackOverflow, '/social/stackoverflow/<int:id>', '/social/stackoverflow')
api.add_resource(Quora, '/social/quora/<int:id>', '/social/quora')
api.add_resource(Facebook, '/social/facebook')
api.add_resource(Gplus, '/social/gplus')
api.add_resource(Klout, '/social/klout')
api.add_resource(Docs, '/opensource/docs')
# Open Source related endpoints
api.add_resource(Csharp, '/opensource/csharp')
api.add_resource(Java, '/opensource/java')
api.add_resource(NodeJS, '/opensource/nodejs')
api.add_resource(ObjC, '/opensource/objc')
api.add_resource(Perl, '/opensource/perl')
api.add_resource(PHP, '/opensource/php')
api.add_resource(Python, '/opensource/python')
# TODO: Remove this endpoint when done with testing this connector
api.add_resource(SF, '/salesforce')