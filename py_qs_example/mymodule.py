"""
An example docstring for the mymodule module.

Describe what the entire module is for, with the first sentence containing the main idea.
"""
from typing import Optional


class ExampleClass:
    """
    An example class created from the pypi-sphinx-quickstart tutorial.
    """

    def __init__(self, num: int, klass: Optional['ExampleClass'] = None):
        """
        Class init method.

        Describe how to pass arguments here.

        :param num: example argument with builtin type
        :param klass: example argument with custom type
        """
        self.num = num
        self.klass = klass

    def do_something(self, arg: str) -> str:
        """
        Class method that does something.

        Describe it here.

        :param arg: A thing to pass
        :return: A return value

        :example:

        >>> import py_qs_example.mymodule
        >>> ec = py_qs_example.mymodule.ExampleClass(1)
        >>> ec.do_something('this')
        'this'

        """
        return arg

    def __repr__(self):
        return 'example'


def example_function(thing: ExampleClass, arg: str) -> str:
    """
    Example for function documentation.

    :param thing: A thing to pass
    :param arg: another thing to pass
    :return: thing and arg combined into a string

    :example:

    >>> import py_qs_example.mymodule
    >>> ec = py_qs_example.mymodule.ExampleClass(1)
    >>> py_qs_example.mymodule.example_function(ec, 'this')
    'examplethis'

    """
    return f'{thing}{arg}'


def _hidden_function(num: int) -> str:
    """
    Example which is documented but hidden.

    :param num:  A thing to pass
    :return: A return value
    """
    return f'{num}'


def less_important_function(num: int) -> str:
    """
    Example which is documented in the module documentation but not highlighted on the main page.

    :param num:  A thing to pass
    :return: A return value
    """
    return f'{num}'