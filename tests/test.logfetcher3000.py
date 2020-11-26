import unittest
import os

from unittest.mock import patch

import logfetcher3000

class TestLogFetcher3000(unittest.TestCase):
    @patch('os.path.isfile')
    def test_file_exists(self, mock_isfile):
        expected = 'links.json'
        mock_isfile.return_value = True
        actual = logfetcher3000.file_exists('links.json')
        self.assertEqual(actual, expected)
