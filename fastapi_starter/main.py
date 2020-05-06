import fastapi

app = fastapi.FastAPI()


@app.get("/")
async def root():
    """API root."""
    return {"message": "Hello World"}
