This API allows you to interact with data related to SendGrid's Dev Rel (Developer Relations) KPIs (Key Performance Indicators). The goal is to make this code general enough for usage by any Developer Relations team.

# Setup

* Clone this repo
* `virtualenv venv`
* `source venv/bin/activate`
* `pip install flask`
* `pip install flask-restful`
* make run.py executable, then `./run.py`
* Look in the [tests file](https://github.com/thinkingserious/sendgrid-devrel-api/blob/master/app/tests/manual_tests.txt) for some example test commands

# Documentation

The documentation is located on [Apiary](http://docs.sendgrid.apiary.io). The source file for the documentation is in [apiary.apib](https://github.com/thinkingserious/sendgrid-devrel-api/blob/master/apiary.apib).

# Application

The API is implemented in Python/Flask. The source code can be found in the [app directory](https://github.com/thinkingserious/sendgrid-devrel-api/tree/master/app).
