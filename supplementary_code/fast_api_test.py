from fastapi import FastAPI

app = FastAPI()

# Decorator syntax defines endpoint in API
@app.get("/")
async def root():
    return {"message": "Hello World"}
a
@app.get("/square")
async def square(num: int): # Specifying type provides automatic validation
    result = num **2 
    return {"squared": result}