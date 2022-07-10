from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=50, null=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Datasets(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    owner = fields.ForeignKeyField("models.Users", related_name="dataset")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Datapoints(models.Model):
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=255)
    dataset = fields.ForeignKeyField("models.Users", related_name="datapoint")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
