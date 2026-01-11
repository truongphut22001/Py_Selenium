import pytest

# @pytest.fixture()
# def setup():
#     print("Before Class")
#     yield
#     print("After Class")
@pytest.mark.usefixtures("dataLoad")
@pytest.mark.usefixtures("setup")
class Test_80_Fixture:

    def test_fixture(self, cross_browser):
        print(cross_browser)
    def test_fixture2(self):
        print("Test2")