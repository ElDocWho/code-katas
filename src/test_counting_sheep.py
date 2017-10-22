"""

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];
              
test.assert_equals(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))"""
import pytest

@pytest.mark.parametrize('arrayOfSheeps', ([True, False], 1))
def count_sheeps(arrayOfSheeps):
    from counting_sheep import count_sheeps
   