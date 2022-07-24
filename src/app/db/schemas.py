from pydantic import BaseModel

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