"""
An example docstring for the mypackage.module module.

Describe what the entire module is for, with the first sentence containing the main idea.
"""

class ExampleClass2:
    """
    An example class created from the pypi-sphinx-quickstart tutorial.
    """

    def __init__(self, num: int, klass: 'ExampleClass2'):
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

        :param arg: Example argument with builtin type
        :return: A return value
        """
        return arg

def example_function2(thing: ExampleClass2, arg: str) -> str:
    """
    Example for function documentation.

    :param thing: A thing to pass
    :param arg: another thing to pass
    :return: thing and arg combined into a string
    """
    return f'{thing}{arg}'