import unittest
from armory.hellodeploy import kv_parser

class TestKVParser(unittest.TestCase):

    def test_kv_parser(self):
        mock_values = "#a comment \n key1=val1\nkey2=val2 "
        values = kv_parser.parse(mock_values)
        self.assertEquals(len(values), 2)
        self.assertEquals(values['key1'], 'val1')
        self.assertEquals(values['key2'], 'val2')
