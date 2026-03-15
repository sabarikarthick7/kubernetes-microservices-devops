from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Notification Service Running"}

@app.get("/notify")
def send_notification():
    return {"status": "Notification sent successfully"}
