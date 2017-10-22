'''Test.expect(bool_to_word(True), 'Yes')
Test.expect(bool_to_word(False), 'No')'''

import pytest

@pytest.mark.parametrize('bool', (True, 'yes'))
def bool_to_word(bool):
    from convert_boolean import bool_to_word
    assert True == 'yes'
