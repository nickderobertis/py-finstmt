from py_qs_example.mymodule import ExampleClass, example_function, less_important_function


class TestExampleClass:
    ec = ExampleClass(5)

    def test_attrs(self):
        ec = ExampleClass(10, self.ec)
        assert ec.num == 10
        assert ec.klass == self.ec

    def test_do_something(self):
        assert self.ec.do_something('stuff') == 'stuff'

    def test_repr(self):
        assert self.ec.__repr__() == 'example'


def test_example_function():
    ec = ExampleClass(5)
    output = example_function(ec, '_test')
    assert output == 'example_test'


def test_less_important_function():
    assert less_important_function(5) == str(5)
