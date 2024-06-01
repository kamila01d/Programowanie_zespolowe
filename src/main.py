from fastapi import FastAPI

app = FastAPI()


@app.get("/healtz")
def read_root():
    return {"Status": "Ok!"}
