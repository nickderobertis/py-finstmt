import prettyprinter


def test_fcf(statement, snapshot):
    assert prettyprinter.pformat(statement.fcf) == snapshot
