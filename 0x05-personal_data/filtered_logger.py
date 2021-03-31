#!/usr/bin/env python3
"""Function called filter_datum that returns the log message obfuscated"""
import re


def filter_datum(fields: str, redaction: str, message: str, separator: str):
    """Return - Log message obfuscated"""
    for i in fields:
        message = re.sub(f'{i}=.+?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message
