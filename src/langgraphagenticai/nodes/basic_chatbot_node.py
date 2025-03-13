from src.langgraphagenticai.state.state import State


class  BasicChatbotNode:
    def __init__(self, model):
        self.model = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """
        msg = self.model.invoke(state["messages"]);
        return {"messages": msg}
    
