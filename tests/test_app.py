import unittest
from app import app


class MyTest(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client()
        self.client.testing = True

    def test_a_test_that_contacts_the_server(self):

        data = {"cls_type": "spam", "count": 5}

        response = self.client.post('/generate_inputs?cls_type=spam', json=data)
        response_data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertIn('inputs', response_data, msg="Response doesn't contain 'inputs' field")
        self.assertIsInstance(response_data['inputs'], list, msg="'inputs' is not a list")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()