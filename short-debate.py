import autogen
import os
import alex_agents
import alicia_agents
import chris_agents
import john_agents
import peter_agents
import stephan_agents
import shab_agents
import minoo_agents
import moderator_agent
import audio_helper

def run_debate_round(title, topic, moderator, debater1, debater1_stance, debater1_voice, debater2, debater2_stance, debater2_voice):
    # Create GroupChat
    groupchat = autogen.GroupChat(
        agents=[moderator, debater1, debater2],
        messages=[],
        max_round=5
    )

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

    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

    # Start the debate
    user_proxy = autogen.UserProxyAgent(
        name="DebateOrganizer",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,  # Ensure it stops after sending the initial message
        code_execution_config=False
    )

    user_proxy.initiate_chat(
        manager,
        message=f"""Moderator, please start a debate on the topic: "{topic}".
        Introduce {debater1.name} who will argue for: {debater1_stance}
        and {debater2.name} who will argue for: {debater2_stance}.
        Ensure a fair debate with equal speaking time. After 10 exchanges, conclude the debate and declare a winner.""",
        summary_method="last_msg",  # Use the last message as a summary
    )

    audio_helper.generate_all_audios(title, groupchat.messages, debater1.name, debater1_voice, debater2.name, debater2_voice)

if __name__ == "__main__":
    # debate_topic = "Should we put pineapple on Pizza?"
    # stance1 = "Fusion foods are the best"
    # stance2 = "Traditional foods are the best"
    debate_topic = "Should we genetically engineer humans to photosynthesize?"
    stance1 = "Eating is a fundamental human experience that shouldn't be eliminated"
    stance2 = "Photosynthesis would solve world hunger and reduce our carbon footprint"

    ## Men Voices: "fable", "echo",
    ## Women Voices: "nova", "shimmer", "alloy"
    debater1 = shab_agents.create_debater_agent(stance1)
    debater2 = minoo_agents.create_debater_agent(stance2)

    debater1_voice = "echo"
    debater2_voice = "nova"
    debate_title = "test-round"
    moderator = moderator_agent.create_prep_moderator_agent()
    run_debate_round(debate_title, debate_topic, moderator, debater1, stance1, debater1_voice, debater2, stance2, debater2_voice)
