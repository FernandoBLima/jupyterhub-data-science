# JupyterHub Data Science

The main goal of this project was development an environment in Docker that contains the most important tools for data analysis, data visualization, machine learning and statistics. 

## Mains Tools
- Docker
- JupyterHub

## Technical Overview

This project include the Jupyter Notebook scientific Python stack that uses the pyspark-notebook image from Jupyter Docker Stacks that is a set of ready-to-run image application. 

This project uses the `jupyter/pyspark-notebook` image that includes some popular packages from the scientific Python ecosystem such as: dask, pandas, numexpr, matplotlib, scipy, seaborn, scikit-learn, scikit-image, sympy, cython, patsy, statsmodel, cloudpickle, dill, numba, bokeh, sqlalchemy, hdf5, vincent, beautifulsoup, protobuf, xlrd, bottleneck, pytables packages, ipywidgets, ipympl and Apache Spark with Hadoop binaries.

Besides that, it was used a simple authenticator for small-medium size JupyterHub applications using the `Native Authenticator` that provides the following features:

- Add new users on the system;
- Users needs an authorization to accessing the system;
- Can be added password security such as common passwords or minimum password length;


## Usage

### Running JupyterHub using Docker

You will need Docker installed to follow the next steps.

Build the image jupyterhub using the following command:

```bash
docker build -t <IMAGE_NAME> .
```

Then, run the docker container using the command shown below:

```bash
docker run -p -d 8000:8000 <IMAGE_NAME>
```

### Running JupyterHub using Docker Compose

And build the image locally using docker-compose build.
```bash
docker-compose build up --build
```

## How it Works

### First Access
After accessing JupyterLab in `http://localhost:8000/`, it is necessary to SignUp and then SignIn using the default user. In the `jupyter_hub_config` file, the default username and password are defined.

### New Users
To add a new user it is necessary to create in the sign up adding the username, email and password. Then the admin user who has permission to authorize or deauthorize users can manage these system accesses in `/hub/authorize` and then add new users in `/hub/admin`

### Change the Password
Users can also change their passwords by accessing: `/hub/change-password`.

## Help and Resources

You can read more on:

- [Docker documentation](https://docs.docker.com/get-started/overview/)
- [Jupyter Docker Stacks documentation](http://jupyter-docker-stacks.readthedocs.io/)
- [Jupyterhub Tutorial](https://github.com/jupyterhub/jupyterhub-tutorial)
- [Native Authenticator’s documentation](https://native-authenticator.readthedocs.io/en/latest/)