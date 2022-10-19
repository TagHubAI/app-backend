FROM python:3.10-buster AS compile-image
RUN python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENV PORT=8330

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-buster AS build-image
WORKDIR /app
COPY --from=compile-image /opt/venv /opt/venv
# RUN apk upgrade --no-cache && \
#     apk add --no-cache postgresql-client bash openssl libgcc libstdc++ ncurses-libs
# RUN set -ex \
#     && apk add --no-cache --virtual .build-deps \
#         cmake \
#         curl \
#         g++ \
#         gcc \
#         jpeg-dev \
#         libffi-dev \
#         libjpeg \
#         make \
#         musl-dev \
#         musl \
#         postgresql-dev \
#         python3-dev \
#         tzdata \
#         zlib \
#         zlib-dev \
#         libc6-compat \
#         libc-dev \
#         alpine-sdk \
#         build-base \
#         linux-headers \
#         cython \
#         c-ares-dev \
#         gdbm \
#         libffi
# COPY ./src .
# COPY .env .

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
# ENV DATABASE_URL="sqlite://db.sqlite"
# EXPOSE 4000
#
CMD uvicorn app.api:app --reload --host 0.0.0.0 --port $PORT
