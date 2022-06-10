This repository is a solution for the test task.
[Docker](https://www.docker.com/) should be installed to run the solution in the container

#### To run with docker:
```console
$ docker build -t api .
$ sudo docker run -p 8000:8000 api:latest
```

#### API will be availible at http://localhost:8000/
- For the first solution use example URL:
http://0.0.0.0:8000/solution?a=8&b=2&c=3
- For the second solution:
http://0.0.0.0:8000/sample_colour


#### To run without docker
Install [Poetry](https://python-poetry.org/) for Python package and environment management and then run with:
```console
poetry install
poetry shell
python3 main.py
```

API documentation: http://localhost:8000/docs

