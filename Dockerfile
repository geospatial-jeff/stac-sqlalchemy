FROM python:3.9-slim-bullseye as base

FROM base as builder
# Any python libraries that require system libraries to be installed will likely
# need the following packages in order to build
RUN apt-get update && apt-get install -y build-essential git

WORKDIR /app

COPY . /app

RUN mkdir -p install && \
    pip install -e .[dev] \