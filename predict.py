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

print("Loading dataset...")

# DATA PATH
df = pd.read_csv("data/triage_data.csv")

# take one patient sample
sample = df.drop(columns=["esi"]).iloc[[0]]

# encode categorical columns
sample = pd.get_dummies(sample)

# align columns with training columns
sample = sample.reindex(columns=model_columns, fill_value=0)

# hackathon delay requirement
hourglass()

prediction = model.predict(sample)

print("\nPredicted ESI Level:", prediction[0] + 1)