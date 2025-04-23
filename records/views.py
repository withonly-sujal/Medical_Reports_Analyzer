from django.shortcuts import render
from django.http import JsonResponse
import pdfplumber
from .models import MedicalTerm

from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'home.html')


def upload_document(request):
    if request.method == 'POST' and request.FILES['document']:
        file = request.FILES['document']
        
        # Parse PDF
        with pdfplumber.open(file) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()

        # You can add parsing and logic to highlight abnormalities here

        return JsonResponse({'message': 'File processed successfully', 'data': text})
    return render(request, 'upload.html')


