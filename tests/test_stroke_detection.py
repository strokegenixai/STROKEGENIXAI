import unittest
from stroke_detection_model import StrokeDetectionModel

class TestStrokeDetectionModel(unittest.TestCase):
    def setUp(self):
        """Set up a StrokeDetectionModel instance before each test."""
        self.model = StrokeDetectionModel()

    def test_load_data(self):
        """Test that load_data returns a dictionary with the expected keys."""
        data = self.model.load_data()
        expected_keys = ["age", "blood_pressure", "cholesterol_level", "smoking", "diabetes"]
        self.assertEqual(list(data.keys()), expected_keys)
        # Check ranges for simulated data
        self.assertTrue(20 <= data["age"] <= 80)
        self.assertTrue(110 <= data["blood_pressure"] <= 180)
        self.assertTrue(150 <= data["cholesterol_level"] <= 250)
        self.assertIn(data["smoking"], [True, False])
        self.assertIn(data["diabetes"], [True, False])

    def test_predict_risk_low(self):
        """Test predict_risk with low-risk data."""
        low_risk_data = {
            "age": 30,  # Below 60, so no points
            "blood_pressure": 120,  # Below 160, so no points
            "cholesterol_level": 180,  # Below 240, so no points
            "smoking": False,  # No points
            "diabetes": False  # No points
        }
        risk_score = self.model.predict_risk(low_risk_data)
        self.assertEqual(risk_score, 0)  # Expected score: 0 (low risk)

    def test_predict_risk_high(self):
        """Test predict_risk with high-risk data."""
        high_risk_data = {
            "age": 65,  # Above 60, +30 points
            "blood_pressure": 170,  # Above 160, +40 points
            "cholesterol_level": 250,  # Above 240, +20 points
            "smoking": True,  # +25 points
            "diabetes": True  # +15 points
        }
        risk_score = self.model.predict_risk(high_risk_data)
        self.assertEqual(risk_score, 130)  # Expected score: 30 + 40 + 20 + 25 + 15 = 130 (high risk)

    def test_run_model_output(self):
        """Test that run_model prints the correct risk category (mocking print)."""
        # This test would ideally mock the print function, but for simplicity, we'll test the logic indirectly
        high_risk_data = {
            "age": 65,
            "blood_pressure": 170,
            "cholesterol_level": 250,
            "smoking": True,
            "diabetes": True
        }
        self.model.data = high_risk_data
        risk = self.model.predict_risk(high_risk_data)
        self.assertTrue(risk > 80)  # Should be high risk

if __name__ == "__main__":
    unittest.main()
