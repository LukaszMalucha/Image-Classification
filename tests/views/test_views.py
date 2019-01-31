from unittest import TestCase
from app import app


class TestHome(TestCase):

    ## Home Test

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)

    # Login page loads correctly

    def test_login_page_loads(self):
        with app.test_client() as c:
            response = c.get('/login', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Please Log in' in response.data)

    # Signup page loads correctly

    def test_signin_page_loads(self):
        with app.test_client() as c:
            response = c.get('/register', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Sign In' in response.data)

    # Digit Recognition page loads correctly

    def test_digit_recognition_page_loads(self):
        with app.test_client() as c:
            response = c.get('/digit_recognition', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Predict' in response.data)

    # Classify image page loads correctly

    def test_classify_image_page_loads(self):
        with app.test_client() as c:
            response = c.get('/classify', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Provide the URL with *.jpg or *.png location' in response.data)


    # Cat Dog Classifier page loads correctly

    def test_cat_dog_classifier_page_loads(self):
        with app.test_client() as c:
            response = c.get('/classifier', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Upload your image in .jpg format:' in response.data)
