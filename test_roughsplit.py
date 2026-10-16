# test_roughsplit.py
"""
Tests for RoughSplit module.
"""

import unittest
from roughsplit import RoughSplit

class TestRoughSplit(unittest.TestCase):
    """Test cases for RoughSplit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughSplit()
        self.assertIsInstance(instance, RoughSplit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughSplit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
