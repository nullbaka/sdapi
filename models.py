from pydantic import BaseModel


class Prompt(BaseModel):
    text: str = """
        Hello, my name is Suno. And, uh — and I like pizza. [laughs]
        But I also have other interests such as playing tic tac toe.
    """
