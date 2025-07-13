import json
import os
import uuid
from datetime import datetime
import random

low_skills = ['Экстремальное вождение', 'Взлом', 'Планирование']
midle_skills = ['Диверсия', 'Слежка', 'Внедрение']
high_skills = ['Аналитика', 'Управление операциями', 'Экстренная эвакуация']

def age_is_right(user_age)-> int:
    try:
        user_age = int(user_age)
        return user_age
    except ValueError:
        print('Invalid age')
        return None


def true_age(validated_age, user_name):
    if 11 <= validated_age <= 14:
        return (f"Агент {user_name} тебе {validated_age} лет")
    elif validated_age % 10 == 1 and validated_age % 100 != 11:
        return (f"Агент {user_name} тебе {validated_age} год")
    elif validated_age % 10 in (2, 3, 4) and not 12 <= validated_age % 100 <= 14:
        return (f"Агент {user_name} тебе {validated_age} года")
    else:
        return (f"Агент {user_name} тебе {validated_age} лет")


def is_agent_ready(validated_age, user_name):
    if validated_age < 7:
        return (f"Агент {user_name} слишком мал для обучения")
    elif validated_age >= 7 and validated_age <= 18:
        return (f" Агент {user_name} пока что молод для работы но способен учится")
    elif validated_age >= 18 and validated_age <= 65:
        return (f"Агент {user_name} готов к работе")
    elif validated_age >= 65:
        return (f" Агент {user_name} последний понедельник доживает")
    return None


def asign_skills(validated_age):
    if validated_age < 18:
        return random.choice(low_skills)
    elif validated_age >= 18 and validated_age <= 40:
        return random.choice(midle_skills), random.choice(low_skills)
    elif validated_age >= 40:
        return random.choice(high_skills), random.choice(midle_skills), random.choice(low_skills)


def agent_card(validated_age, user_name, asign_skills):
    skills = asign_skills(validated_age)
    agent = {
        'id': str(uuid.uuid4()),
        'name': user_name,
        'age': validated_age,
        'skills': skills,
        'ragistration date': datetime.now().isoformat(),
    }
    return agent

def print_agent(agent):
    print(f"Агент {agent['name']}")
    print(f"Возраст: {agent['age']}")
    print("Навыки:")
    for skill in agent["skills"]:
        print(f" - {skill}")

def save_agent_card(agent: dict, filename="agents.json"):
    agents_list = []

    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                agents_list = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Файл повреждён или пустой. Создаю новый список.")

    agents_list.append(agent)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(agents_list, file, ensure_ascii=False, indent=4)

    print(f"Агент {agent['name']} сохранён в {filename}")






