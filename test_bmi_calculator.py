import unittest
from bmi_calculator import calculate_bmi_logic, convert_units

class TestBMICalculator(unittest.TestCase):

    def test_underweight(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 50)
        self.assertAlmostEqual(bmi, 16.33, places=2)
        self.assertEqual(category, "Underweight")

    def test_normal_weight(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 68)
        self.assertAlmostEqual(bmi, 22.2, places=1)
        self.assertEqual(category, "Normal weight")

    def test_overweight(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 80)
        self.assertAlmostEqual(bmi, 26.12, places=2)
        self.assertEqual(category, "Overweight")

    def test_obese(self):
        bmi, category, _ = calculate_bmi_logic(1.75, 95)
        self.assertAlmostEqual(bmi, 31.02, places=2)
        self.assertEqual(category, "Obese")

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi_logic(0, 50)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi_logic(1.75, 0)

    def test_convert_units_cm(self):
        height, weight = convert_units(175, 150, "cm", "kg")
        self.assertAlmostEqual(height, 1.75)
        self.assertAlmostEqual(weight, 150)

    def test_convert_units_feet(self):
        height, weight = convert_units(5.74, 150, "feet", "kg")
        self.assertAlmostEqual(height, 1.75, places=2)
        self.assertAlmostEqual(weight, 150)

    def test_convert_units_pounds(self):
        height, weight = convert_units(1.75, 330.69, "m", "pounds")
        self.assertAlmostEqual(height, 1.75)
        self.assertAlmostEqual(weight, 150, places=2)

if __name__ == "__main__":
    unittest.main()
