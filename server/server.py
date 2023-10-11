import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .config import Config

class Server:
    def __init__(self, app: FastAPI, config: Config):
        self.app = app
        self.host = "0.0.0.0"
        self.port = config.PORT
        self.workers = config.SERVER_WORKERS
        self.timeout = config.SERVER_TIMEOUT
        self.reload = config.SERVER_RELOAD
        self.productName = config.PRODUCT_NAME
        self.moduleName = config.MODULE_NAME
        self.version = config.VERSION
        self.allowCorsOrigin = config.ALLOW_CORS_ORIGIN
        self.trustedHosts = config.TRUSTED_HOSTS
        

    def start(self):
        self.setupMiddleware()

        uvicorn.run(
            "main:app",
            host=self.host,
            port=self.port,
            workers=self.workers,
            timeout_keep_alive=self.timeout,
            reload=self.reload
        )

    def setupMiddleware(self):
        self.app.add_middleware(CORSMiddleware, allow_origins=[self.allowCorsOrigin])
        self.app.add_middleware(TrustedHostMiddleware, allowed_hosts=self.trustedHosts)

    def shutdown(self):
        pass
