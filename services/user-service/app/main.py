from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "User Service Running"}

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "Sabari"},
            {"id": 2, "name": "DevOps User"}
        ]
    }
