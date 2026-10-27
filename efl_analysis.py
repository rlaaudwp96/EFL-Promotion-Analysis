"""Analyze English Championship performance metrics associated with promotion."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "efl_table_final_clean.csv"
FEATURES = ["Total_Points", "GF", "GA", "GD", "Shot_Accuracy", "Net_SOT", "Card_Points"]


def main():
    df = pd.read_csv(DATA).dropna(subset=FEATURES + ["Promoted"])
    df["promoted_flag"] = df["Promoted"].eq("Yes").astype(int)
    X = df[FEATURES]
    y = df["promoted_flag"]

    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    prep = Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    logistic = Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))]).fit(x_train, y_train)
    forest = Pipeline(
        [
            ("impute", SimpleImputer(strategy="median")),
            ("model", RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced")),
        ]
    ).fit(x_train, y_train)

    for name, model in [("Logistic regression", logistic), ("Random forest", forest)]:
        pred = model.predict(x_test)
        probability = model.predict_proba(x_test)[:, 1]
        print(f"{name}: accuracy={accuracy_score(y_test, pred):.3f}, ROC AUC={roc_auc_score(y_test, probability):.3f}")

    linear = LinearRegression().fit(df[["Total_Points"]], df["GD"])
    print(f"Rows: {len(df):,}; points-to-goal-difference R2: {linear.score(df[['Total_Points']], df['GD']):.3f}")
    print("\nRandom forest classification report:")
    print(classification_report(y_test, forest.predict(x_test), target_names=["Not promoted", "Promoted"]))


if __name__ == "__main__":
    main()
