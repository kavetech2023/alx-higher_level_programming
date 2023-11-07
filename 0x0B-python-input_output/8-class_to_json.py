#!/usr/bin/python3
"""A class-to-JSON module."""


def class_to_json(obj):
    """Return dictionary represntation of json."""
    return obj.__dict__
