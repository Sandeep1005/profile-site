from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the folder where your images are stored
app.mount("/static", StaticFiles(directory="/static"), name="static")
