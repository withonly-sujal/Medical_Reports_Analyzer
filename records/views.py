from django.shortcuts import render, redirect
from django.http import JsonResponse
import pdfplumber
import re
from .helpers import medical_ranges, term_simplifications

def homepage(request):
    return render(request, 'home.html')


def upload_document(request):
    if request.method == 'POST' and request.FILES.get('document'):
        file = request.FILES['document']
        lines = []

        # Step 1: Extract line-by-line text from PDF
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    lines.extend(page_text.split('\n'))

        highlights = []
        highlighted_lines = []

        for line in lines:
            line_copy = line  # modified version of line
            for test, data in medical_ranges.items():
                if test.lower() in line.lower():
                    match = re.search(r"([0-9.]+)", line)
                    if match:
                        try:
                            value = float(match.group(1))
                        except ValueError:
                            continue
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

                        # Inline annotation (optional)
                        line_copy = line_copy.replace(str(value), f"{value} ({status})")

            highlighted_lines.append(line_copy)

        raw_text = "\n".join(highlighted_lines)

        return render(request, 'results.html', {
            "highlights": highlights,
            "raw_text": raw_text
        })

    return render(request, 'upload.html')


def translated_terms(request):
    if request.method == 'POST':
        text = request.POST.get("text")
        matched_terms = []

        for term, info in term_simplifications.items():
            if term.lower() in text.lower():
                matched_terms.append({
                    "term": term,
                    "definition": info["definition"],
                    "domain": info["domain"]
                })

        return render(request, 'translation.html', {
            "matched_terms": matched_terms,
            "original_text": text
        })

    return redirect('home')
