from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Crime Count Prediction</h1>

    <form action="/predict" method="get">
        <input type="number" name="primary_type" placeholder="Primary Type"><br><br>
        <input type="number" name="district" placeholder="District"><br><br>
        <input type="number" name="ward" placeholder="Ward"><br><br>
        <input type="number" name="community" placeholder="Community Area"><br><br>
        <input type="number" name="day" placeholder="Day"><br><br>
        <input type="number" name="month" placeholder="Month"><br><br>
        <input type="number" name="year" placeholder="Year"><br><br>

        <button type="submit">Predict</button>
    </form>
    """

@app.route("/predict")
def predict():
    prediction = 13

    return f"""
    <h2>Predicted Count: {prediction}</h2>
    <a href="/">Back</a>
    """

# Required for Vercel
app = app