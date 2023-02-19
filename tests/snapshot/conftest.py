from typing import Optional

import prettyprinter
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

prettyprinter.install_extras(include=["dataclasses"])


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
        print("Serializing with", exclude)
        return AmberDataSerializer.serialize(data, exclude=exclude, matcher=matcher)


@pytest.fixture
def snapshot(snapshot: SnapshotAssertion):
    return snapshot.use_extension(SingleFileTextSnapshotExtension)
