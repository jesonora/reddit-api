FROM python:3.9-slim

WORKDIR /app

# As this file doesn't change often, Docker will detect it and use the cache for this step and the next one too
COPY requirements.txt .

# The --no-cache-dir option tells pip to not save the downloaded packages locally, as that's only if pip was going to
# be run again to install the same packages, but that's not the case when working with containers
RUN pip install --no-cache-dir -r ./requirements.txt

ADD src/ ./src/
ADD main.py .

EXPOSE 8000

CMD ["python", "main.py"]