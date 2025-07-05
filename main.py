import os

from agents_utils import age_is_right, true_age, is_agent_ready, asign_skills, agent_card, print_agent, save_agent_card

if __name__ == "__main__":
    user_name = input('Enter your name: ')
    user_age = input('Enter your age: ')
    validated_age = age_is_right(user_age)

    if validated_age is not None:
        print(true_age(validated_age, user_name))
        print(is_agent_ready(validated_age, user_name))
        print(asign_skills(validated_age))

        agent = agent_card(validated_age, user_name, asign_skills)
        print_agent(agent)
        print(os.getcwd())
        save_agent_card(agent)
