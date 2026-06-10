from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Crime Prediction System</h1>

    <form action="/predict">
        Population:<br>
        <input type="number" name="population"><br><br>

        Unemployment Rate:<br>
        <input type="number" name="unemployment"><br><br>

        Poverty Rate:<br>
        <input type="number" name="poverty"><br><br>

        <input type="submit" value="Predict">
    </form>
    """

@app.route("/predict")
def predict():
    unemployment = float(request.args.get("unemployment"))
    poverty = float(request.args.get("poverty"))

    if unemployment > 8 or poverty > 20:
        return "<h2>⚠ High Crime Risk Area</h2>"
    else:
        return "<h2>✅ Low Crime Risk Area</h2>"