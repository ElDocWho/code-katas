"""test.assert_equals(Descending_Order(0), 0)
test.assert_equals(Descending_Order(15), 51)
test.assert_equals(Descending_Order(123456789), 987654321)"""
import pytest

@pytest.mark.parametrize('num', (123, 321))
def Descending_Order(num):
    from descending_order import Descending_Order
  