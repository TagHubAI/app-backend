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
    

