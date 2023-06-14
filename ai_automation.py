import openai
import os

openai.api_key = '<openai api key>'


while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        break
    elif user_input.lower() == 'clear':
        os.system('clear')
    prompt = f'without comentary please type out a bash script that will {user_input}\n'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    ai_response = response.choices[0].text.strip()
    os.system(ai_response)
