import os

from dotenv import load_dotenv
from src import create_app

load_dotenv()
config = os.environ.get("CONFIG")

app = create_app(config)

if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0", debug=True)
