import unittest
from flask import current_app
import requests, json


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.VERSION = 'v1.0'
        self.BASE_URL = 'http://127.0.0.1:5000/api/' + self.VERSION
        self.headers={'content-type': 'application/json'}

    def tearDown(self):
        pass

    # Did our app instantiate correctly?
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # Bad URL should throw a 404
    def test_404(self):
        r = requests.get(self.BASE_URL + '/does/not/exist')
        self.assertTrue(r.status_code == 404)

    def test_team(self):
        url = self.BASE_URL + '/team'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/elmer.thomas@sendgrid.com.devrel')
        self.assertTrue(r.status_code == 200)

        payload = {'Email': 'elmer.thomas@sendgrid.com.devrel'}
        r = requests.patch(url + '/elmer.thomas@sendgrid.com.devrel', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {'Email': 'elmer.thomas@sendgrid.com'}
        r = requests.patch(url + '/elmer.thomas@sendgrid.com.devrel', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {'Bogus': 'data'}
        r = requests.patch(url + '/elmer.thomas@sendgrid.com.devrel', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 400)

        payload = {'Email': 'elmer.thomas@sendgrid.com'}
        r = requests.patch(url + '/bad/url', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 404)

    def test_relationship(self):
        url = self.BASE_URL + '/relationship'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

        payload = {'company_name': 'E-Dizzle Enterprises'}
        r = requests.patch(url + '/0', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {
            "owner": 0,
            "first_name": "Hulk",
            "email": "hulkster@hulk.hogan.com",
            "status": "dev rel nurture"
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        print r.text
        self.assertTrue(r.status_code == 201)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 200)

        r = requests.delete(url + '/1')
        self.assertTrue(r.status_code == 204)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 404)

    def test_event(self):
        url = self.BASE_URL + '/event'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

        payload = {'twitter': 'SendGrid'}
        r = requests.patch(url + '/0', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {
            "owner": 0,
            "event_name": "BurgerKingHack",
            "event_short_description": "Find out who can make the best Burger King Burger.",
            "event_long_description": "Find out who can make the best Burger King. Given some burgers, cheese and condiments, let us see what you can do in 24 hours.",
            "who_is_attending": "0, 2, 5",
            "start_date": "2014-04-06",
            "end_date": "2014-04-10",
            "venue": 0,
            "event_type": "other, cookathon",
            "sendgrid_api_uses": 0,
            "number_of_attendees": 50,
            "participation": "demo sendgrid api, other, cook",
            "audience_type": "evenly split between technical and non-technical",
            "education_focused": "False",
            "should_we_attend": "True",
            "registration_link": "www.burgerkinghack.com",
            "comments": "This hackathon was terrible, let us stick to McHack."
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 201)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 200)

        r = requests.delete(url + '/1')
        self.assertTrue(r.status_code == 204)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 404)

    def test_feedback(self):
        url = self.BASE_URL + '/feedback'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

        payload = {'owner': 'Dominic'}
        r = requests.patch(url + '/0', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {
            "creator": 0,
            "source": "CapitalOne",
            "title": "Sign Up",
            "description": "They want to know what is in our wallets."
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 201)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 200)

        r = requests.delete(url + '/1')
        self.assertTrue(r.status_code == 204)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 404)

    def test_project(self):
        url = self.BASE_URL + '/project'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

        payload = {'status': 'On Fire'}
        r = requests.patch(url + '/0', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {
            "owner": 1,
            "name": "Wrestlemania",
            "description": "A wrestling revival."
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 201)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 200)

        r = requests.delete(url + '/1')
        self.assertTrue(r.status_code == 204)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 404)

    def test_blog(self):
        url = self.BASE_URL + '/blog'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

        payload = {'content_type': 'Tutorial'}
        r = requests.patch(url + '/0', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {
            "author": 1,
            "url": "http://www.sendgrid.com/blog/why-wrestlemania-is-totally-technical",
            "description": "Why Wrestlemania is Totally Technical"
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 201)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 200)

        r = requests.delete(url + '/1')
        self.assertTrue(r.status_code == 204)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 404)

    def test_accelerator(self):
        url = self.BASE_URL + '/accelerator'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

        payload = {'notes': 'Forget Oscar, hang out with Elmo instead.'}
        r = requests.patch(url + '/0', json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 204)

        payload = {
            "owner": 0,
            "accelerator_url": "http://www.acceleratorsareus.com",
            "name": "Accelerators are Us",
            "venue": 4
        }
        r = requests.put(url, json.dumps(payload), headers=self.headers)
        self.assertTrue(r.status_code == 201)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 200)

        r = requests.delete(url + '/1')
        self.assertTrue(r.status_code == 204)

        r = requests.get(url + '/1')
        self.assertTrue(r.status_code == 404)

    def test_stackoverflow(self):
        url = self.BASE_URL + '/social/stackoverflow'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

    def test_quora(self):
        url = self.BASE_URL + '/social/quora'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

        r = requests.get(url + '/0')
        self.assertTrue(r.status_code == 200)

    def test_twitter(self):
        url = self.BASE_URL + '/social/twitter'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_facebook(self):
        url = self.BASE_URL + '/social/facebook'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_gplus(self):
        url = self.BASE_URL + '/social/gplus'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_klout(self):
        url = self.BASE_URL + '/social/klout'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_docs(self):
        url = self.BASE_URL + '/opensource/docs'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_csharp(self):
        url = self.BASE_URL + '/opensource/csharp'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_java(self):
        url = self.BASE_URL + '/opensource/java'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_nodejs(self):
        url = self.BASE_URL + '/opensource/nodejs'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_objc(self):
        url = self.BASE_URL + '/opensource/objc'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_perl(self):
        url = self.BASE_URL + '/opensource/perl'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_php(self):
        url = self.BASE_URL + '/opensource/php'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

    def test_python(self):
        url = self.BASE_URL + '/opensource/python'

        r = requests.get(url)
        self.assertTrue(r.status_code == 200)

if __name__ == '__main__':
    unittest.main()