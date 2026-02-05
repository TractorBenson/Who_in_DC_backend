FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# Copy app code
COPY . .

EXPOSE 8000

VOLUME ["/app/data"]

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
