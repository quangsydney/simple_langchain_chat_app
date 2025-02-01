from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory

llm = None

def get_llm_instance(gemini_api_key):
    """
    Method to return the instance of llm model globally
    :return:
    """
    global llm
    if llm is None:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=gemini_api_key,
            stream=True,
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            },
        )
    return llm