from langchain_groq import ChatGroq


def get_llm(self):
    llm = ChatGroq(model="qwen-2.5-32b")
    return llm

