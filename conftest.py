import pytest
from fixture.application import Applications

fixture = None

@pytest.fixture
def app(request):
    global fixture
    base_address = request.config.getoption("--base_address")
    if fixture is None:
        fixture = Applications(base_address=base_address)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--base_address", action="store", default="c:\\AddressBook\\AddressBook.exe")
