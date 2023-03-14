import prettyprinter


def test_load(statement, snapshot):
    # print("######### STATEMENT ######")
    # print(prettyprinter.pformat(statement))
    
    # with open('output.txt', 'wt') as out:
    #     print(prettyprinter.pformat(statement), file=out)

    # print("######### SNAPSHOT ######")
    # print(snapshot)
    assert prettyprinter.pformat(statement) == snapshot
