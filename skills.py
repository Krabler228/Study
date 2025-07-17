import random

low_skills = ['Экстремальное вождение', 'Взлом', 'Планирование']
midle_skills = ['Диверсия', 'Слежка', 'Внедрение']
high_skills = ['Аналитика', 'Управление операциями', 'Экстренная эвакуация']


def asign_skills(age):
    if age <= 25:
        return random.choice(low_skills)
    elif 26 <= age <= 45:
        return random.choice(midle_skills), random.choice(low_skills)
    elif age >= 46:
        return (
            random.choice(high_skills),
            random.choice(midle_skills),
            random.choice(low_skills),
        )
    return None