from fastapi import FastAPI

def health_controller(app: FastAPI):
    @app.get("/health")
    def health():
        return {"status": "healthy"}