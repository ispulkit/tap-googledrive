"""Stream type classes for tap-googledrive."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_googledrive.client import googledriveStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class FilesStream(googledriveStream):
    """Define custom stream."""

    name = "files"
    path = "/files"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("files",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.StringType), 
                            th.Property("name", th.StringType), 
                            th.Property("mimeType", th.StringType)))),
    ).to_dict()
