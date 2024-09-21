import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify, request
from app import app  # Assuming your Flask app is named 'app' in app.py

class TestSubmitEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        self.sample_data = {
            "PassengerId": "12345",
            "HomePlanet": "Earth",
            "CryoSleep": False,
            "Cabin": "C123",
            "Destination": "Mars",
            "Age": 29.5,
            "VIP": False,
            "RoomService": 100.0,
            "FoodCourt": 200.0,
            "ShoppingMall": 150.0,
            "Spa": 80.0,
            "VRDeck": 120.0,
            "Name": "John Doe",
        }

        self.invalid_sample_data = {
            "PassengerId": None,  # Invalid value
            "HomePlanet": 123,  # Invalid type
            "CryoSleep": "unknown",  # Invalid type
            "Cabin": "",  # Invalid value
            "Destination": None,  # Invalid value
            "Age": -5,  # Invalid value
            "VIP": "yes",  # Invalid type
            "RoomService": "free",  # Invalid type
            "FoodCourt": -100,  # Invalid value
            "ShoppingMall": "none",  # Invalid type
            "Spa": -50,  # Invalid value
            "VRDeck": "zero",  # Invalid type
            "Name": "",  # Invalid value
        }

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_submit_endpoint(self, mock_commit, mock_add):
        response = self.app.post('/api/submit', json=self.sample_data)

        self.assertEqual(response.status_code, 200)
        print(response.json.keys())
        self.assertIn(response.json['status'], ['safe', 'transported'])

        mock_add.assert_called_once()
        mock_commit.assert_called_once()

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_submit_endpoint_invalid_data(self, mock_commit, mock_add):
        response = self.app.post('/api/submit', json=self.invalid_sample_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

        mock_add.assert_not_called()
        mock_commit.assert_not_called()

if __name__ == '__main__':
    unittest.main()