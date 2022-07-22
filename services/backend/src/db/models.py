from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Users(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=50, null=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class Workflows(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class Datasets(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    workflow = fields.ForeignKeyField("models.Workflows", related_name="dataset")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class Datapoints(models.Model):
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=255)
    dataset = fields.ForeignKeyField("models.Datasets", related_name="datapoint")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
UserOut_Pydantic = pydantic_model_creator(Users, name="UserOut", exclude=("password",))

Workflow_Pydantic = pydantic_model_creator(Workflows, name="Workflow")
WorkflowIn_Pydantic = pydantic_model_creator(Workflows, name="WorkflowIn", exclude_readonly=True)
WorkflowOut_Pydantic = pydantic_model_creator(Workflows, name="WorkflowOut")

Dataset_Pydantic = pydantic_model_creator(Datasets, name="Dataset")
DatasetIn_Pydantic = pydantic_model_creator(Datasets, name="DatasetIn", exclude_readonly=True)
DatasetOut_Pydantic = pydantic_model_creator(Datasets, name="DatasetOut", exclude_readonly=True)

Datapoint_Pydantic = pydantic_model_creator(Datapoints, name="Datapoint")
DatapointIn_Pydantic = pydantic_model_creator(Datapoints, name="DatapointIn", exclude_readonly=True)
DatapointOut_Pydantic = pydantic_model_creator(Datapoints, name="DatapointOut", exclude_readonly=True)