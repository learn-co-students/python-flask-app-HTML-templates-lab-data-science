import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from hello_world import app


class TestSimpleFlaskApp(unittest.TestCase):

    def test_guest_class_methods(self):
        self.assertItemsEqual()
        self.assertEqual()
