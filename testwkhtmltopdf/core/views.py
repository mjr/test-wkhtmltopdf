import pdfkit

from django.http import HttpResponse
from django.shortcuts import render


try:
    config = pdfkit.configuration(wkhtmltopdf='bin/wkhtmltopdf')
except:
    config = None


def home(request):
    pdf = pdfkit.from_url('http://google.com', False, configuration=config)
    response = HttpResponse(pdf)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline; filename=out.pdf'
    return response
