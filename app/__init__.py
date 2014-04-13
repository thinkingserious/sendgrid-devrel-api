from flask import Flask
from flask.ext.restful import Api

from api_1_0.team import Team
from api_1_0.relationship import Relationship
from api_1_0.event import Event
from api_1_0.feedback import Feedback
from api_1_0.project import Project
from api_1_0.blog import Blog
from api_1_0.accelerator import Accelerator

from api_1_0.twitter import Twitter
from api_1_0.stackoverflow import StackOverflow
from api_1_0.quora import Quora
from api_1_0.facebook import Facebook
from api_1_0.gplus import Gplus
from api_1_0.klout import Klout

from api_1_0.docs import Docs
from api_1_0.csharp import Csharp
from api_1_0.java import Java
from api_1_0.nodejs import NodeJS
from api_1_0.objc import ObjC
from api_1_0.perl import Perl
from api_1_0.php import PHP
from api_1_0.python import Python

app = Flask(__name__)
api = Api(app)

# Register the endpoints
api.add_resource(Team, '/team/<int:id>', '/team')
api.add_resource(Relationship, '/relationship/<int:id>', '/relationship')
api.add_resource(Event, '/event/<int:id>', '/event')
api.add_resource(Feedback, '/feedback/<int:id>', '/feedback')
api.add_resource(Project, '/project/<int:id>', '/project')
api.add_resource(Blog, '/blog/<int:id>', '/blog')
api.add_resource(Accelerator, '/accelerator/<int:id>', '/accelerator')
api.add_resource(Twitter, '/social/twitter')
api.add_resource(StackOverflow, '/social/stackoverflow/<int:id>', '/social/stackoverflow')
api.add_resource(Quora, '/social/quora/<int:id>', '/social/quora')
api.add_resource(Facebook, '/social/facebook')
api.add_resource(Gplus, '/social/gplus')
api.add_resource(Klout, '/social/klout')
api.add_resource(Docs, '/opensource/docs')
api.add_resource(Csharp, '/opensource/csharp')
api.add_resource(Java, '/opensource/java')
api.add_resource(NodeJS, '/opensource/nodejs')
api.add_resource(ObjC, '/opensource/objc')
api.add_resource(Perl, '/opensource/perl')
api.add_resource(PHP, '/opensource/php')
api.add_resource(Python, '/opensource/python')