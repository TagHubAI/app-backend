from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.db.models import Datasets


DatasetInSchema = pydantic_model_creator(
    Datasets, name="DatasetIn", exclude=["name"], exclude_readonly=True)
DatasetOutSchema = pydantic_model_creator(
    Datasets, name="DatasetOut", exclude =[
      "modified_at", "created_at", "user.id"
    ]
)

class UpdateDataset(BaseModel):
    name: Optional[str]