from fastapi import FastAPI
from app.controller.health_controller import health_controller
from app.controller.version_controller import version_controller

class RouteHandler:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()

    # Setup routes
    def setup_routes(self):
        # Add home route
        @self.app.get("/")
        def home():
            return {"message": "Welcome to my FastAPI server!"}

        # Add health route
        health_controller(self.app)

        # Add version route
        version_controller(self.app)
        
        # Add a dummy POST route
        @self.app.post("/dummy-post")
        def dummy_post(request_data: dict):
            return {"message": "Received a POST request", "data": request_data}

    def shutdown(self):
        pass
