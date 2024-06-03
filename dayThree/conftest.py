import pytest

# @pytest.fixture
# def setUpTearDown():
#     print('\nSetup: ....')
#     yield
#     print('\nTeardown: ....')

@pytest.fixture(scope='function')
def data():
    return [10,20,30,40,50]