from langchain_groq import ChatGroq
import streamlit as st


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_input = user_controls_input

    def get_groq_llm(self):
        try:
            api_key = self.user_input["GROQ_API_KEY"]
            model = self.user_input["selected_groq_model"]

            if api_key != None:
                llm = ChatGroq(model=model, api_key=api_key)
                return llm
            else:
                st.error("Error occurred: API Key is not present")
                
        except:
            raise ValueError("Exception occurred while getting LLM instance.")


