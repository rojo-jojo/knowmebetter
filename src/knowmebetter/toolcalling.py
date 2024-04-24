from langchain_core.pydantic_v1 import BaseModel, Field
from llm import llm

# Note that the docstrings here are crucial, as they will be passed along
# to the model along with the class name.
class Add(BaseModel):
    """Add two integers together."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")


class Multiply(BaseModel):
    """Multiply two integers together."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")


tools = [Add, Multiply]

from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(model="mistral-large-latest")