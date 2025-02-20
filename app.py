from fastapi import FastAPI

# start with uvicorn app:app --reload
# (app.py:app)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Morten!"}

@app.get("/{name}")
def read_root(name: str):
    return {"message": f"Hello, {name}!"}

        