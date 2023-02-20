from typing import Optional

import pytest
from syrupy import SnapshotAssertion
from syrupy.extensions.amber import AmberDataSerializer
from syrupy.extensions.single_file import SingleFileSnapshotExtension, WriteMode
from syrupy.types import (
    PropertyFilter,
    PropertyMatcher,
    SerializableData,
    SerializedData,
)

from tests.snapshot.ext_prettyprinter.dataclasses import (
    install as install_custom_dataclass_prettyprinter_extension,
)

install_custom_dataclass_prettyprinter_extension()


class SingleFileTextSnapshotExtension(SingleFileSnapshotExtension):
    _write_mode = WriteMode.TEXT
    _file_extension = "txt"

    def serialize(
        self,
        data: "SerializableData",
        *,
        exclude: Optional["PropertyFilter"] = None,
        matcher: Optional["PropertyMatcher"] = None,
    ) -> "SerializedData":
        return AmberDataSerializer.serialize(data, exclude=exclude, matcher=matcher)


@pytest.fixture
def snapshot(snapshot: SnapshotAssertion):
    return snapshot.use_extension(SingleFileTextSnapshotExtension)
