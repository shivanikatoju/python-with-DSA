import pytest

def fun():
    print('\nStatement #1 in fun()...')
    raise ExceptionGroup(
        "MY ERROR MESSAGE",
        [
            RuntimeError(),
            TypeError()
        ]
    )
    print('\nstatement #2...')

def testExceptionOne():
    with pytest.raises(ExceptionGroup) as excinfo:
        print('\n #1. Inside testExceptionOne before calling fun()...')
        fun()
        print('\n #2. Inside testExceptionOne After calling fun()...')
        assert excinfo.group_contains(RuntimeError)
        assert not excinfo.group_contains(TypeError)