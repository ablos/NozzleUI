from fastapi import FastAPI
from routers import printer
from utils.config import config

app = FastAPI(title="NozzleUI API")

app.include_router(printer.router)

@app.get("/")
def read_root():
    return {"message", "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)