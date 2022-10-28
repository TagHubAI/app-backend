from pydantic import BaseModel
from typing import List

class SingleResourceActionResponse(BaseModel):
    resource_name: str
    resource_id: str 
    action: str

class DualResourceActionResponse(BaseModel):
    resource_1_name: str
    resource_1_id: int
    resource_2_name: str
    resource_2_id: int
    action: str

class CreateDatasetBody(BaseModel):
    facebook_post_urls: List[str]

class SignUpRequestBody(BaseModel):
    email: str
    # Only require email at this time
    # password: str
    
class SignInRequestBody(BaseModel):
    email: str
    password: str

class LineByLineTextInput(BaseModel):
    """
    This is first line\nThis is second line

    """
    text_data: str

class VerifyTokenInput(BaseModel):
    token: str

