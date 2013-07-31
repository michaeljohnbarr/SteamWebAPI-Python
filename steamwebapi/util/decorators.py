# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import sys
from functools import wraps


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


def api_key_required(f):
    def decorator(self, *args, **kwargs):
        if not self.key:
            raise Exception('You dun fucked up.')
    return decorator
