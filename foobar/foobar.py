#!/usr/bin/env python
# -*- coding: utf-8 -*-


def multiply(a, b):
    """return a * b
    """
    return a * b


class Dog(object):
    """class for Dog"""
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        """add a trick"""
        self.tricks.append(trick)
