# coding=utf-8
__author__ = 'Tang'

import lib.xmltodict as xmltodict
import unittest


class PatentFileException(Exception):
    """Raised when file is empty"""
    def __init__(self, filename):
        self.filename = filename


class Patent:
    """Patent data as extracted from XML"""
    def __init__(self, filename):
        with open(filename, 'r') as infile:
            data = infile.read().replace('\n', '')
        if data is not None:
            temp_dict = xmltodict.parse(data)
            self.dict = dict()
            for each in temp_dict['doc']['str']:
                if u'#text' in each.keys() and u'#text' in each.keys():
                    self.dict[each[u'@name']] = each[u'#text']
        else:
            raise PatentFileException(filename)

    def get_data(self):
        return self.dict


class TestPatentClass(unittest.TestCase):

    def test_read_patent(self):
        with open("tests/json/patent_class_test1.txt", 'r') as infile:
            output = infile.read().replace('\n', '')
        p = Patent("corpus/patsnap-corpus/EP0049154B2.xml")
        self.assertEqual(output, str(p.get_data()))

if __name__ == '__main__':
    unittest.main()