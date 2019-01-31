import pdfkit

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    pdf = pdfkit.from_url('http://google.com', False)
    response = HttpResponse(pdf)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline; filename=out.pdf'
    return response
