# Reddit API

## Local Running
This is an example to in local:
````shell
# Build image
docker build -t reddit:latest .

# Run image in local (from port 5000 to 5000 in localhost)
docker run -d -p 8000:8000 --name reddit reddit:latest

# Status
docker ps

# Go to docs
http://127.0.0.1:8000/docs

# Test with curl
curl -X 'GET' 'http://127.0.0.1:8000/api/v1/scores/webdev?sort_by=created_utc'
  
````


## Project structure
````
fastapi-project
├── alembic/
├── src
│   ├── api
│   │   ├── comments.py
│   │   └── base.py
│   ├── configs
│   │   └── base.py
│   ├── utils
│   │   └── logging.py
│   └── routes.py
├── tests/
│   └── api
├── main.py
├── requirements-dev.txt
├── requirements.txt
└── .gitignore
````
