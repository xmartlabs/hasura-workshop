### Install docker
https://get.docker.com/

### Install docker-compose
https://github.com/docker/compose/releases

### Install pyenv
To handle python versions we will be using pyenv in order for us to be sure that we are using the same python version and avoid any kind of unexpected issues

https://github.com/pyenv/pyenv

### Install Poetry
We will be using Poetry for the python local virtual environment
https://python-poetry.org/docs/#installation

Note: We will be using python just for the custom actions and triggers and the logic will be already implemented by the time the workshop start, the goal of this workshop is not to improve our python coding

### Project setup
Note: This step can be skipped if you are already using other python version handler or if you already have python 3.7 or above installed on your machine.

First of all we will need to install python 3.10.2

```shell
pyenv install 3.10.2
pyenv local 3.10.2
```

After setting the python version we will be using in our virtual environment, just need to install the dependencies with poetry
```shell
poetry install
```

### Running Hasura and the Fastapi server

To run both instances of Hasura that we will be using just run:

```shell
pyenv install 3.10.2
pyenv local 3.10.2
```

And to run the FastApi server in another console run:
 ```shell
uvicorn main:app --reload
```
