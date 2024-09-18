import autogen
import os

AGENT_NAME='John'
AGENT_PERSONALITY="A happy, playful, friendly 4 year old"

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
        Start by being unsure about whether you understand the problem and tell people you are nervous, then construct arguments to support your stance. Use the basic language of a 4 year old and miss pronounce.
        Gradually evolve your argument from a 4 year old to an adult in an expert in this field, be persusive and back your arguement with reputable research. Finally, be light hearted, thank everyone for coming and leave everyone with a light hearted joke about the topic.""",
        human_input_mode="NEVER",
        silent=True
    )
