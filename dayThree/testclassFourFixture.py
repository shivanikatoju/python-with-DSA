import pytest

# @pytest.fixture(scope='function')
# def data():
#     return [10,20,30,40,50]

class TestClassOne:
    def testOne(self, data):
        print(f'\n in testOne() with {data}')
        assert True
    
    def testTwo(self, data):
        print(f'\n in testTwo() with {data}')
        assert True

    def testThree(self, data):
        total = sum(data)
        assert total == 150
    
    def testSix(self, data):
        data[0] = 8
        print(f'in six {data}')
        assert True
    
    def testFour(self, data):
        assert data == [10,20,30,40,50]

    def testFive(self, data):
        length = len(data)
        assert length == 5

    