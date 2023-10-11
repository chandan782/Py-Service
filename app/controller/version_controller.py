from fastapi import FastAPI
from server.config import Config

def version_controller(app: FastAPI):
    @app.get("/version")
    def version():
        return {"version": Config.VERSION, "productName": Config.PRODUCT_NAME, "moduleName": Config.MODULE_NAME}