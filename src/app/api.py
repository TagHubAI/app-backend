from fastapi import FastAPI, Request, Depends, Form, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

import asyncio

from .db.config import TORTOISE_ORM_CONFIG
from .db.models import (
    Users, 
    User_Pydantic, 
    UserIn_Pydantic, 
    UserOut_Pydantic, 
    Workflows,
    Workflow_Pydantic, 
    WorkflowIn_Pydantic, 
    WorkflowOut_Pydantic,
    Datasets,
    Dataset_Pydantic,
    DatasetIn_Pydantic,
    DatasetOut_Pydantic,
    Datapoints,
    Datapoint_Pydantic,
    DatapointIn_Pydantic,
    DatapointOut_Pydantic,
    )

from .db.schemas import DualResourceActionResponse, SingleResourceActionResponse
from tortoise.contrib.fastapi import register_tortoise
import starlette.status as status
from tortoise.query_utils import Prefetch


from typing import List
from typing import Union

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, **TORTOISE_ORM_CONFIG)

@app.get("/")
async def read_root():
    return "Please go to /docs to read the documentation"

@app.post("/api/v1/workflows", response_model = WorkflowOut_Pydantic)
async def create_workflow(workflow: WorkflowIn_Pydantic):
    """
    Create a new Workflow
    """
    workflow_obj = await Workflows.create(**workflow.dict(exclude_unset=True))
    return await WorkflowOut_Pydantic.from_tortoise_orm(workflow_obj)

@app.get("/api/v1/workflows", response_model=List[WorkflowOut_Pydantic])
async def list_workflows():
    """
    List all workflows available
    """
    return await WorkflowOut_Pydantic.from_queryset(Workflows.all())

@app.put("/api/v1/workflows/{workflow_id}/mount/datasets/{dataset_id}", response_model = DualResourceActionResponse)
async def mount_dataset_to_workflow(workflow_id: int, dataset_id: int):
    """
    Add a dataset to a workflow
    """
    workflow = await Workflows.get(id=workflow_id)
    dataset = await Datasets.get(id=dataset_id)
    await workflow.datasets.add(dataset)
    return DualResourceActionResponse(
        resource_1_name="workflow", 
        resource_1_id=workflow_id,
        resource_2_name="dataset",
        resource_2_id=dataset_id,
        action="mount" ,
        ) 

@app.delete("/api/v1/workflows/{workflow_id}", response_model=SingleResourceActionResponse)
async def delete_workflow(workflow_id: int):
    """
    Delete a workflow
    """
    await Workflows.filter(id=workflow_id).delete()
    return SingleResourceActionResponse(
        resource_name = "workflow",
        resource_id = workflow_id,
        action = "delete"
    )

@app.get("/api/v1/workflows/{workflow_id}/datasets", response_model=List[DatasetOut_Pydantic])
async def get_datasets_by_workflow(workflow_id):
    """
    Get all datasets given a workflow
    """
    queryset = await Datasets.filter(workflow__id__in=[workflow_id])
    return queryset

@app.post("/api/v1/datasets/upload")
async def upload_dataset(file: UploadFile, dataset_name: str = "Default dataset name"):
    """
    Upload a dataset to a id-th workflow
    """
    ACCEPTED_EXT = [".csv"]

    filename = file.filename
    if not any([filename.endswith(ext) for ext in ACCEPTED_EXT]):
        return HTTPException(status_code="415", detail=f"Expected extension to be in {ACCEPTED_EXT} but got '{file.filename}'")

    dataset = await Datasets.create(name=dataset_name) 

    if filename.endswith(".csv"):
        import csv
        content =  await file.read()
        lines = content.splitlines()

        for row in lines:
            row_content = row.decode().split(",")
            content = row_content[0]
            data = await Datapoints.create(content=content, dataset=dataset)
    
    return {"filename": file.filename}

@app.get("/api/v1/datasets", response_model=List[DatasetOut_Pydantic])
async def list_datasets():
    """
    List all datasets
    """
    return await DatasetOut_Pydantic.from_queryset(Datasets.all())

@app.delete("/api/v1/datasets", response_model=SingleResourceActionResponse)
async def delete_dataset(dataset_id):
    await Datasets.filter(id=dataset_id).delete()
    return SingleResourceActionResponse(
        resource_name = "dataset",
        resource_id = dataset_id,
        action = "delete"
    )

@app.get("/api/v1/datasets/{dataset_id}/datapoints", response_model=List[DatapointOut_Pydantic])
async def list_datapoints_from_dataset(dataset_id):
    """
    List all datapoints from a dataset
    """
    queryset = await Datapoints.filter(dataset__id__in=[dataset_id])
    return queryset


    # return await Datapoints.all().prefetch_related(Prefetch(dataset, queryset))
# 
#### POSTPONED UNTIL HAVE USERS MANAGEMENT
# @app.get("/")
# def get_root():
#     return "Hello World! TagHub is awesome!"

# @app.get("/api/v1/users", response_model = List[UserOut_Pydantic])
# async def get_users():
#     return await UserOut_Pydantic.from_queryset(Users.all())

# @app.get("/api/v1/users/{user_id}", response_model = UserOut_Pydantic)
# async def get_user(user_id: int):
#     return await UserOut_Pydantic.from_queryset_single(Users.get(id=user_id))

# @app.post("/api/v1/user", response_model = UserOut_Pydantic)
# async def create_user(user: UserIn_Pydantic):
#     user_obj = await Users.create(**user.dict(exclude_unset=True))
#     return await UserOut_Pydantic.from_tortoise_orm(user_obj)

# @app.post("/api/v1/authorize")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = User_Pydantic.from_queryset_single(Users.get(username=form_data.get('username'))) 

#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")

#     return {"access_token": user.username, "token_type": "bearer"}


