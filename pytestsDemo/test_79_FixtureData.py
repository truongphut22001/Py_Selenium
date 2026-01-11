import pytest

# @pytest.fixture()
# def setup():
#     print("Before Class")
#     yield
#     print("After Class")
@pytest.mark.usefixtures("dataLoad")
@pytest.mark.usefixtures("setup")
class Test_79_Fixture:

    def test_fixture(self, dataLoad):
        print(dataLoad)
    def test_fixture2(self):
        print("Test2")