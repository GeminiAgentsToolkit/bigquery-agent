import vertexai
#from config import (PROJECT_ID, REGION, SIMPLE_MODEL)
from gemini_agents_toolkit import agent


def say_to_duck(say: str):
    """say something to a duck"""
    return f"duck answer is: duck duck {say} duck duck duck"


vertexai.init(project='trim-field-444020-g8', location='us-west1')

all_functions = [say_to_duck]
duck_comms_agent = agent.create_agent_from_functions_list(functions=all_functions,
                                                          model_name='gemini-1.5-flash-002')

print(duck_comms_agent.send_message("say to the duck message: I am hungry"))