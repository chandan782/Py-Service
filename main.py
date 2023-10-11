import time
import signal
from fastapi import FastAPI
from routes.routes import RouteHandler
from server.server import Server
import logging
from server.config import Config

app = FastAPI()
server = Server(app, Config)

route_handler = RouteHandler(app)

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] - %(message)s")

def handle_shutdown(signal, frame):
    logging.info("Received shutdown signal.")
    server.shutdown()
    logging.info("Shutting down gracefully...")
    time.sleep(server.config.WAIT_TIME_BEFORE_KILL)
    exit(0)

def start():
    setup_logging()
    server.start()

if __name__ == "__main__":
    # Register signal handlers
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    # Start the server
    start()
