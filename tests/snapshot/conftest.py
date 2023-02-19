import prettyprinter
import pytest
from syrupy import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension, WriteMode

prettyprinter.install_extras(include=["dataclasses"])


class SingleFileTextSnapshotExtension(SingleFileSnapshotExtension):
    _write_mode = WriteMode.TEXT
    _file_extension = "txt"


@pytest.fixture
def snapshot(snapshot: SnapshotAssertion):
    return snapshot.use_extension(SingleFileTextSnapshotExtension)
