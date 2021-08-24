import unittest
from die import Die

class TestDie(unittest.TestCase):
    """Tests for die.py"""

    def test_init(self):
        """Test die.__init__"""
        d = Die()
        self.assertEqual(d.Value(), 1)
        self.assertEqual(d.Sides(), 6)