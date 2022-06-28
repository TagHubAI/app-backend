<div align="center">

# TagHub.Dev 
**Next-gen text analytics platform**

</div>

# Installation
## Install requirements
First, install `Python >= 3.7` using either [OEM Python Installer](https://www.python.org/downloads/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
```
pip install -r backend/requirements.txt
```

## Run the backend service
```bash
cd backend
python main.py 
```
Then go to `127.0.0.0:8000` to see to the main dashboard.

## Run the frontend 
```bash
cd frontend
npm install # Install dependencies
npm run lint # Optional: Run linting
npm run dev # Run dev server
```

## Docker
Dedicated Dockerfile for web services:
- Backend: `backend/Dockerfile` 
- Frontend: `frontend/Dockerfile`

# Roadmap
@TODO: To be updated

# Contributing
@TODO: To be updated

# License
GPLv3