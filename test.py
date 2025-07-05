from agents_utils import age_is_right
import pytest

def test_age_is_right():
    assert age_is_right('25') == 25
    assert age_is_right('abc') is None
    assert age_is_right('0') == 0
    assert age_is_right('-5') == -5
    print("Все тесты для age_is_right пройдены")

from agents_utils import save_agent_card

test_agent = {
    "name": "Testov",
    "age": 25,
    "skills": ["Слежка", "Коммуникация"]
}

save_agent_card(test_agent)