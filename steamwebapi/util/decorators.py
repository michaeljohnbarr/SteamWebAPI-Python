# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import sys


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
    all = sys.modules[f.__module__].__dict__.setdefault('__all__', [])
    # Prevent duplicates if run from an IDE.
    if f.__name__ not in all:
        all.append(f.__name__)
    return f

public(public)  # Emulate decorating ourself
