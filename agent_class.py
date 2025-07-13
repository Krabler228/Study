import uuid
import datetime

class Agent:
    def __init__(self, name: str, age: int, skills=None):
        self.name = name
        self.age = age
        self.skills = skills or []
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "skills": self.skills,
            "id": self.id,
            "created_at": self.created_at
        }

    def __str__(self):
        return f"Agent({self.name}, {self.age}y, skills {self.skills})"