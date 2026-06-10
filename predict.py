@app.route("/predict")
def predict():

    primary_type = int(request.args.get("primary_type"))
    district = int(request.args.get("district"))
    ward = int(request.args.get("ward"))
    community = int(request.args.get("community"))
    day = int(request.args.get("day"))
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))

    features = np.array([
        [primary_type, district, ward,
         community, day, month, year]
    ])

    prediction = model.predict(features)[0]

    return f"""
    <h2>Predicted Count: {prediction}</h2>
    <a href="/">Back</a>
    """