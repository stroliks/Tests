
from main import average

import pytest


@pytest.mark.parametrize("lst, expected_result",
                         [
                             ([1,2,3,4,5], 3),
                             ([1,2,3], 2),
                             ([-1, -2, -3], -2),
                             ([-1.4,-1.1,-1.1],-1.2),
                             ([1.4,1.1,1.1],1.2),
                             ([1,2,1],1.33),
                         ])

def test_average_positive(lst, expected_result):
    assert average(lst) == expected_result


@pytest.mark.parametrize("lst, expected_result",
                             [
                                 (["a","v",3,4], TypeError),
                                 ([], ValueError),
                                 ("", ValueError),
                                 (0, ValueError),
                                 (None, ValueError)
                             ])
def test_average_negative(lst, expected_result):
    with pytest.raises(expected_result):
        average(lst)


@pytest.mark.parametrize("lst, expected_result",
                             [
                                 ([0, 0, 0], 0),
                                 ([-1, -2, 3], 0),
                                 ([-1], -1),
                             ])

def test_average_bound(lst, expected_result):
        assert average(lst) == expected_result

