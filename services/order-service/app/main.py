from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Order Service Running"}

@app.get("/orders")
def get_orders():
    return {
        "orders": [
            {"id": 1, "product": "Laptop", "user": "Sabari"},
            {"id": 2, "product": "Phone", "user": "DevOps User"}
        ]
    }
