import uvicorn
from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import subprocess

app = FastAPI()

# @app.get("/", response_class=HTMLResponse)
# def root():
#     with open("index.html", "r") as root_file:
#         return root_file.read()
    

@app.post("/api/simulate")
def read_root(payload: dict):
    FILE = payload.get("path")
    subprocess.run(["python", FILE])
    
    """
    Endpoint that returns a simple welcome message.
    """
    return {"message": "Hello, World!"}

app.mount("/", StaticFiles(directory=".",html=True), name="static")


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)