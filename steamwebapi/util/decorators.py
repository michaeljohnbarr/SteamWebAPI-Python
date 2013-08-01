# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import sys

# Util Imports
from .exceptions import APIKeyRequiredError


# =============================================================================
# >> DECORATORS
# =============================================================================
def public(f):
    """"Use a decorator to avoid retyping function/class names.

    * Based on an idea by Duncan Booth:
    http://groups.google.com/group/comp.lang.python/msg/11cbb03e09611b8a
    * Improved via a suggestion by Dave Angel:
    http://groups.google.com/group/comp.lang.python/msg/3d400fb22d8a42e1

    """
    new_all = sys.modules[f.__module__].__dict__.setdefault('__all__', [])
    # Prevent duplicates if run from an IDE.
    if f.__name__ not in new_all:
        new_all.append(f.__name__)
    return f

public(public)  # Emulate decorating ourself (make public)


class api_key_required(object):
    """
    """

    def __init__(self, method):
        '''Store the method instance for further use'''
        self.method = method

    def __get__(self, instance, owner):
        '''Return the class value instead of the methods directly'''
        return self.__class__(self.method.__get__(instance, owner))

    def __call__(self, *args, **kwargs):
        '''Verifies that the key exists prior to calling the method'''

        # Does the class have an API key
        if not self.method.__self__.key:

            # Raise an error if no key is provided
            raise APIKeyRequiredError

        # Call the method and return
        return self.method(*args, **kwargs)
