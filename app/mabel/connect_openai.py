from dotenv import load_dotenv
import openai
import os
import json
#load_dotenv()
openai.api_key=os.getenv('OPENAI_KEY')

SYSTEM_DIRECTIVES = []
DIALOGUE_STACK = []

def load_system_directives():
    '''Load the json file containing system directives'''
    with open('app/mabel/system-directives/system_directives.json') as f:
        system_directives = json.load(f)
    return system_directives

def chatgpt_response(prompt):
    global DIALOGUE_STACK, SYSTEM_DIRECTIVES
    SYSTEM_DIRECTIVES = load_system_directives()
    current_prompt = {"role": "user", "content": prompt}
    DIALOGUE_STACK.append(current_prompt)
    DIALOGUE_STACK = DIALOGUE_STACK[-6:]
    messages = SYSTEM_DIRECTIVES + DIALOGUE_STACK

    if "mabel" in prompt.lower() or "Mabel" in prompt.lower():
        response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1800,
        )
        DIALOGUE_STACK.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        return response ['choices'][0]['message']['content']
    else:
        DIALOGUE_STACK.append({"role": "user", "content": prompt})