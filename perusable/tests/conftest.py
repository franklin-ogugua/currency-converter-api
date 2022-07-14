import pytest
from starlette.testclient import TestClient

from converter.config import Settings, get_settings
from converter.main import create_application


def get_settings_override():
    """
    Overides the default settings
    """
    return Settings(testing=1)


@pytest.fixture(scope="module")
def test_app():
    """
    Test set up
    """
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client
