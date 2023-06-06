#!/usr/bin/python3
"""class called MagicString that has a fixed number of
slots specified """


class LockedClass:
    """no new items can be added to list if user is already defined"""
    __slots__ = ['first_name']
