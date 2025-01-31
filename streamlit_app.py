import streamlit as st
# from langchain.llms import openai
import ollama
import os

os.system('ollama pull deepseek-r1:1.5b')

st.title('Quickstart App')
# openai_api_key = st.sidebar.text_input('OpenAI API Key')

messages = []
# Roles
USER = 'user'
ASSISTANT = 'assistant'

def add_history(content, role):
    messages.append({'role': role, 'content': content})

def generate_response(input_text):
    # llm = openai.OpenAI(openai_api_key=openai_api_key)
    # st.info(llm(input_text))

    add_history(input_text, USER)
    response = ollama.chat(
            # model="deepseek-r1:1.5b",
            model="gemma2:2b",
            messages=messages,
            stream=True
            )
    complete_message = ""
    for line in response:
        complete_message += line['message']['content']
        print(line['message']['content'], end='', flush=True)
    st.info(complete_message)
    add_history(complete_message, ASSISTANT)

with st.form('my_form'):
    text = st.text_area('Enter text: ', 'Give 2 advantages of reading.')
    submitted = st.form_submit_button('Submit')
    # if not openai_api_key.startswith('sk-'):
    #     st.warning("Please enter your OpenAI API key!", icon="⚠")
    # elif submitted:
    #     generate_response(text)
    generate_response(text)



# def chat(message):
#     add_history(message, USER)
#     response = ollama.chat(model="gemma2:2b", messages=messages, stream=True)
#     complete_message = ''
#     for line in response:
#         complete_message += line['message']['content']
#         print(line['message']['content'], end='', flush=True)
#     add_history(complete_message, ASSISTANT)

# while True:
#     print('\nQ to quit')
#     prompt = input('Enter your message: ')
#     if prompt.lower() == 'q':
#         break
#     else:
#         chat(prompt)