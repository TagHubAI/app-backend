from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Users(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=50, null=True)
    username = fields.CharField(max_length=20, unique=True)
    email = fields.CharField(max_length=128, null=True)
    hashed_password = fields.CharField(max_length=128, null=True)
    is_activated = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.username

class UserRegisterIn(Users):
    password = fields.CharField(max_length=128, null=True, generated=True)

class Workflows(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, default="Default Workflow Name")
    description = fields.CharField(max_length=255, default="Default Workflow Description")
    datasets = fields.ManyToManyField('models.Datasets', related_name="workflow", through="workflow_dataset", null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name

class Datasets(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, default="Default Dataset Name")
    datapoints: fields.ReverseRelation["Datapoints"]
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Datapoints(models.Model):
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=65536)
    dataset = fields.ForeignKeyField("models.Datasets", related_name="datapoint")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.content

User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude=("hashed_password", "is_activated"))
UserOut_Pydantic = pydantic_model_creator(Users, name="UserOut", exclude=("hashed_password",))
UserRegisterIn_Pydantic = pydantic_model_creator(UserRegisterIn, exclude=("hashed_password", "is_activated"), exclude_readonly=True)

Workflow_Pydantic = pydantic_model_creator(Workflows, name="Workflow")
WorkflowIn_Pydantic = pydantic_model_creator(Workflows, name="WorkflowIn", exclude_readonly=True)
WorkflowOut_Pydantic = pydantic_model_creator(Workflows, name="WorkflowOut")

Dataset_Pydantic = pydantic_model_creator(Datasets, name="Dataset")
DatasetIn_Pydantic = pydantic_model_creator(Datasets, name="DatasetIn", exclude_readonly=True)
DatasetOut_Pydantic = pydantic_model_creator(Datasets, name="DatasetOut")

Datapoint_Pydantic = pydantic_model_creator(Datapoints, name="Datapoint")
DatapointIn_Pydantic = pydantic_model_creator(Datapoints, name="DatapointIn", exclude_readonly=True)
DatapointOut_Pydantic = pydantic_model_creator(Datapoints, name="DatapointOut", exclude=["created_at","modified_at"])
