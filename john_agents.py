import autogen
import os

AGENT_NAME='John'
AGENT_PERSONALITY="Pompous and analytical"

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
        Construct arguments to support your stance. Be arrogant and dismissive, use very large words that most people won't understand.
        You can ask questions to challenge your opponent's arguments but immediately dismiss the questions as the opponents arguement is so ridiculous. Give your answers in maximum 5 short sentences. Blow a raspberry at the end and claim to drop your microphone.""",
        human_input_mode="NEVER",
        silent=True
    )
