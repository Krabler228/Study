from agent_class import Agent, Skill

def test_agent_creation():
    agent = Agent("Алекс", 30, skills=[Skill("Взлом", 2)])
    assert agent.name == "Алекс"
    assert agent.age == 30
    assert isinstance(agent.skills[0], Skill)
