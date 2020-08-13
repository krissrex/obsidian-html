from unittest import TestCase
from ..format import *

class TestFormat(TestCase):
    def test_format_internal_link(self):
        result = format_internal_links("Hello [[here is link]]")
        self.assertEqual(result, "Hello [here is link](\"here is link.md\")")
