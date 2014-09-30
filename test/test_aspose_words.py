__author__ = 'AssadMahmood'
import unittest
import asposecloud
import os.path
import json

from asposecloud.words import Converter


class TestAsposeWords(unittest.TestCase):

    def setUp(self):
        with open('setup.json') as json_file:
            data = json.load(json_file)

        asposecloud.AsposeApp.app_key = str(data['app_key'])
        asposecloud.AsposeApp.app_sid = str(data['app_sid'])
        asposecloud.AsposeApp.output_path = str(data['output_location'])
        asposecloud.Product.product_uri = str(data['product_uri'])

    def test_convert_local_file(self):
        # Create object of words converter class
        converter = Converter('file_on_storage.docx')
        converter.convert_local_file('./data/test_convertlocal.docx', 'doc')
        self.assertEqual(True, os.path.exists('./output/test_convertlocal.doc'))

if __name__ == '__main__':
    unittest.main()
