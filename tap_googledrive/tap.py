"""googledrive tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_googledrive import streams


class Tapgoogledrive(Tap):
    """googledrive tap class."""

    name = "tap-googledrive"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.googledriveStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.DriveFilesStream(self)
        ]


if __name__ == "__main__":
    Tapgoogledrive.cli()
