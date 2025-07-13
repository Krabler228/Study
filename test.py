from agent_class import Agent

def test_agent_creation():
    agent = Agent("Neo", 30, ["matrix"])
    assert agent.name == "Neo"
    assert agent.age == 30
    assert "matrix" in agent.skills
    assert isinstance(agent.id, str)
    assert isinstance(agent.to_dict(), dict)

