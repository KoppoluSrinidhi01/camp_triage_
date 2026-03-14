import pandas as pd
import joblib
import time

# ASCII hourglass animation
def hourglass():
    art = [
        "      _____",
        "     /     \\",
        "    /       \\",
        "    \\       /",
        "     \\_____/",
        "       / \\",
        "      /   \\",
        "     /_____\\"
    ]
    print("\nModel inference starting...\n")
    for line in art:
        print(line)
        time.sleep(1)
    print("\nWaiting 10 seconds before prediction...\n")
    time.sleep(10)

print("Loading model...")
model = joblib.load("triage_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# ----------------------
# Real-time user input
# ----------------------
print("Enter patient data for prediction:")

# Minimal useful features for demo
features = [
    "age",
    "glucose_min",
    "hemoglobin_min",
    "hematocrit_min",
    "lactate,poc_min",
    "inr_min",
    "2ndarymalig",
    "abdomhernia"
]

inputs = {}
for col in features:
    val = input(f"{col}: ")
    try:
        # numeric input
        inputs[col] = float(val)
    except:
        # categorical input
        inputs[col] = val

# create DataFrame
sample = pd.DataFrame([inputs])

# encode categorical columns if needed
sample = pd.get_dummies(sample)

# fill remaining model columns with 0 so prediction works
sample = sample.reindex(columns=model_columns, fill_value=0)

# ----------------------
# Hourglass animation
# ----------------------
hourglass()

# Predict
prediction = model.predict(sample)

print("\nPredicted ESI Level:", prediction[0] + 1)