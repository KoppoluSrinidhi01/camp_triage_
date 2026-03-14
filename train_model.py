import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import joblib

print("Loading dataset...")

# DATA PATH
df = pd.read_csv("data/triage_data.csv")

print("Dataset shape:", df.shape)

target = "esi"

# remove rows with missing target
df = df.dropna(subset=[target])

# split features and target
X = df.drop(columns=[target])
y = df[target] - 1   # convert 1-5 → 0-4

print("Encoding categorical features...")

# convert categorical columns
X = pd.get_dummies(X)

print("Total features after encoding:", X.shape[1])

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = XGBClassifier(
    objective="multi:softmax",
    num_class=5,
    eval_metric="mlogloss",
    tree_method="hist"
)

model.fit(X_train, y_train)

print("Evaluating model...")

preds = model.predict(X_test)

acc = accuracy_score(y_test, preds)

print("Model Accuracy:", acc)

print("Saving model...")

joblib.dump(model, "triage_model.pkl")

# save training columns
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("Model saved!")