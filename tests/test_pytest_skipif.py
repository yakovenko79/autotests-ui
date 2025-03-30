import pytest

SYSTEM_VERSION = 'v1.2.0'


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason="Test cant be executed on version v1.3.0"
)
def test_system_version_valid():
    ...


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="Test cant be executed on version v1.2.0"
)
def test_system_version_invalid():
    ...
