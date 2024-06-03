import pytest

@pytest.fixture
def someFunction():
    print('\nSetup: for Initialization process')
    yield
    print(f'\nTearDown: for clearing up resources')

def testTrue(someFunction):
    print('#1. My test Functions: Performing testing')
    assert True

def testIsTrue(someFunction):
    print('#2. My test Functions: performing testing')
    assert True