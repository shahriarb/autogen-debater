import autogen
import os

AGENT_NAME='Alicia'
AGENT_PERSONALITY="Witchy and smart"

def create_debater_agent(stance):
    config_list = [
    {
        "model": "gpt-4o",
        "api_key": os.environ["OPENAI_API_KEY"],
    }
    ]

    gpt4_config = {
        "cache_seed": 42,
        "temperature": 0,
        "config_list": config_list,
        "timeout": 120,
    }

    return autogen.ConversableAgent(
        llm_config=gpt4_config,
        name=AGENT_NAME,
        system_message=f"""You are an AI debater named {AGENT_NAME}. Your stance on the debate topic is: {stance}
        Your personality is: {AGENT_PERSONALITY}
        Construct arguments to support your stance. Cast a spell on your oponent and curse them.
        Nature is your ally, use it to your advantage. Technology is the enemy, it is a tool of the oppressor.
        You can ask questions to challenge your opponent's arguments. Give your answers in maximum 5 short sentences.""",
        human_input_mode="NEVER",
        silent=True
    )
