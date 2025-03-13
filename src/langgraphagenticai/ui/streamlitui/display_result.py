import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage


class DisplayResultsStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_results(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase =="Basic Chatbot":
            for event in graph.stream({'messages':("user",user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
