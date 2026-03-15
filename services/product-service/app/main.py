from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Product Service Running"}

@app.get("/products")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Phone"}
        ]
    }
