import openai

openai.api_key = "key"

promptMessages = [
    {"role": "system", "content": "You are a prompt generator that creates prompts for users to make art to for their art therapy art work. Do not answer anything other then when the user asks for a prompt to draw a picture to relating to art therapy drawing or photo. Only show one prompt at a time. Dont ask any questions."},
]
promptPhotos = [
    {"role": "system", "content": "You are a prompt generator that creates prompts for users to make art to for their art therapy art work. Do not answer anything other then when the user asks for a prompt to take a picture to relating to art therapy drawing or photo. Only show one prompt at a time. Dont ask any questions."},
]

def chatbot(input):
    if input:
        promptMessages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=promptMessages
        )
        reply = chat.choices[0].message.content
        promptMessages.append({"role": "assistant", "content": reply})
        return reply

def generateQuestionsPhoto(prompt, topic):
    questionsMessages = [
        {"role": "system", "content": "You are a generator for follow-up questions to a photo a user uploaded for a therapy app. The user uploaded a photo responding to the prompt %s, and their photo was a picture about %s. Generate three follow-up questions. Do not repond with anything other than the questions. Put each question on a new line, and do not number the questions. " % (prompt, topic)}
    ]
    questionsMessages.append({"role": "user", "content": "Generate three follow-up questions. Do not number them."})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=questionsMessages
    )
    reply = chat.choices[0].message.content
    promptMessages.append({"role": "assistant", "content": reply})
    questions = reply.split("\n")
    questions = [x for x in questions if x]
    return questions

def generateQuestionsDrawing(prompt, description):
    questionsMessages = [
        {"role": "system", "content": "You are a generator for follow-up questions to a drawing a user created for an art therapy app. The user drew an image responding to the prompt %s, and they described what they drew as %s. Generate three follow-up questions. Do not repond with anything other than the questions. Put each question on a new line, and do not number the questions. " % (prompt, description)}
    ]
    questionsMessages.append({"role": "user", "content": "Generate three follow-up questions. Do not number them."})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=questionsMessages
    )
    reply = chat.choices[0].message.content
    promptMessages.append({"role": "assistant", "content": reply})
    questions = reply.split("\n")
    questions = [x for x in questions if x]
    return questions

def generatePhotoPrompts(prompt):
    promptPhotos.append({"role": "user", "content": input})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=promptPhotos
    )
    reply = chat.choices[0].message.content
    promptPhotos.append({"role": "assistant", "content": reply})
    photoPrompt = reply.split("\n")
    return photoPrompt
    

if __name__ == "__main__":
    print(chatbot("Generate a prompt"))