FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv sync --frozen

COPY main.py .

EXPOSE 3001

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3001"]