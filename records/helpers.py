# records/helpers.py

medical_ranges = {
    "Hemoglobin": {"unit": "gm/dL", "low": 13.5, "high": 18.0},
    "WBC": {"unit": "10^9/L", "low": 4000, "high": 11000},
    "Platelets": {"unit": "10^9/L", "low": 150, "high": 400},
    "Lymphocytes": {"unit": "%", "low": 20, "high": 40},
    "Mean Platelet Volume (MPV)": {"unit": "fL", "low": 7.2, "high": 11.7},
    "PDW": {"unit": "%", "low": 9, "high": 11.7},
    "Bilirubin - Total": {"unit": "mg/dL", "low": 0.4, "high": 1.2}
    
}


term_simplifications = {
    "Anemia": {
        "definition": "A condition where your blood has lower than normal red blood cells or hemoglobin.",
        "domain": "Hematology"
    },
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
    }
    
}
