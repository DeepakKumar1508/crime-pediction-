import pickle

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

print("\nCrime Prediction System\n")

population = int(input("Enter Population: "))
unemployment = float(input("Enter Unemployment Rate: "))
poverty = float(input("Enter Poverty Rate: "))

result = model.predict(
    [[population, unemployment, poverty]]
)

if result[0] == 1:
    print("\nPrediction: High Crime Area")
else:
    print("\nPrediction: Low Crime Area")