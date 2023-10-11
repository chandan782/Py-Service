import os

class Config:
    ALLOW_CORS_ORIGIN = os.getenv("ALLOW_CORS_ORIGIN", "*")
    ALLOW_CORS_METHODS = os.getenv("ALLOW_CORS_METHODS", "POST")
    MODULE_NAME = os.getenv("MODULE_NAME", "Basket-Service")
    PORT = int(os.getenv("PORT", 8081))
    PRODUCT_NAME = os.getenv("PRODUCT_NAME", "Basket")
    WAIT_TIME_BEFORE_KILL = int(os.getenv("WAIT_TIME_BEFORE_KILL", 10))
    VERSION = os.getenv("VERSION", "v0.0.0")
    TRUSTED_HOSTS = os.getenv("TRUSTED_HOSTS", "localhost,127.0.0.1")
    SERVER_WORKERS = int(os.getenv("SERVER_WORKERS", 4))
    SERVER_TIMEOUT = int(os.getenv("SERVER_TIMEOUT", 30))
    SERVER_RELOAD = bool(int(os.getenv("SERVER_RELOAD", 1)))
