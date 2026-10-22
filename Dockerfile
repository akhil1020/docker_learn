FROM  python:3.12-slim

# Copy uv from its official image
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files first for better build caching  
## for pip-  copy requirements.txt .
COPY pyproject.toml uv.lock ./

# Install dependencies without installing the project yet
## for pip- run pip install --no-chache-dir -r requirements.txt
RUN uv sync --frozen --no-install-project

# Copy application code
COPY . .

# Install the project
## for pip no need this
RUN uv sync --frozen


EXPOSE 8080

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



