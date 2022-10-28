FROM python:3.10-buster AS compile-image
RUN python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENV PORT=4000

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim-buster AS build-image
WORKDIR /app
COPY --from=compile-image /opt/venv /opt/venv
# RUN apk upgrade --no-cache && \
#     apk add --no-cache postgresql-client bash openssl libgcc libstdc++ ncurses-libs
# COPY .env .

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
# ENV DATABASE_URL="sqlite://db.sqlite"
# EXPOSE 4000
#
# CMD uvicorn app.api:app --reload --host 0.0.0.0 --port $PORT
#
# FROM python:3.10
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY ./src .
