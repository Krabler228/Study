import uuid
import datetime
from skills import asign_skills


class Skill:
    def __init__(self, skill: str, lvl: int = 1):
        self.skill = skill
        self.lvl = lvl

    def __str__(self):
        return f"{self.skill} lvl({self.lvl})"

    def to_dict(self):
        return {
            "skill": self.skill,
            "lvl": self.lvl
        }

    def lvl_up(self):
        self.lvl += 1


class Agent:
    def __init__(self, name: str, age: int, skills: list[Skill] = None):
        self._name = name
        self._age = age

        if skills is not None:
            self.__skills = skills
        else:
            raw_skills = asign_skills(age)
            if isinstance(raw_skills, str):
                raw_skills = [raw_skills]
            self.__skills = [Skill(s) for s in raw_skills]

        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.datetime.now().isoformat()

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if 18 <= value <= 65:
            self._age = value
        else:
            raise ValueError("Возраст должен быть от 18 до 65 лет")

    @property
    def skills(self):
        return self.__skills

    def add_skill(self, skill: Skill):
        self.__skills.append(skill)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "skills": [skill.to_dict() for skill in self.__skills],
            "id": self.__id,
            "created_at": self.__created_at
        }

    def __str__(self):
        skill_list = ", ".join(str(skill) for skill in self.__skills)
        return f"Agent({self.name}, {self.age}y, skills: [{skill_list}])"