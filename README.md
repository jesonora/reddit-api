# Reddit API
## Table of contents
* [General info](#general-info)
* [Project structure](#project-structure)
* [Running locally](#running-locally)


## General info

This project is an API who get the latest 25 comments of a subreddit with a polarization score.

Would be nice to have:

* pre-commit hooks
* tests
* security layer


## Project structure
```
fastapi-project
├── bin/local
│   └── environment.yml
├── src
│   ├── api
│   │   ├── comments.py
│   │   └── base.py
│   ├── configs
│   │   └── base.py
│   ├── utils
│   │   └── logging.py
│   └── routes.py
├── tests
│   └── test_comments.py
├── notebooks
│   ├── 00_explore.ipynb
│   └── 01_direct_api.ipynb
├── .dockerignore
├── .gitignore
├── Dockerfile
├── main.py
├── requirements-dev.txt
├── requirements.txt
└── README.md
```

## Running locally
Follow the steps to run it locally:

````shell
# Build image
docker build -t reddit:latest .

# Run image in local (from port 8000 to 8000 in localhost)
docker run -d -p 8000:8000 --name reddit reddit:latest

# Status of the container
docker ps

# Go to docs
http://127.0.0.1:8000/docs

# Test with curl
curl -X 'GET' 'http://127.0.0.1:8000/api/v1/scores/webdev?sort_by=created_utc'
  
````