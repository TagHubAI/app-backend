FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
RUN yarn add @vue/cli@4.5.13 -g

COPY package.json .
COPY yarn.lock .

RUN yarn install
