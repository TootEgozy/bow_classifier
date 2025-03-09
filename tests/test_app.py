import unittest, time
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_server_ready_before_data_loaded(self):
        response = self.client.get('/server_ready')
        self.assertEqual(response.status_code, 503)

    def test_server_ready_after_data_loaded(self):
        self.client.get('/server_ready')
        time.sleep(60)
        response = self.client.get('/server_ready')
        self.assertEqual(response.status_code, 204)

    def test_generate_inputs_valid(self):
        response = self.client.post('/generate_inputs', json={
            'cls_type': 'spam',
            'count': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('inputs', response.json)

    def test_generate_inputs_missing_data(self):
        response = self.client.post('/generate_inputs', json={'cls_type': 'some_type'})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing 'cls_type' or 'count'", response.json['error'])

    def test_classify_valid(self):
        global learning_data
        learning_data = {'some_type': 'some_value'}
        response = self.client.post('/classify', json={
            'cls_type': 'some_type',
            'input_text': 'Test input text'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

    def test_classify_missing_data(self):
        response = self.client.post('/classify', json={'cls_type': 'some_type'})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing 'cls_type' or 'input_text'", response.json['error'])

if __name__ == '__main__':
    unittest.main()
