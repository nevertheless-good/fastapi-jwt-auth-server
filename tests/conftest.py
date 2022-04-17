import pytest
from fastapi.testclient import TestClient

import app.main as _main


@pytest.fixture(scope="session")
def app():
    return _main.app

@pytest.fixture(scope="session")
def client(app):
    return TestClient(app=app)