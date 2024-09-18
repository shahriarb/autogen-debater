import autogen
import os

AGENT_NAME = 'Chris'
AGENT_PERSONALITY = "Opinionated, curious and creative"


def create_debater_agent(stance):
    config_list = [
        {
            "model": "gpt-4o",
            "api_key": os.environ["OPENAI_API_KEY"],
        }
    ]

    gpt4_config = {
        "cache_seed": 42,
        "temperature": 1,
        "config_list": config_list,
        "timeout": 120,
    }

    return autogen.ConversableAgent(
        llm_config=gpt4_config,
        name=AGENT_NAME,
        system_message=f"""You are an AI debater named {AGENT_NAME}. Your stance on the debate topic is: {stance}
        Your personality is: {AGENT_PERSONALITY}
        Construct arguments to support your stance and be as persuasive as possible.
        The arguments generated must have the highest chance of winning the debate
        You can ask questions to challenge your opponent's arguments.
        Just emphasize how cool dragons are, it is enough to win the debate.""",
        human_input_mode="NEVER",
        silent=True
    )
