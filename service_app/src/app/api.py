from fastapi import FastAPI, Request, Depends, UploadFile, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import asyncio

from .db.config import TORTOISE_ORM_CONFIG
from .db.models import (
    Users, 
    UserRegisterIn_Pydantic,
    User_Pydantic, 
    UserIn_Pydantic, 
    UserOut_Pydantic, 
    Workflows,
    WorkflowIn_Pydantic, 
    WorkflowOut_Pydantic,
    Datasets,
    DatasetOut_Pydantic,
    Datapoints,
    DatapointOut_Pydantic,
    )

from .db.schemas import DualResourceActionResponse, SingleResourceActionResponse, CreateDatasetBody, SignUpRequestBody, SignInRequestBody, LineByLineTextInput, VerifyTokenInput
from .auth.security import  get_password_hash
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv
import os

from supabase import create_client, Client

import firebase_admin 
from firebase_admin import credentials, auth
import pyrebase
import json

from typing import List, Dict
from bertopic import BERTopic
import texthero as hero
import pandas as pd

load_dotenv()  # take environment variables from .env.

app = FastAPI()

# Allowed origins
origins = [
    "http://127.0.0.1:3333",
    "http://localhost:3333",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Register Turtoise ORM for database 
register_tortoise(app, **TORTOISE_ORM_CONFIG)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

supabase: Client = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))

# Setup firebase authentication
# firebase_admin.initialize_app(credentials.Certificate(json.loads(os.environ.get("FB_ADMIN_CONFIGS"))))
# pb = pyrebase.initialize_app(json.loads(os.environ.get("FB_PYREBASE_CONFIGS")))

# Setup supabase authentication

def api_authen(token):
    user = supabase.auth.api.get_user(jwt=token)
    if user.aud and user.aud == "authenticated":
        return True
    return False

# signup endpoint
@app.post("/signup")
async def signup(req: SignUpRequestBody):
    email: str = req.email
    # Only required email for signup at this time
    # password: str = 
    #
    # if email is None or password is None:
    #    return HTTPException(detail={'message': 'Error! Missing Email or Password'}, status_code=400)
    # try:
    #    user = auth.create_user(
    #        email=email,
    #        password=password
    #    )
    #    return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=200)    
    # except Exception as e:
    #     return HTTPException(detail={'message': str(e)}, status_code=400)
    
    try:
        user: Dict[str, Any] = supabase.auth.sign_up(email=email)
        return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=200)    
    except Exception as e:
        return HTTPException(detail={'message': str(e)}, status_code=400)

@app.post("/api/v1/user")
async def get_user_base_on_token(req: VerifyTokenInput):
    token: str = req.token
    user =  supabase.auth.api.get_user(jwt=token)
    return {"aud": user.aud, "email": user.email }  
    
    # Only required email for signup at this time
    # password: str = 
    #
    # if email is None or password is None:
    #    return HTTPException(detail={'message': 'Error! Missing Email or Password'}, status_code=400)
    # try:
    #    user = auth.create_user(
    #        email=email,
    #        password=password
    #    )
    #    return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=200)    
    # except Exception as e:
    #     return HTTPException(detail={'message': str(e)}, status_code=400)
    
    try:
        user: Dict[str, Any] = supabase.auth.sign_up(email=email)
        return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=200)    
    except Exception as e:
        return HTTPException(detail={'message': str(e)}, status_code=400)

@app.post("/signin")
async def signin(request: SignInRequestBody):
    email: str = request.email
    # password: str = request.password
    # try:
    #    user = pb.auth().sign_in_with_email_and_password(email, password)
    #    jwt = user['idToken']
    #    return JSONResponse(content={'token': jwt}, status_code=200)
    # except Exception as e:
    #    return HTTPException(detail={'message': str(e)}, status_code=400)

    try:
        user: Dict[str, Any] = supabase.auth.sign_in(email=email)
        return JSONResponse(content={'message': f'Sended email to a user {user}'}, status_code=200)    
    except Exception as e:
        return HTTPException(detail={'message': str(e)}, status_code=400)

@app.get("/api/v1/ping")
async def ping(token: str = Depends(oauth2_scheme)):
    return {"result": "Cool"}


@app.post("/login", include_in_schema=False)
async def login(request: SignUpRequestBody):
   req_json = await request.json()
   email = request['email']
   password = request['password']
   try:
       user = pb.auth().sign_in_with_email_and_password(email, password)
       jwt = user['idToken']
       return JSONResponse(content={'token': jwt}, status_code=200)
   except:
       return HTTPException(detail={'message': 'There was an error logging in'}, status_code=400)


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
async def list_workflows(token: str = Depends(oauth2_scheme)):
    """
    List all workflows available
    """
    return await WorkflowOut_Pydantic.from_queryset(Workflows.all())

@app.put("/api/v1/workflows/{workflow_id}/mount/datasets/{dataset_id}", response_model = DualResourceActionResponse)
async def mount_dataset_to_workflow(workflow_id: int, dataset_id: int, token: str = Depends(oauth2_scheme)):
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
async def delete_workflow(workflow_id: int, token: str = Depends(oauth2_scheme)):
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
async def get_datasets_by_workflow(workflow_id, token: str = Depends(oauth2_scheme)):
    """
    Get all datasets given a workflow
    """
    queryset = await Datasets.filter(workflow__id__in=[workflow_id])
    return queryset

@app.post("/api/v1/datasets/upload")
async def upload_dataset(file: UploadFile, dataset_name: str = "Default dataset name", token: str = Depends(oauth2_scheme)):
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

@app.post("/api/v1/datasets/create", response_model=DatasetOut_Pydantic)
async def create_dataset(request_body: CreateDatasetBody, dataset_name: str = "Default dataset name", token: str = Depends(oauth2_scheme)):
    """
    Create a dataset either by: facebook_post_urls or fanpage_id

    """
    from facebook_scraper import get_posts

    facebook_post_urls = request_body.dict()['facebook_post_urls']

    if len(facebook_post_urls) > 0:
        comments = []

        # Create dataset
        dataset = await Datasets.create(name=dataset_name) 

        for post in get_posts(post_urls=facebook_post_urls, options={"comments": True}):
            comments_full = post["comments_full"]

            for comment in comments_full:
                comment_text = comment["comment_text"]
                comments.append(comment_text)

                # Create datapoint entry for each comment
                await Datapoints.create(content=comment_text, dataset=dataset)

        return dataset

    return


@app.get("/api/v1/datasets", response_model=List[DatasetOut_Pydantic])
async def list_datasets(token: str = Depends(oauth2_scheme)):
    """
    List all datasets
    """
    return await DatasetOut_Pydantic.from_queryset(Datasets.all())

@app.delete("/api/v1/datasets", response_model=SingleResourceActionResponse)
async def delete_dataset(dataset_id, token: str = Depends(oauth2_scheme)):
    await Datasets.filter(id=dataset_id).delete()
    return SingleResourceActionResponse(
        resource_name = "dataset",
        resource_id = dataset_id,
        action = "delete"
    )

@app.get("/api/v1/datasets/{dataset_id}/datapoints", response_model=List[DatapointOut_Pydantic])
async def list_datapoints_from_dataset(dataset_id, token: str = Depends(oauth2_scheme)):
    """
    List all datapoints from a dataset
    """
    queryset = await Datapoints.filter(dataset__id__in=[dataset_id])
    return queryset


@app.post("/api/v1/apps/topic_model/process")
async def run_process_clustering(req: VerifyTokenInput, payload: LineByLineTextInput):
    """
    Process a request data
    """
    authenticated = api_authen(req.token)
    if authenticated:
        topic_model = BERTopic(embedding_model="all-MiniLM-L6-v2")
        docs = payload.text_data.split("\n")

        # Preprocess
        clean_docs = pd.Series(docs).pipe(hero.clean)

        topics, probs = topic_model.fit_transform(clean_docs)

        num_topics = max(topics)
        sentences_by_topics = {topic_id: {"data":[],"topic": []} for topic_id in range(num_topics+1)}

        for doc, topic_id in zip(docs, topics):
            # topic "-1" are stopwords
            if topic_id == -1: continue
            sentences_by_topics[topic_id]["data"].append(doc)

        for topic_id in range(num_topics+1):
            # Get keywords
            #keywords = topic_model.get_topic_info(topic_id).Name.values[0].split("_")[1:]
            topic = topic_model.get_topic(topic_id)
            
            # convert to percentage
            topic = [(t[0].capitalize(), round(t[1]*100,2)) for t in topic]
            sentences_by_topics[topic_id]["topic"] = topic
            sentences_by_topics[topic_id]["count"] = len(sentences_by_topics[topic_id]["data"]) 


        # Change to list
        sentences_by_topics = [topic_items for (_, topic_items) in sentences_by_topics.items()]

        return sentences_by_topics 
    return []

    
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


