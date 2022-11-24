FROM node:16-bullseye

SHELL ["/bin/bash", "-c"]
# Make sure we use the virtualenv:
WORKDIR /usr/src/app 
RUN npm install --global pnpm \
    && SHELL=bash pnpm setup \
    && source /root/.bashrc
# COPY package.json /usr/src/app
# RUN pnpm store prune
# RUN pnpm cache clean --force
COPY . /usr/src/app
COPY package.json /usr/src/app

RUN rm -rf node_modules
# RUN rm pnpm-lock.yaml
RUN pnpm install 
RUN pnpm install esbuild
EXPOSE 3333
# RUN pnpm install -g esbuild
# RUN pnpm install esbuild-arm-64
# RUN pnpm build 
# RUN pnpm dev

# FROM node:16-alpine as build-stage
# WORKDIR /app
# RUN corepack enable
#
# RUN apk add --no-cache curl \
#     && curl -sL https://unpkg.com/@pnpm/self-installer | node
# RUN npm install -g pnpm
# COPY .npmrc package.json pnpm-lock.yaml ./
# RUN --mount=type=cache,id=pnpm-store,target=/root/.pnpm-store \
#     pnpm install --frozen-lockfile
#
#
# FROM nginx:stable-alpine as production-stage
#
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
#
# CMD ["nginx", "-g", "daemon off;"]
#
