"""
.. versionadded:: 0.9.2

Functions for wrapping strings in ANSI color codes.

Each function within this module returns the input string ``text``, wrapped
with ANSI color codes for the appropriate color.

For example, to print some text as green on supporting terminals::

    from fabric.colors import green

    print(green("This text is green!"))

Because these functions simply return modified strings, you can nest them::

    from fabric.colors import red, green

    print(red("This sentence is red, except for " + \
          green("these words, which are green") + "."))

If ``bold`` is set to ``True``, the ANSI flag for bolding will be flipped on
for that particular invocation, which usually shows up as a bold or brighter
version of the original color on most terminals.

.. versionchanged:: 1.11
    Added support for the shell env var ``FABRIC_DISABLE_COLORS``; if this
    variable is present and set to any non-empty value, all colorization driven
    by this module will be skipped/disabled.
"""

import os

def _wrap_with(code):

    def inner(text, bold=False):
        c = code

        if os.environ.get('FABRIC_DISABLE_COLORS'):
            return text

        if bold:
            c = "1;%s" % c
        return f"\033[{c}m{text}\033[0m"
    return inner

red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')
blue = _wrap_with('34')
magenta = _wrap_with('35')
cyan = _wrap_with('36')
white = _wrap_with('37')
