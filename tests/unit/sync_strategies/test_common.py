import pytest

from tap_mssql.sync_strategies.common import escape


@pytest.mark.parametrize(
    "value, expected",
    [
        ("simple_identifier", "[simple_identifier]"),
        ("\"simple\"_identifier", "[\"simple\"_identifier]"),
        ("'simple'_identifier", "['simple'_identifier]"),
        ("`simple`_identifier", "[`simple`_identifier]"),
        ("[simple]_identifier", "[[simple]]_identifier]"),
    ],
)
def test_escape(value: str, expected: str) -> None:
    ### act
    actual = escape(value)

    ### assert
    assert actual == expected
