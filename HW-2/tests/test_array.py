
import pytest

from main import Array

@pytest.mark.parametrize("input_lst, expected_result",
                         [
                             ((1,2,3),6),
                             ((0,0,0),0),
                             ((-1,-2,-6),-9),
                         ])

def test_sum_positive(input_lst, expected_result):
    arr = Array(*input_lst)
    assert arr.sum() == expected_result

@pytest.mark.parametrize("input_lst, expected_result",
                         [
                             (("a","b",3),TypeError),
                             ((),ValueError)
                         ])

def test_sum_negative(input_lst, expected_result):
    arr = Array(*input_lst)
    with pytest.raises(expected_result):
        arr.sum()



@pytest.mark.parametrize("input_lst, expected_result",
                         [
                             ((1,2,3),6),
                             ((0,0,0),0),
                             ((-1,-2,-6),-12)
                         ])

def test_multiply_positive(input_lst, expected_result):
    arr = Array(*input_lst)
    assert arr.multiply() == expected_result

@pytest.mark.parametrize("input_lst, expected_result",
                         [
                             (("a","b",3),TypeError),
                             ((),ValueError)
                         ])

def test_multiply_negative(input_lst, expected_result):
    arr = Array(*input_lst)
    with pytest.raises(expected_result):
        arr.multiply()


@pytest.mark.parametrize("input_lst, expected_result",
                         [
                             ((1,2,3),2),
                             ((0,0,0),0),
                             ((-1,-2,-6),-3),
                         ])

def test_average_positive(input_lst, expected_result):
    arr = Array(*input_lst)
    assert arr.average() == expected_result

@pytest.mark.parametrize("input_lst, expected_result",
                         [
                             (("a","b",3),TypeError),
                             ((),ValueError)
                         ])

def test_average_negative(input_lst, expected_result):
    arr = Array(*input_lst)
    with pytest.raises(expected_result):
        arr.average()
