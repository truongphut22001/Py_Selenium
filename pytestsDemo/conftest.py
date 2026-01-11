import pytest


@pytest.fixture(scope="class")
def setup():
    print("Before Class")
    yield
    print("After Class")

@pytest.fixture()
def dataLoad():
    print("Data Parameter")
    return ["PHU", "Truong", "TEST"]

@pytest.fixture(params=[("chrome","PHU1","vip"),
                        ("firefox","PHu2","vip2"),
                        ("IE", "phu3", "vip3")])
def cross_browser(request):
    return request.param