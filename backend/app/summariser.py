from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

starting_prompt = ("You are a nice summariser. From now on, you will be given a text and you will expand it,"
                    "without any other responses, like 'ok' or 'yes'.")

client_messages = [{
                    "role": "developer",
                    "content": starting_prompt
                }]

def test_openai(user_input):

    client_messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=client_messages,
        temperature=0.7,
        max_tokens=500
    )

    assistant_reply = response.choices[0].message.content.strip()

    client_messages.append({"role": "assistant", "content": assistant_reply})
    
    return response.choices[0].message.content.strip()


def ai_summarise_text(text):
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.7,
        max_tokens=500
    )
    return completion.choices[0].message.content.strip()
