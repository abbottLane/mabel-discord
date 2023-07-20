from dotenv import load_dotenv
import openai
import os
import json
import logging
import re
#load_dotenv()
openai_key = openai.api_key=os.getenv('OPENAI_KEY')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYSTEM_DIRECTIVES = []
DIALOGUE_STACK = []

def load_system_directives():
    '''Load the json file containing system directives'''
    with open('app/mabel/system-directives/system_directives.json') as f:
        system_directives = json.load(f)
    return system_directives

async def chatgpt_response(prompt):
    global DIALOGUE_STACK, SYSTEM_DIRECTIVES
    SYSTEM_DIRECTIVES = load_system_directives()
    current_prompt = {"role": "user", "content": prompt}
    DIALOGUE_STACK.append(current_prompt)
    DIALOGUE_STACK = DIALOGUE_STACK[-6:]
    messages = SYSTEM_DIRECTIVES + DIALOGUE_STACK

    
    logger.info("PROMPT: " + prompt.lower())
    try:
        response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1800,
        )
        response_content = response['choices'][0]['message']['content']
        logger.info("RESPONSE: " + response_content)
        re.compile(r'As an .* AI')
        if not re.search(r'As an .* AI', response_content):
            DIALOGUE_STACK.append({"role": "assistant", "content": response_content })
        return response_content
    except Exception as e:
        logger.info("OPENAI Error: " + str(e))
        return "I'm sorry, I'm having trouble understanding you. Could you try rephrasing that?"        