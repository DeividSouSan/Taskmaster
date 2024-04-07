from src import create_app

app = create_app("DevelopmentConfig")

if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0", debug=True)
