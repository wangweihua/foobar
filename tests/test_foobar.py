#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `foobar` package."""
import pytest
from foobar.foobar import multiply, Dog


def test_multiply_3_3():
    assert multiply(3, 3) == 9


def test_multiply_x_3():
    assert multiply('x', 3) == 'xxx'


def test_multiply_list_3():
    res = multiply(['a', 'b'], 3)
    assert res == ['a', 'b', 'a', 'b', 'a', 'b']


@pytest.fixture()
def twodog():
    fido = Dog('Fido')
    buddy = Dog('Buddy')
    return fido, buddy


class TestDog(object):
    """test case of function multiply"""

    def test_name(self, twodog):
        fido, buddy = twodog
        assert fido.name == 'Fido'
        assert fido.tricks == []

    def test_add_trick(self, twodog):
        fido, buddy = twodog
        fido.add_trick('roll over')
        assert 'roll over' in fido.tricks

    def test_add_trick_02(self, twodog):
        fido, buddy = twodog
        fido.add_trick('play dead')
        buddy.add_trick('play dead')
        assert 'roll over' in fido.tricks
        assert 'play dead' in fido.tricks
        assert 'play dead' in buddy.tricks
