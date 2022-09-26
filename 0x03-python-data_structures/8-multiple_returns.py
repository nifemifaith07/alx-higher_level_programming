#!/usr/bin/python3

def multiple_returns(sentence):
    """
    returns a tuple with the length of a string
    and its first character
    """
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
