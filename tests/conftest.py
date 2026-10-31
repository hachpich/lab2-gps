import pytest

@pytest.fixture(scope="session")
def valid_coords() -> list[str]:
    return [
        "55.7558, 37.6173",
        "-33.8688, 151.2093",
        "0.0, 0.0",
        "-90.0, -180.0",
        "90.0, 180.0",
        "12.34, -56.78",
    ]

@pytest.fixture(scope="session")
def invalid_coords() -> list[str]:
    return [
        "",
        "55.7558 37.6173",
        "91.0, 37.6173",
        "-91.0, 37.6173",
        "55.7558, 181.0",
        "55.7558, -181.0",
        "55, 37",
        "abc, def",
    ]