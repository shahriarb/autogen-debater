import autogen
import os

def create_moderator_agent():
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
        name="Moderator",
        system_message="""You are the debate moderator.
        If it is the start of the chat introduce the debate topic and the debaters and ask them to start.
        Do nothing after first exchange.
        Do nothing after second exchange.
        Do nothing after third exchange.
        Ask probing questions from the first debater after forth exchange.
        Ask probing questions from the second debater after the first debater response to your probing question.
        After second debater answered your probing question, Conclude the debate and declare a winner based on the strength of arguments presented and TERMINATE the debate. """,
        human_input_mode="NEVER",
        silent=True
    )


def create_short_moderator_agent():
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
        name="Moderator",
        system_message="""You are the debate moderator.
        If it is the start of the chat introduce the debate topic and the debaters and ask them to start.
        Do nothing after first exchange.
        After second exchange, Conclude the debate and declare a winner based on the strength of arguments presented and TERMINATE the debate. """,
        human_input_mode="NEVER",
        silent=True
    )
