import service
from unittest import TestCase
from unittest.mock import patch

class TestService(TestCase):
  @patch('service.Service.bad_random', return_value=10)
  def test_bad_random(self, bad_random):
    self.assertEqual(bad_random(), 10)

  @patch('service.Service.bad_random', return_value=10)
  def test_divide(self, divide):
    self.assertEqual(divide(2), 5)
  
  





