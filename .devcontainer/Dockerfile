# docker build -t purplesand/stable3d:latest -f .devcontainer/Dockerfile .
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
    && rm -rf /var/lib/apt/lists/*

# install required packages from pypi
COPY requirements/pt2.txt /home/${USER_NAME}/requirements/pt2.txt
RUN cd /home/${USER_NAME} \
    && pip3 install -r requirements/pt2.txt
COPY requirements/vivid123.txt /home/${USER_NAME}/requirements/vivid123.txt
RUN cd /home/${USER_NAME} \
    && pip3 install -r requirements/vivid123.txt