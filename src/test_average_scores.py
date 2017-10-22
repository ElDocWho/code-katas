'''Test.describe("Basic tests")
Test.assert_equals(average([5, 78, 52, 900, 1]), 207)
Test.assert_equals(average([5, 25, 50, 75]), 39)
Test.assert_equals(average([2]), 2)
Test.assert_equals(average([1, 1, 1, 1, 9999]), 2001)
Test.assert_equals(average([0]), 0)'''

import pytest

@pytest.mark.parametrize('array', ([10,10,10], 10))
def average(array):
    from average_scores import average
    assert (10+10+10)/3 == 10
