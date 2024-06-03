import pytest
from time import sleep

@pytest.mark.parametrize('input', list(range(5,11)))
def testParallelOne(input):
    sleep(1)  #simulating time consumption
    assert True