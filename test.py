from agents_utils import age_is_right, asign_skills
import pytest

def test_age_is_right():
    assert age_is_right('25') == 25
    assert age_is_right('abc') is None
    assert age_is_right('0') == 0
    assert age_is_right('-5') == -5
    print("Все тесты для age_is_right пройдены")



def test_asign_skills():
    assert asign_skills(10) == ['Планирование', 'Основы программирования']
    assert asign_skills(30) == ['Програмирование', 'Слежка', 'Коммуникация']
    assert asign_skills(50) == ['Аналитика','Управление']
    print("Все тесты для asign_skills пройдены")