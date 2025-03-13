
from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """

    def __init__(self, model):
        self.model = model

    def process(self, state: State) -> dict:
        """
        Process the input state and generates a response with tool integration
        """

        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.model.invoke([{"role": "user", "content": user_input}])

        # Simulate tool specific logic
        tool_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tool_response]}
    
    def create_chatbot(self, tools):
        """
        Returns chatbot node function.
        """
        model_with_tools = self.model.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response
            """
            return {"messages": [model_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
    
