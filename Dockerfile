FROM python:3.9-slim AS compile-image
RUN python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENV PORT=4000

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-alpine AS build-image
WORKDIR /code
COPY --from=compile-image /opt/venv /opt/venv
COPY ./src .

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENV DATABASE_URL="sqlite://db.sqlite"
EXPOSE 4000

CMD uvicorn app.api:app --reload --host 0.0.0.0 --port $PORT

