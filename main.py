from agent_class import Agent, Skill
import json

def main():
    name = input("Enter name: ")
    age = int(input("Enter age: "))


    skills = [Skill("stealth", 1), Skill("hacking", 2)]


    agent = Agent(name, age, skills=skills)


    print(agent)


    with open("agents.json", "a", encoding="utf-8") as f:
        json.dump(agent.to_dict(), f, ensure_ascii=False)
        f.write("\n")

if __name__ == "__main__":
    main()
