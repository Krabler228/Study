import uuid
import datetime
from skills import assign_skills


class Skill:
    __slots__ = ['skill', 'lvl']
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
    @classmethod
    def from_dict(cls, data):
        return cls(skill=data["skill"], lvl=data["lvl"])
    def lvl_up(self):
        self.lvl += 1
    def __eq__(self, other):
        return isinstance(other, Skill) and self.skill == other.skill and self.lvl == other.lvl

class BaseAgent:
    __slots__ = [
        '_name', '_age',
        '_BaseAgent__skills',
        '_BaseAgent__id',
        '_BaseAgent__created_at'
    ]
    def __init__(self, name: str, age: int, skills: list[Skill] = None):
        self._name = name
        self._age = age

        if skills is not None:
            self.__skills = skills
        else:
            raw_skills = assign_skills(self.__class__.__name__, age)
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
    def __eq__(self, other):
        return isinstance(other, BaseAgent) and self._name == other._name and self._age == other._age

    @property
    def skills(self):
        return self.__skills

    def __len__(self):
        return len(self.__skills)

    def same_skills(self, other):
        return self.__skills == other.__skills

    def add_skill(self, skill: Skill):
        self.__skills.append(skill)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "skills": [skill.to_dict() for skill in self.__skills],
            "id": self.__id,
            "created_at": self.__created_at,
            "agent_type": self.__class__.__name__
        }
    @classmethod
    def from_dict(cls, data: dict):
        skills = [Skill.from_dict(s) for s in data["skills"]]
        return cls(
            name=data["name"],
            age=data["age"],
            skills= skills
        )

    def __str__(self):
        skill_list = ", ".join(str(skill) for skill in self.__skills)
        return f"Agent({self.name}, {self.age}y, skills: [{skill_list}])"

class FieldAgent(BaseAgent):
    def __init__(self, name: str, age: int, skills: list[Skill] = None):
        super().__init__(name, age, skills)
class AnalystAgent(BaseAgent):
    def __init__(self, name: str, age: int, skills: list[Skill] = None):
        super().__init__(name, age, skills)
class SpyAgent(BaseAgent):
    def __init__(self, name: str, age: int, skills: list[Skill] = None):
        super().__init__(name, age, skills)
