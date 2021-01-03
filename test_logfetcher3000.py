import os
import unittest

from unittest.mock import patch

from logfetcher3000.logfetcher3000 import *

class TestLogFetcher3000(unittest.TestCase):
    @patch('os.path.isfile')
    def test_file_exists(self, mock_isfile):
        expected = 'links.json'
        mock_isfile.return_value = True
        actual = file_exists('links.json')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
