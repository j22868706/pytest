import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(num_one=1, num_two=4)
    assert result == 5
    # assert: is used when debugging code
    # test if a condition in the code returns True, if not, the program will raise an AssertionError

def test_divide():
    result = my_functions.divide(num_one=10, num_two=2)
    assert result == 5

def test_divide_zero():
    '''result = my_functions.divide(num_one=10, num_two=0)
    assert result == 0
    # will rasie ZeroDivisionError
    '''
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(num_one=10, num_two=0)