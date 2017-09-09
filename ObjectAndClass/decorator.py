# -*- encoding:utf-8 -*-
# __author__=='Gan'
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#
#     # Repeated property code, but for a different name (bad!)
#     @property
#     def last_name(self):
#         return self._last_name
#
#     @last_name.setter
#     def last_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._last_name = value
#

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def decorator(self, func):
        pass
