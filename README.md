# AutoGen Debater

AI Agents debating each others :)

## Install
Python version >= 3.8, < 3.13

python -m venv debater

source debater/bin/activate

pip install -r requirements.txt

export OPENAI_API_KEY=<REPLACE WITH YOUR KEY>

## Running Short Debate
In the Fast debaste each dabater will have one chance to presents their argument.

Set your debate topic, debaters and their stance in the fast-debate.py. You can also choose their voice.
```
    debate_topic = "Should we put pineapple on Pizza?"
    stance1 = "Fusion foods are the best"
    stance2 = "Traditional foods are the best"

    ## Men Voices: "fable", "echo",
    ## Women Voices: "nova", "shimmer", "alloy"
    debater1 = shab_agents.create_debater_agent(stance1)
    debater2 = minoo_agents.create_debater_agent(stance2)

    debater1_voice = "echo"
    debater2_voice = "nova"
    debate_title = "test-round"
    moderator = moderator_agent.create_prep_moderator_agent()
    run_debate_round(debate_title, debate_topic, moderator, debater1, stance1, debater1_voice, debater2, stance2, debater2_voice)
```

python short-debate.py

## Running Debate
In this debate, debaters will have at two exchanges and moderator will ask a question as well.

Set your debate topic, debaters and their stance in the debate.py. You can also choose their voice.
```
    debate_topic = "Should we leave the cities and go back to the nature?"
    stance1 = "I like urban areas"
    stance2 = "I like contryside"

    ## Men Voices: "fable", "echo",
    ## Women Voices: "nova", "shimmer", "alloy"
    debater1 = shab_agents.create_debater_agent(stance1)
    debater2 = minoo_agents.create_debater_agent(stance2)

    debater1_voice = "echo"
    debater2_voice = "nova"
    debate_title = "round1"

```

python debate.py

## Voice samples

Application is using OpenAI tts APIs to generate voices.
To see the samples check [Voice Options](https://platform.openai.com/docs/guides/text-to-speech/voice-options)

Note: `Onyx` is reserved for moderators.
