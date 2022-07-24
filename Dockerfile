FROM python:3.9-slim AS compile-image
# RUN apt-get update
# RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .

FROM python:3.9-alpine AS build-image
RUN mkdir app
WORKDIR /app
COPY --from=compile-image /opt/venv /opt/venv
COPY . .
EXPOSE $PORT 

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENV DATABASE_URL="sqlite://db.sqlite"

CMD uvicorn src.app.api:app --reload --host 0.0.0.0 --port 4000

