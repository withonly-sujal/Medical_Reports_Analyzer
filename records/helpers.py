medical_ranges = {
    "Hemoglobin": {"unit": "gm/dL", "low": 13.5, "high": 18.0},
    "WBC": {"unit": "10^9/L", "low": 4000, "high": 11000},
    "Platelets": {"unit": "10^9/L", "low": 150, "high": 400},
    "Lymphocytes": {"unit": "%", "low": 20, "high": 40},
    "Mean Platelet Volume (MPV)": {"unit": "fL", "low": 7.2, "high": 11.7},
    "PDW": {"unit": "%", "low": 9, "high": 11.7},
    "Bilirubin - Total": {"unit": "mg/dL", "low": 0.4, "high": 1.2},
    "Bilirubin - Direct": {"unit": "mg/dL", "low": 0.1, "high": 0.4},
    "Bilirubin - Indirect": {"unit": "mg/dL", "low": 0.1, "high": 0.8},
    "SGOT": {"unit": "U/L", "low": 0, "high": 40}, 
    "SGPT": {"unit": "U/L", "low": 0, "high": 45},  
    "ALP": {"unit": "U/L", "low": 44, "high": 147},  
    "GGT": {"unit": "U/L", "low": 0, "high": 50},    
    "Total Protein": {"unit": "g/dL", "low": 6.0, "high": 8.3},
    "Albumin": {"unit": "g/dL", "low": 3.5, "high": 5.0},
    "Globulin": {"unit": "g/dL", "low": 2.0, "high": 3.5},
    "A/G Ratio": {"unit": "-", "low": 1.0, "high": 2.2},
    "Vitamin B12": {"unit": "pg/mL", "low": 200, "high": 900},
    "Vitamin D (25-OH)": {"unit": "ng/mL", "low": 20, "high": 50}, 
    "Folic Acid": {"unit": "ng/mL", "low": 2.7, "high": 17.0},

    "Iron": {"unit": "µg/dL", "low": 60, "high": 170},
    "Ferritin": {"unit": "ng/mL", "low": 20, "high": 500}, 
    "TIBC": {"unit": "µg/dL", "low": 240, "high": 450}, 
    "Transferrin Saturation": {"unit": "%", "low": 20, "high": 50},

    "Calcium": {"unit": "mg/dL", "low": 8.5, "high": 10.5},
    "Magnesium": {"unit": "mg/dL", "low": 1.7, "high": 2.2},
    "Zinc": {"unit": "µg/dL", "low": 70, "high": 120},

    "Phosphorus": {"unit": "mg/dL", "low": 2.5, "high": 4.5},
    "Potassium": {"unit": "mmol/L", "low": 3.5, "high": 5.0},
    "Sodium": {"unit": "mmol/L", "low": 135, "high": 145},
    "Heart Rate": {"unit": "bpm", "low": 60, "high": 100},  
    "Blood Pressure - Systolic": {"unit": "mmHg", "low": 90, "high": 120},
    "Blood Pressure - Diastolic": {"unit": "mmHg", "low": 60, "high": 80},
    "Pulse Rate": {"unit": "bpm", "low": 60, "high": 100},

    "Respiratory Rate": {"unit": "breaths/min", "low": 12, "high": 20},
    "Temperature": {"unit": "°F", "low": 97.0, "high": 99.0},

    "Oxygen Saturation (SpO2)": {"unit": "%", "low": 95, "high": 100},
    "Blood Glucose - Fasting": {"unit": "mg/dL", "low": 70, "high": 99},
    "Blood Glucose - Postprandial": {"unit": "mg/dL", "low": 80, "high": 140},
    "HbA1c": {"unit": "%", "low": 4.0, "high": 5.6},
    "Absolute Lymphocyte Count": {"unit": "/uL", "low": 990.00, "high": 3150.00},
    "CD3 (Total T cells)": {"unit": "%", "low": 59.00, "high": 83.00},
    "Absolute CD3": {"unit": "/uL", "low": 677.00, "high": 2383.00},
    "CD4 (Helper T cells)": {"unit": "%", "low": 31.00, "high": 59.00},
    "Absolute CD4": {"unit": "/uL", "low": 424.00, "high": 1509.00},
    "CD8 (Suppressor T cells)": {"unit": "%", "low": 12.00, "high": 38.00},
    "Absolute CD8": {"unit": "/uL", "low": 169.00, "high": 955.00},
    "CD4 / CD8": {"unit": "Ratio", "low": 1.00, "high": float('inf')}

     
}




term_simplifications = {
    "Leucopenia": {
        "definition": "Low white blood cell count, which can weaken your immune system.",
        "domain": "Immunology"
    },
    "Macrocytosis": {
        "definition": "Larger than normal red blood cells, which may indicate vitamin B12 or folate deficiency.",
        "domain": "Hematology"
    },
    "Thrombocytopenia": {
        "definition": "A condition where you have fewer platelets than normal, which can affect clotting.",
        "domain": "Hematology"
    },
    "PDW": {
        "definition": "Platelate Distribution Width, suggest conditions like inflammation, cancer, or vascular diseases",
        "domain": "hematology"
    },
    "Hypertension": {
        "definition": "High blood pressure, which increases the risk of stroke and heart disease.",
        "domain": "Cardiology"
    },
    "Hypotension": {
        "definition": "Low blood pressure that can cause dizziness and fainting.",
        "domain": "Cardiology"
    },
    "Tachycardia": {
        "definition": "An unusually fast heart rate, which can result from stress, fever, or heart issues.",
        "domain": "Cardiology"
    },
    "Bradycardia": {
        "definition": "An abnormally slow heart rate, which may cause fatigue or fainting.",
        "domain": "Cardiology"
    },
    "Hypoxia": {
        "definition": "Low oxygen levels in the blood, causing shortness of breath or confusion.",
        "domain": "Pulmonology"
    },
    "Hyperglycemia": {
        "definition": "High blood sugar, a sign of diabetes or poor diet control.",
        "domain": "Endocrinology"
    },
    "Hypoglycemia": {
        "definition": "Low blood sugar that can cause shaking, confusion, and even unconsciousness.",
        "domain": "Endocrinology"
    },
    "Diabetes": {
        "definition": "A chronic condition where the body can't regulate blood sugar properly.",
        "domain": "Endocrinology"
    },
    "Hyperkalemia": {
        "definition": "High potassium levels, which can cause dangerous heart rhythms.",
        "domain": "Nephrology / Cardiology"
    },
    "Hypokalemia": {
        "definition": "Low potassium, possibly causing muscle weakness and irregular heartbeat.",
        "domain": "Nephrology"
    },
    "Hyponatremia": {
        "definition": "Low sodium levels that can lead to confusion or seizures.",
        "domain": "Nephrology"
    },
    "Hypernatremia": {
        "definition": "Excess sodium which may lead to dehydration symptoms.",
        "domain": "Nephrology"
    },
    "Hypocalcemia": {
        "definition": "Low calcium causing muscle cramps or tingling sensations.",
        "domain": "Endocrinology"
    },
    "Hypercalcemia": {
        "definition": "High calcium which can cause kidney stones, fatigue, or confusion.",
        "domain": "Endocrinology"
    },
    "Vitamin B12 Deficiency": {
        "definition": "Lack of Vitamin B12 causing fatigue, memory issues, and anemia.",
        "domain": "Nutrition / Hematology"
    },
    "Vitamin D Deficiency": {
        "definition": "Low Vitamin D levels leading to weak bones, fatigue, or mood issues.",
        "domain": "Endocrinology"
    },
    "Iron Deficiency": {
        "definition": "Lack of iron often leading to anemia and fatigue.",
        "domain": "Hematology / Nutrition"
    },
    "Folic Acid Deficiency": {
        "definition": "A vitamin deficiency that can cause anemia and neural tube defects in pregnancy.",
        "domain": "Nutrition"
    },
    "Hyperbilirubinemia": {
        "definition": "High bilirubin levels, often causing jaundice and indicating liver dysfunction.",
        "domain": "Hepatology"
    },
    "Hepatitis": {
        "definition": "Inflammation of the liver often indicated by elevated SGOT and SGPT.",
        "domain": "Hepatology"
    },
    "Liver Dysfunction": {
        "definition": "Poor liver performance shown by abnormal liver enzymes like ALP, GGT, or low albumin.",
        "domain": "Hepatology"
    },
    "Anemia": {
        "definition": "A condition where your blood has lower than normal red blood cells or hemoglobin.",
        "domain": "Hematology"
    },
    "Leukocytosis": {
        "definition": "An increased white blood cell count, often indicating infection or inflammation.",
        "domain": "Hematology"
    },
    "Leukopenia": {
        "definition": "Low white blood cell count, increasing the risk of infections.",
        "domain": "Hematology"
    },
    "Thrombocytopenia": {
        "definition": "Low platelet count, which can lead to increased bleeding or bruising.",
        "domain": "Hematology"
    },
    "Thrombocytosis": {
        "definition": "Elevated platelet count, which may increase the risk of clotting.",
        "domain": "Hematology"
    }
    




}
