import prettyprinter


def test_load(statement, snapshot):
    with open('output.txt', 'wt') as out:
        print(prettyprinter.pformat(statement.config), file=out)
    assert prettyprinter.pformat(statement.config) == snapshot
