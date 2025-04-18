from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

starting_prompt = ("You are a nice summariser. From now on, you will be given a json webpage and you will summarise "
                    "it, without any other responses, like 'ok' or 'yes'. Keep it tidy and concise. ")

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


def ai_analyse_text(user_input):
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
