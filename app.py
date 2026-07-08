from flask import Flask

app = Flask(__name__)
VERSION = "1.0.0"

@app.route("/")
def home():
    return {"message": "CI/CD pipeline demo", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
