# -k "Greet": choose test case has "Greet" in name
import pytest


@pytest.mark.smoketest
@pytest.mark.xfail
def test_firstProgram():
    print("Hello")

@pytest.mark.skip
def test_Greet():
    print("Hello")