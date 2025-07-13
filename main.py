from agent_class import Agent
import json

def main():
    name = input("Enter name:")
    age = int(input("Enter age:"))

    agent = Agent(name, age, skills=["stealth", "hacking"])
    print(agent)

    with open("agents.json", "a", encoding="utf-8") as f:
        json.dump(agent.to_dict(), f)
        f.write("\n")

if __name__ == "__main__":
    main()
