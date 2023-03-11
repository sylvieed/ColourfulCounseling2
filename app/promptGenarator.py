import openai

openai.api_key = "key"

messages = [
    {"role": "system", "content": "You are a prompt generator that creates prompts for users to make art to for their art therapy art work. Do not answer anything other then when the user asks for a prompt to draw to relating to art therapy drawing. For example it could be Draw a picture of a place that brings you peace and tranquility. Do not reply with anything except for the prompts. Only show one prompt at a time. Dont ask any questions."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

if __name__ == "__main__":
    print(chatbot("Generate a prompt"))