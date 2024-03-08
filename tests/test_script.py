import unittest
from calculator import Calculator

class TestCalc(unittest.TestCase):
  def setUp(self):
    self.calculator=Calculator()

  def test_add(self):
    result=self.calculator.add(4,8)
    self.assertEqual(result,12)

  def test_subtract(self):
    result=self.calculator.subtract(8,4)
    self.assertEqual(result,4)

  def test_multiply(self):
    result=self.calculator.multiply(4,8)
    self.assertEqual(result,32)

  def test_divide(self):
    result=self.calculator.divide(8,4)
    self.assertEqual(result,2)

if __name__ == '__main__':
  unittest.main()
