from django.shortcuts import render
from django.http import JsonResponse
import pdfplumber
import re
from .helpers import medical_ranges

def upload_document(request):
    if request.method == 'POST' and request.FILES.get('document'):
        file = request.FILES['document']
        extracted_text = ""

        # Step 1: Extract text from PDF
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"

        # Step 2: Parse values and compare with normal ranges
        highlights = []
        for test, data in medical_ranges.items():
            pattern = rf"{test}[:\s]*([0-9.]+)"
            match = re.search(pattern, extracted_text, re.IGNORECASE)
            if match:
                value = float(match.group(1))
                status = "Normal"
                if value < data['low']:
                    status = "Low"
                elif value > data['high']:
                    status = "High"

                highlights.append({
                    "test": test,
                    "value": value,
                    "unit": data["unit"],
                    "status": status
                })

        return render(request, 'results.html', {
            "highlights": highlights,
            "raw_text": extracted_text
        })

    return render(request, 'upload.html')
