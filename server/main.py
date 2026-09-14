from fastapi import FastAPI

app = FastAPI(title="Nginx Under the Hood")


@app.get("/")
def home():
    return {
        "status": "ok",
        "service": "reached home!",
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "server",
    }


@app.get("/api/message")
def message():
    return {
        "message": "Hello from the server!",
    }