from flask import Blueprint
from flask.ext.restful import Api
from .endpoints.team import Team
from .endpoints.relationship import Relationship
from .endpoints.event import Event
from .endpoints.feedback import Feedback
from .endpoints.project import Project
from .endpoints.blog import Blog
from .endpoints.accelerator import Accelerator
from .endpoints.social.twitter import Twitter
from .endpoints.social.stackoverflow import StackOverflow
from .endpoints.social.quora import Quora
from .endpoints.social.facebook import Facebook
from .endpoints.social.gplus import Gplus
from .endpoints.social.klout import Klout
from .endpoints.opensource.docs import Docs
from .endpoints.opensource.csharp import Csharp
from .endpoints.opensource.java import Java
from .endpoints.opensource.nodejs import NodeJS
from .endpoints.opensource.objc import ObjC
from .endpoints.opensource.perl import Perl
from .endpoints.opensource.php import PHP
from .endpoints.opensource.python import Python

api_blueprint = Blueprint('api', __name__)
api = Api(prefix='/api/v1.0')

# Register the endpoints
api.add_resource(Team, '/team/<string:id>', '/team')
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