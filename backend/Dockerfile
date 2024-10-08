FROM python:3.12.3-slim-bookworm AS prod
RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*


RUN pip install poetry==1.8.2

# Configuring poetry
RUN poetry config virtualenvs.create false
RUN poetry config cache-dir /tmp/poetry_cache

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Installing requirements
RUN --mount=type=cache,target=/tmp/poetry_cache poetry install --only main
# Removing gcc
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copying actuall application
COPY . /app/src/
RUN --mount=type=cache,target=/tmp/poetry_cache poetry install --only main

# DEV
RUN addgroup --gid 1000 ubuntu
RUN useradd -lm -u 1000 -g 1000 ubuntu
USER ubuntu

# CMD ["/usr/local/bin/python", "-m", "backend"]
CMD ["sleep", "infinity"]

FROM prod AS dev

RUN --mount=type=cache,target=/tmp/poetry_cache poetry install
