# app.py

from flask import Flask, render_template, request, session
import joblib
import numpy as np
from food_recommender import generate_food_recommendation



model = joblib.load("model/final_model.pkl")



condition_to_finding = {
    "anemia": "LOW hemoglobin / RBC → Possible Anemia",
    "diabetes": "HIGH blood sugar → Risk of Diabetes",
    "cholesterol_high": "HIGH cholesterol → Risk of Heart Disease",
    "cholesterol_low": "LOW cholesterol → Hormone imbalance risk",
    "vitamin_d_deficiency": "LOW vitamin D → Vitamin D Deficiency",
    "vitamin_d_toxicity": "HIGH vitamin D (Toxicity possible if persistent)",
    "kidney_issue": "HIGH creatinine → Possible Kidney Issue",
    "low_creatinine": "LOW creatinine → Muscle loss or liver condition",
    "uric_acid_low": "LOW uric acid → Possible nutrient imbalance",
    "hypoglycemia": "LOW sugar → Risk of Hypoglycemia",
    "polycythemia": "HIGH RBC → Risk of Polycythemia",
    "dehydration": "High concentration markers → Possible Dehydration",
    "iron_overload": "HIGH iron → Risk of Iron Overload",
    "borderline_low_iron": "Low-normal iron → Monitor for deficiency",
    "wbc_low": "LOW WBC → Possible infection risk",
    "wbc_high": "HIGH WBC → Possible infection/inflammation",
    "platelets_low": "LOW Platelets → Bleeding Risk",
    "platelets_high": "HIGH Platelets → Clotting Risk"
}

NORMAL_RANGES = {
    'hemoglobin': (13.5, 17.5),
    'sugar': (70, 140),
    'cholesterol': (125, 200),
    'iron': (60, 170),
    'vitamin_d': (30, 100),
    'platelets': (150000, 450000),
    'wbc_count': (4000, 11000),
    'rbc_count': (4.7, 6.1),
    'creatinine': (0.6, 1.3),
    'uric_acid': (3.5, 7.2)
}

app = Flask(__name__)
app.secret_key = 'heal_secret'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input")
def input_page():
    return render_template("index.html", previous=session.get("last_input", {}))


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        fields = list(NORMAL_RANGES.keys())
        inputs = [float(request.form.get(field)) for field in fields]
        input_dict = dict(zip(fields, inputs))
        session["last_input"] = input_dict

        
        prediction = list(model.predict([inputs])[0])
        labels = list(condition_to_finding.keys())
        predicted_conditions = [label for label, value in zip(labels, prediction) if value == 1]
        findings = [condition_to_finding.get(label, label) for label in predicted_conditions]

        
        normal_flags = [field.replace('_', ' ').title()
                        for field, (low, high) in NORMAL_RANGES.items()
                        if low <= input_dict[field] <= high]

        
        already_flagged = " ".join(findings).lower()
        for field, (low, high) in NORMAL_RANGES.items():
            val = input_dict[field]
            if val < low and field.replace('_', ' ') not in already_flagged:
                findings.append(f"LOW {field.replace('_', ' ').title()} (below normal)")
            elif val > high and field.replace('_', ' ') not in already_flagged:
                findings.append(f"HIGH {field.replace('_', ' ').title()} (above normal)")

        
        eat, avoid = generate_food_recommendation(findings)

        return render_template("results.html",
                               findings=findings,
                               eat=eat,
                               avoid=avoid,
                               normal_flags=normal_flags,
                               input_data=input_dict)

    except Exception as e:
        return f"Something went wrong: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
