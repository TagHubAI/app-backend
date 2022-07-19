from pydantic import BaseModel

class TextBase(BaseModel):
    text_content: str