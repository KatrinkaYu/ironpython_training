from model.group import Group
import pytest
from fixture.application import Applications
import os.path
import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=12.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

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

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("excel_"):
            testdata = load_from_excel(fixture[6:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_excel(file):
    testdata = []
    excel = Excel.ApplicationClass()
    excel.Visible = True
    workbook = excel.Workbooks.Open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % file))
    sheet = workbook.ActiveSheet
    for i in range(6):
        testdata.append(Group(name=sheet.Range["A%s" % (i+1)].Value2))
    excel.Quit()
    return testdata