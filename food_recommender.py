# food_recommender.py

def generate_food_recommendation(findings):
    """
    Given a list of findings (e.g. "LOW hemoglobin → Possible Anemia"),
    returns two lists:
      - foods to eat with explanations
      - foods to avoid with explanations
    """
    eat = []
    avoid = []

    for finding in findings:
        
        if ("LOW hemoglobin" in finding or "LOW iron" in finding or 
            "Borderline LOW hemoglobin" in finding):
            eat += [
                "Spinach (rich in iron and vitamins, boosts hemoglobin synthesis)",
                "Beetroot (improves blood flow and increases hemoglobin)",
                "Red Meat (contains heme iron, which is easily absorbed)",
                "Lentils (good source of plant-based iron and protein)"
            ]
            avoid += [
                "Tea (tannins reduce iron absorption)",
                "Coffee (similarly hinders iron absorption)"
            ]

        
        if ("HIGH blood sugar" in finding or "Borderline HIGH blood sugar" in finding):
            eat += [
                "Whole Grains (low glycemic index, slow digestion)",
                "Leafy Greens (high fiber, helps stabilize blood sugar)",
                "Nuts (contain healthy fats that help regulate blood sugar)"
            ]
            avoid += [
                "Sugary foods (cause rapid blood sugar spikes)",
                "Soda (high in sugar, offers no nutrition)",
                "White Bread (refined carbohydrates that raise blood sugar)"
            ]

       
        if ("HIGH cholesterol" in finding or "Borderline HIGH cholesterol" in finding):
            eat += [
                "Oats (soluble fiber can reduce cholesterol absorption)",
                "Avocado (rich in monounsaturated fats that lower LDL)",
                "Salmon (high in omega-3 fatty acids, beneficial for heart health)",
                "Walnuts (help lower cholesterol levels)"
            ]
            avoid += [
                "Fried foods (rich in trans fats that increase cholesterol)",
                "Red Meat (high in saturated fats)",
                "Butter (contains animal fats that raise cholesterol)"
            ]

        
        if ("LOW vitamin D" in finding or "Borderline LOW vitamin D" in finding):
            eat += [
                "Fatty Fish like Salmon (natural source of vitamin D3)",
                "Egg Yolk (provides vitamin D)",
                "Fortified Milk (enriched with vitamin D)",
                "Mushrooms (especially when exposed to sunlight)"
            ]
            

        
        if "HIGH vitamin D" in finding:
            avoid += [
                "Excess vitamin D supplements (should only be taken if prescribed)",
                "Overconsumption of fortified foods (if leading to high intake)"
            ]

        
        if ("HIGH creatinine" in finding or "Borderline HIGH creatinine" in finding or
            "kidney" in finding):
            eat += [
                "Watermelon (high water content helps with hydration)",
                "Berries (rich in antioxidants that support kidney function)",
                "Low-sodium foods (reduce kidney strain)"
            ]
            avoid += [
                "Red Meat (high protein load can overburden the kidneys)",
                "Salt (excessive salt can increase blood pressure and strain kidneys)"
            ]

        
        if "HIGH iron" in finding:
            avoid += [
                "Red Meat (may contribute to iron overload)",
                "Iron supplements (unless medically necessary)"
            ]
            

       
        if ("HIGH uric acid" in finding or "Borderline HIGH uric acid" in finding):
            eat += [
                "Cherries (shown to help reduce uric acid levels)",
                "Low-fat dairy (good protein source with low purines)",
                "Whole grains (offer a balanced nutrient profile without high purine)"
            ]
            avoid += [
                "Organ meats (very high in purines)",
                "Alcohol (can increase uric acid levels)",
                "Seafood (moderate purine levels, best consumed in moderation)"
            ]

        
        if "HIGH WBC" in finding:
            avoid += [
                "Sugary foods (can promote inflammation)"
            ]
        if "LOW WBC" in finding:
            eat += [
                "Citrus fruits (rich in vitamin C, boosting immunity)",
                "Garlic (has natural antibacterial properties)",
                "Yogurt (contains beneficial probiotics)"
            ]
            
        
        if "LOW Platelets" in finding:
            eat += [
                "Papaya (may help boost platelet count)",
                "Pomegranate (rich in antioxidants)",
                "Folic acid-rich foods (support blood health)"
            ]
            avoid += [
                "Alcohol (can lower platelet count)"
            ]
        
        if "HIGH Platelets" in finding:
            avoid += [
                "Excessive iron supplements (may interfere with platelet function)",
                "Smoking (linked to elevated platelet counts)"
            ]

    
    return sorted(set(eat)), sorted(set(avoid))
