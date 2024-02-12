from src.server.server import app

PORT = 3000

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
