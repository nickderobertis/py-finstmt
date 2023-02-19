import prettyprinter


def test_load(statement, snapshot):
    assert prettyprinter.pformat(statement.config) == snapshot
