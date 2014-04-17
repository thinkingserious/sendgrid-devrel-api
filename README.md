This API allows you to interact with data related to SendGrid's Dev Rel (Developer Relations) KPIs (Key Performance Indicators). The goal is to make this code general enough for usage by any Developer Relations team.

# Setup

* Clone this repo
* `virtualenv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* make run.py executable, then `./run.py`
* Look in the [tests file](https://github.com/thinkingserious/sendgrid-devrel-api/blob/master/app/tests/manual_tests.txt) for some example test commands

# Documentation

The documentation is located on [Apiary](http://docs.sendgrid.apiary.io). The source file for the documentation is in [apiary.apib](https://github.com/thinkingserious/sendgrid-devrel-api/blob/master/apiary.apib). To utilize that source file, [sign up for a free Apiary.io account](http://apiary.io). For offline testing, see [Dredd](http://blog.apiary.io/2013/10/17/How-to-test-api-with-api-blueprint-and-dredd).

# Application

The API is implemented in Python/Flask. The source code can be found in the [app directory](https://github.com/thinkingserious/sendgrid-devrel-api/tree/master/app).
