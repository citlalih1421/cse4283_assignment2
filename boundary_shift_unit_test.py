import unittest
from bmi_boundary_shift import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    def test_underweight(self):
        self.assertEqual(calculate_bmi(5, 6, 110), (17.8, "Underweight"))

    def test_normal_weight(self):
        self.assertEqual(calculate_bmi(5, 8, 150), (22.8, "Normal weight"))

    def test_overweight(self):
        self.assertEqual(calculate_bmi(5, 10, 180), (25.8, "Overweight"))

    def test_obese(self):
        self.assertEqual(calculate_bmi(6, 0, 250), (33.9, "Obese"))

    # Boundary tests
    def test_boundary_underweight(self):
        self.assertEqual(calculate_bmi(5, 8, 122), (18.5, "Normal weight"))
        self.assertEqual(calculate_bmi(5, 8, 121), (18.4, "Underweight"))

    def test_boundary_normal(self):
        self.assertEqual(calculate_bmi(5, 6, 154), (24.9, "Normal weight"))
        self.assertEqual(calculate_bmi(5, 6, 155), (25.0, "Overweight"))

    def test_boundary_overweight(self):
        self.assertEqual(calculate_bmi(5, 6, 185), (29.9, "Overweight"))
        self.assertEqual(calculate_bmi(5, 6, 186), (30.0, "Obese"))

if __name__ == "__main__":
    unittest.main()


