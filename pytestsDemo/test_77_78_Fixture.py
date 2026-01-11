import pytest

# @pytest.fixture()
# def setup():
#     print("Before Class")
#     yield
#     print("After Class")
@pytest.mark.usefixtures("setup")
class Test_77_Fixture:

    def test_fixture(self):
        print("L77. Fixture")
    def test_fixture1(self):
        print("L77. Fixture1")
    def test_fixture2(self):
        print("L77. Fixture2")
    def test_fixture3(self):
        print("L77. Fixture3")
    def test_fixture4(self):
        print("L77. Fixture4")