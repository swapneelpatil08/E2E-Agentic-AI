from typing import Annotated, TypedDict
from langgraph.graph import add_messages

class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """
    messages: Annotated[list, add_messages]
