# docker build -t purplesand/generative_model:latest -f dockers/Dockerfile .
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

# apt install by root user
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libegl1-mesa-dev \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    python-is-python3 \
    python3.10-dev \
    python3-pip \
    wget \
    software-properties-common curl openssh-server \
    && rm -rf /var/lib/apt/lists/*

# install for vessl ai
RUN pip install jupyterlab

# install required packages from pypi
COPY requirements/pt2.txt tmp/requirements/pt2.txt
RUN  pip3 install -r tmp/requirements/pt2.txt