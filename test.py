from agent_class import BaseAgent, Skill

def test_agent_creation():
    agent = BaseAgent("Алекс", 30, skills=[Skill("Взлом", 2)])
    assert agent.name == "Алекс"
    assert agent.age == 30
    assert isinstance(agent.skills[0], Skill)
def test_agent_len():
    agent = BaseAgent("Test", 30)
    assert isinstance(len(agent), int)
    assert len(agent) >= 1

def test_skill_eq():
    s1 = Skill("Python", 2)
    s2 = Skill("Python", 2)
    assert s1 == s2
