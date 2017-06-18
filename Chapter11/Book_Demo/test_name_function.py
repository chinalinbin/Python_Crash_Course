# coding:utf-8

# import unittest
# from name_function import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):
#     """test_name_function.py"""
#
#     def test_first_last_name(self):
#         """能够正确处理Janis Jophin这样的姓名吗？"""
#         formatted_name = get_formatted_name('janis', 'jophin')
#         self.assertEqual(formatted_name, 'Janis Jophin')
#
# unittest.main()

import unittest
from Python_Crash_Course.Chapter11.Book_Demo.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
