# records/helpers.py

medical_ranges = {
    "Hemoglobin": {"unit": "gm/dL", "low": 13.5, "high": 18.0},
    "WBC": {"unit": "10^9/L", "low": 4.0, "high": 11.0},
    "Platelets": {"unit": "10^9/L", "low": 150, "high": 400},
    
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
    
}
