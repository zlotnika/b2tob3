# -*- coding: utf-8 -*-
import unittest

from os.path import abspath, dirname, join
import sys

DIR_TESTS = abspath(dirname(__file__))
DIR_LIB = join(dirname(DIR_TESTS), 'b2tob3')
sys.path.insert(0, DIR_LIB)

from b2tob3.b2tob3 import make_replacements


def get_replacement(fname):
    file_type = 'html'
    if fname.endswith('.haml'):
        file_type = 'css'
    with open(join(DIR_TESTS, fname), 'r') as f:
        content = f.read()
    return make_replacements(content, file_type)


class B2tob3TestSuite(unittest.TestCase):
    """b2tob3 test cases."""

    def test_html_count(self):
        (content, count) = get_replacement('fluid.html')
        self.assertEqual(count, 22)

    def test_html_match(self):
        (content, count) = get_replacement('fluid.html')
        self.assertRegexpMatches(content, 'col-md-3')

    def test_haml_count(self):
        (content, count) = get_replacement('fluid.html.haml')
        self.assertEqual(count, 22)

    def test_haml_match(self):
        (content, count) = get_replacement('fluid.html.haml')
        self.assertRegexpMatches(content, 'col-md-3')
