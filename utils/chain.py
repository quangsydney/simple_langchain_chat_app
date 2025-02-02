import os
from langchain.chains import ConversationChain
import asyncio
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory, ConversationBufferWindowMemory
from utils.load_llm import get_llm_instance


conversation_chain = None


def get_conversation_chain(gemini_api_key):
    """
    Method to return the conversational chain
    In langchain chain is the sequence of interconnected component designed to execute tasks
    in a specific order.
    :return: conversational chain
    """
    global conversation_chain
    llm = get_llm_instance(gemini_api_key)

    if conversation_chain is None:
        conversation_chain = ConversationChain(
            llm=llm,
            memory=ConversationBufferWindowMemory(k=10)
        )
    return llm, conversation_chain


async def generate_response(conversational_chain,prompt):
    async for chunk in conversational_chain.astream(input=prompt):
        print(chunk.content)


if __name__ == "__main__":
    llm, conversation_chain = get_conversation_chain(gemini_api_key)
    asyncio.run(generate_response(llm, prompt="hello, how llm help to address patient health queries in hospital'schatbot?"))