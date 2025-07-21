import random

SKILLS = {
    "FieldAgent": {
        "low": ["Экстремальное вождение", "Взлом", "Планирование"],
        "middle": ["Диверсия", "Слежка"],
        "high": ["Операции под прикрытием"]
    },
    "AnalystAgent": {
        "low": ["Excel", "Исследование"],
        "middle": ["SQL", "Python", "Визуализация данных"],
        "high": ["Аналитика", "Моделирование угроз", "Стратегическое планирование"]
    },
    "SpyAgent": {
        "low": ["Наблюдение", "Уход от слежки"],
        "middle": ["Внедрение", "Социальная инженерия"],
        "high": ["Манипуляции", "Допрос под прикрытием"]
    }
}

def assign_skills(agent_type: str, age: int) -> list:
    pool = SKILLS.get(agent_type)
    if not pool:
        return []
    result = []

    if age <= 25:
        result.append(random.choice(pool["low"]))
    elif 26 <= age <= 45:
        result.append(random.choice(pool["middle"]))
        result.append(random.choice(pool["high"]))
    elif age >= 46:
        result.append(random.choice(pool["low"]))
        result.append(random.choice(pool["middle"]))
        result.append(random.choice(pool["high"]))
    return result