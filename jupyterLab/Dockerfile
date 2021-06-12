ARG BASE_CONTAINER=jupyter/pyspark-notebook

# Set the base image. 
FROM --platform=linux/amd64 $BASE_CONTAINER

# Adds metadata to image.
LABEL maintainer="Fernando"
LABEL org.label-schema.name="jupyterhub"
LABEL org.label-schema.description="Image that contains the most important tools for JupyterHub Data Science"
# LABEL org.label-schema.build-date="2021-03-14T09:24:41Z"
# LABEL org.label-schema.usage="./doc/app-usage.txt"
LABEL org.label-schema.schema-version="1.0"

# Sets the user name to use when running the image.
USER root

RUN apt-get update && apt-get install -y && apt-get clean

USER jovyan

# Sets the working directory
WORKDIR /etc/jupyter/

# Add requirements file 
COPY requirements.txt /etc/jupyter/

# Install Python Packages & Requirements 
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Native Authenticator
RUN pip install --quiet --no-cache-dir 'jupyterhub-nativeauthenticator'

# Indicates the ports on which a container listens for connections. 
EXPOSE 8000

USER root

COPY jupyter_hub_config.py /etc/jupyter
# Run shell command for notebook
CMD jupyterhub -f /etc/jupyter/jupyter_hub_config.py 