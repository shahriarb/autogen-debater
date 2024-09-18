import playsound
from openai import OpenAI

client = OpenAI()

def generate_audio(file_name, transcript, voice):
    try:
        # Generate audio using OpenAI's TTS
        audio_response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=transcript,
            response_format="mp3"
        )

        # Save the chunk audio to a temporary file
        output_audio_path = f"{file_name}.mp3"
        with open(output_audio_path, "wb") as f:
            f.write(audio_response.content)
        return output_audio_path
    except Exception as e:
        print(f"Error generating audio for chunk : {e}")

def generate_all_audios(debate_title, messages, debater1_name, voice1, debater2_name, voice2):
    result = []
    for idx, message in enumerate(messages):
        if idx == 0:
            continue
        sender = message.get("name", "Unknown").lower()
        content = message.get("content", "")
        if content.strip().lower() == sender:
            continue
        voice = "alloy"
        if sender == "moderator":
            voice="onyx"
        elif sender == debater1_name.lower():
            voice=voice1
        elif sender == debater2_name.lower():
            voice=voice2
        print(f"Generating the voice for {sender}({voice}):{content}")
        audio_file = generate_audio(f"{debate_title}_{idx}_{sender.lower()}", content, voice=voice)
        result.append({"sender": sender, "content": content, "audio_file": audio_file})

    print("\n\n==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("======= FULL DEBATE TRANSCRIPT ===\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    print("==================================\n")
    for item in result:
        sender = item["sender"]
        content = item["content"]
        audio_file = item["audio_file"]
        print(f"\n---->{sender}<----------:\n{content}\n{'-'*50}")
        playsound.playsound(audio_file, True)

    return result
