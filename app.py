from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Crime Prediction ML Project")
    return "Crime Prediction Project is Running"

if __name__ == "__main__":
    app.run()