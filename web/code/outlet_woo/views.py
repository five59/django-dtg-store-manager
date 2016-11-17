from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import A3
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields as extension_fields
from creative import models as cr
from catalog import models as ca
from outlet_woo import models as wc
from reportlab.lib.units import inch


def pdf_productcatalog(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="allproducts.pdf"'
    p = canvas.Canvas(response, pagesize=A3)
    p.setTitle(_("Product Catalog"))
    # p.setAuthor()
    width, height = A3

    # PC = PageContent
    pc = {
        ['sku':]
    }

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
