import unittest, sys
sys.path.insert(0, '..')
from app import app

class HelloWorldTestCase(unittest.TestCase):
    testy = app.test_client()

    def test_index_status_code(self):
        response = self.testy.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_html(self):
        response = self.testy.get('/')
        raw = response.data
        result = raw.decode("utf-8")
        h1, p_tag = result.split("</h1>")
        self.assertTrue('<h1>Welcome to my flask app' in h1)
        self.assertTrue('<p>be careful, it\'s still under construction...</p>' in p_tag)

    def test_user_profile_status_code(self):
        response = self.testy.get('/profile/frank')
        self.assertEqual(response.status_code, 200)

    def test_user_profile_html(self):
        response = self.testy.get('/profile/frank')
        raw = response.data
        result = raw.decode("utf-8")
        self.assertTrue('<h1>Welcome to Frank\'s profile</h1>' in result)

    def test_hello_world_template_status_code(self):
        response = self.testy.get('/hello-world-template')
        self.assertEqual(response.status_code, 200)

    def test_hello_world_template_html(self):
        response = self.testy.get('/hello-world-template')
        raw = response.data
        result = raw.decode("utf-8")
        self.assertTrue('<h1>Hello again, World! This is a template!</h1>' in result)

    def test_profile_page_template_status_code(self):
        response = self.testy.get('/profile/frank/31/foisting_toasters/jackson_hole,wy')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_template_html(self):
        response = self.testy.get('/profile/frank/31/foisting_toasters/jackson_hole,wy')
        raw = response.data
        result = raw.decode("utf-8")
        self.assertTrue('<h1>Welcome to Frank\'s profile!</h1>' in result)
        self.assertTrue('<h3>About Frank:</h3>' in result)
        self.assertTrue('<strong>Age:</strong>'in result)
        self.assertTrue('<li>31</li>' in result)
        self.assertTrue('<strong>Favorite Hobby:</strong>' in result)
        self.assertTrue('<li>Foisting_Toasters</li>' in result)
        self.assertTrue('<strong>Hometown:</strong>' in result)
        self.assertTrue('<li>Jackson Hole, WY</li>' in result)
