#This project utilizes the GPT library provided by OpenAI (https://openai.com) 
#for generating AI responses. The AI responses are generated using the OpenAI GPT-3.5 model. 
# Please note that the AI responses are powered by OpenAI GPT-3.5 and not by my custom AI model, 
# which is currently under development.

import openai
import os

openai.api_key = '<gpt api key goes here>'


while True:
    user_input = input("==User=> ")
    if user_input.lower() == 'quit':
        break
    elif user_input.lower() == 'clear':
        os.system('clear')
    prompt = f'without commentary please type out a bash script that will {user_input}\n'
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
