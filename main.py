

from agent_class import FieldAgent, AnalystAgent, SpyAgent
import json

AGENT_TYPES = {
    "field": FieldAgent,
    "analyst": AnalystAgent,
    "spy": SpyAgent,
}

def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))


    agent_type_key = input("Выберите и введите класс агента из доступных классов (field/ analyst/ spy:").strip().lower()
    AgentClass = AGENT_TYPES.get(agent_type_key)
    if AgentClass is None:
        print("Ошибка!")
    else:
        agent = AgentClass(name, age)


    print(agent)

    with open("agents.json", "a", encoding="utf-8") as f:
        json.dump(agent.to_dict(), f, ensure_ascii=False, indent=4)
        f.write("\n")

if __name__ == "__main__":
    main()
