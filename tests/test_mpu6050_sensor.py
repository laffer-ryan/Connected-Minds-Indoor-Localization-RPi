# tests/test_sensor.py
import unittest
from src.sensors.mpu_6050 import calculate_magnitude

class TestSensor(unittest.TestCase):
    def test_calculate_magnitude(self):
        data = {'x': 3, 'y': 4, 'z': 0}
        self.assertEqual(calculate_magnitude(data), 5.0)

if __name__ == "__main__":
    unittest.main()
